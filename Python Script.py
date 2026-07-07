"""
Synthetic SaaS Retention & Cohort Dataset Generator (Tuned Version)
------------------------------------------------------------------

Output:
- saas_retention_events_raw.csv

This script generates a raw event-level SaaS dataset for retention/cohort analysis.
It intentionally does NOT export analytical derived fields such as:
signup_week, cohort_index, churned, churn_status, is_core_feature, or reached_aha_moment.

Those fields should be calculated later using SQL.
"""

import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# ==================================================
# CONFIG
# ==================================================
np.random.seed(42)
random.seed(42)

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 6, 30, 23, 59, 59)

NUM_USERS = 13_500
OUTPUT_FILE = "saas_retention_events_raw.csv"

SOURCES = ["ads", "organic", "referral", "social"]
SOURCE_PROBS = [0.40, 0.30, 0.20, 0.10]

DEVICES = ["mobile", "desktop", "tablet"]
DEVICE_PROBS = [0.58, 0.36, 0.06]

COUNTRIES = ["US", "UK", "France", "Indonesia", "India", "Australia", "Germany"]
COUNTRY_PROBS = [0.25, 0.14, 0.10, 0.16, 0.16, 0.09, 0.10]

ACTIVITY_EVENTS = ["login", "dashboard_view", "feature_used", "report_created", "invite_team_member"]
CORE_EVENTS = ["feature_used", "report_created", "invite_team_member"]

RAW_COLUMNS = [
    "event_id",
    "user_id",
    "event_time",
    "event_name",
    "source",
    "device",
    "country",
    "plan_type",
    "subscription_status",
    "revenue",
]

FORBIDDEN_RAW_COLUMNS = {
    "signup_date", "signup_week", "cohort_start_date", "event_week",
    "cohort_index", "max_observable_week", "churned", "churn_status",
    "churn_week", "is_core_feature", "reached_aha_moment", "final_plan_type",
    "last_activity_date", "total_events", "total_core_feature_events",
}

# ==================================================
# HELPERS
# ==================================================
def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return np.log(p / (1 - p))

def sigmoid(x: float) -> float:
    return 1 / (1 + np.exp(-x))

def get_week_start(dt: datetime) -> datetime:
    d = datetime(dt.year, dt.month, dt.day)
    return d - timedelta(days=d.weekday())

def base_retention(week_index: int) -> float:
    """Base retention before segment adjustments. Tuned to produce target overall retention."""
    curve = {
        0: 1.00,
        1: 0.82,
        2: 0.58,
        3: 0.41,
        4: 0.31,
        5: 0.245,
        6: 0.195,
        7: 0.155,
        8: 0.130,
    }
    if week_index in curve:
        return curve[week_index]
    return max(0.055, 0.090 * (0.94 ** (week_index - 8)))

def source_delta(source: str) -> float:
    return {"ads": -0.18, "organic": 0.10, "referral": 0.26, "social": -0.28}[source]

def plan_delta(plan: str) -> float:
    return {"free": -0.10, "trial": 0.02, "basic": 0.20, "pro": 0.34}[plan]

def aha_delta(reached_aha: bool) -> float:
    return 0.22 if reached_aha else -0.14

def source_aha_probability(source: str) -> float:
    return {"ads": 0.20, "organic": 0.32, "referral": 0.42, "social": 0.16}[source]

def trial_probability(source: str, reached_aha: bool) -> float:
    base = {"ads": 0.17, "organic": 0.27, "referral": 0.33, "social": 0.13}[source]
    return min(0.72, base * (1.55 if reached_aha else 0.70))

def paid_probability(source: str, reached_aha: bool) -> float:
    base = {"ads": 0.30, "organic": 0.41, "referral": 0.48, "social": 0.24}[source]
    return min(0.80, base * (1.30 if reached_aha else 0.70))

def random_datetime_between(start_dt: datetime, end_dt: datetime):
    if end_dt <= start_dt:
        return None
    seconds_range = int((end_dt - start_dt).total_seconds())
    return start_dt + timedelta(seconds=random.randint(0, max(1, seconds_range)))

def random_datetime_in_relative_week(signup_time: datetime, week_index: int):
    """Generate a timestamp within a calendar cohort week.

    Cohort week 0 is the calendar week containing signup_time.
    Cohort week 1 is the next calendar week, and so on.
    This aligns generation with SQL DATE_TRUNC('week') cohort logic.
    """
    cohort_start = get_week_start(signup_time)
    week_start_time = cohort_start + timedelta(days=7 * week_index)
    week_end_time = cohort_start + timedelta(days=7 * (week_index + 1)) - timedelta(seconds=1)
    start = max(signup_time, week_start_time)
    end = min(END_DATE, week_end_time)
    return random_datetime_between(start, end)

def choose_activity_event(source: str, reached_aha: bool, current_plan: str, early_week: bool) -> str:
    if early_week and reached_aha:
        probs = [0.22, 0.22, 0.32, 0.18, 0.06]
    elif source in ["ads", "social"] and not reached_aha:
        probs = [0.55, 0.32, 0.095, 0.03, 0.005]
    elif current_plan == "pro":
        probs = [0.24, 0.25, 0.25, 0.17, 0.09]
    elif current_plan == "basic":
        probs = [0.28, 0.28, 0.24, 0.14, 0.06]
    elif reached_aha:
        probs = [0.31, 0.27, 0.25, 0.13, 0.04]
    else:
        probs = [0.45, 0.35, 0.15, 0.04, 0.01]
    return str(np.random.choice(ACTIVITY_EVENTS, p=probs))

def expected_events_per_active_week(current_plan: str, reached_aha: bool, week_index: int) -> float:
    base = {"free": 1.35, "trial": 1.95, "basic": 2.80, "pro": 3.80}[current_plan]
    if reached_aha:
        base *= 1.25
    if week_index == 0:
        base *= 1.22
    # Keep long-term retained users active, but do not explode row counts.
    base *= max(0.70, 1 - week_index * 0.018)
    return base

def clean_for_validation(df: pd.DataFrame) -> pd.DataFrame:
    c = df.copy()
    c["event_name_clean"] = c["event_name"].replace({"log_in": "login", "sign_up": "signup"})
    c["country_clean"] = c["country"].replace({"USA": "US", "Indnesia": "Indonesia"})
    c["device_clean"] = c["device"].replace({"Mobile": "mobile"})
    c["plan_type_clean"] = c["plan_type"].replace({"Basic": "basic"})
    return c

# ==================================================
# GENERATION
# ==================================================
def generate_dataset() -> pd.DataFrame:
    events = []
    event_counter = 1

    def add_event(user_id, event_time, event_name, source, device, country, plan_type, subscription_status, revenue=0):
        nonlocal event_counter
        if event_time is None or event_time > END_DATE:
            return
        events.append({
            "event_id": f"E{event_counter:06d}",
            "user_id": user_id,
            "event_time": event_time,
            "event_name": event_name,
            "source": source,
            "device": device,
            "country": country,
            "plan_type": plan_type,
            "subscription_status": subscription_status,
            "revenue": revenue,
        })
        event_counter += 1

    for user_number in range(1, NUM_USERS + 1):
        user_id = f"U{user_number:05d}"
        source = str(np.random.choice(SOURCES, p=SOURCE_PROBS))
        device = str(np.random.choice(DEVICES, p=DEVICE_PROBS))
        country = str(np.random.choice(COUNTRIES, p=COUNTRY_PROBS))

        signup_offset_days = int(np.random.randint(0, (END_DATE.date() - START_DATE.date()).days + 1))
        signup_time = (
            START_DATE
            + timedelta(days=signup_offset_days)
            + timedelta(hours=int(np.random.randint(0, 23)))
            + timedelta(minutes=int(np.random.randint(0, 60)))
            + timedelta(seconds=int(np.random.randint(0, 60)))
        )
        cohort_start_date = get_week_start(signup_time)
        max_observable_week = max(0, int((get_week_start(END_DATE) - cohort_start_date).days // 7))

        reached_aha = np.random.rand() < source_aha_probability(source)

        has_trial = np.random.rand() < trial_probability(source, reached_aha)
        is_paid = False
        final_plan = "free"

        if has_trial and np.random.rand() < paid_probability(source, reached_aha):
            is_paid = True
            final_plan = str(np.random.choice(["basic", "pro"], p=[0.72, 0.28]))
        elif has_trial:
            final_plan = "trial"
        else:
            direct_paid_prob = {"ads": 0.012, "organic": 0.035, "referral": 0.052, "social": 0.010}[source]
            if reached_aha and np.random.rand() < direct_paid_prob:
                is_paid = True
                final_plan = str(np.random.choice(["basic", "pro"], p=[0.75, 0.25]))
            else:
                final_plan = "free"

        # Cohort-level / user-level noise to avoid perfect curves.
        user_noise = np.random.normal(0, 0.11)

        active_weeks = []
        for week_index in range(max_observable_week + 1):
            if week_index == 0:
                active_weeks.append(0)
                continue

            # Logistic adjustment keeps segment effects realistic without exploding Week 1.
            adjusted_logit = (
                logit(base_retention(week_index))
                + source_delta(source)
                + plan_delta(final_plan)
                + aha_delta(reached_aha)
                + user_noise
            )

            p_active = sigmoid(adjusted_logit)

            # Shape controls to avoid Week 1 too high and Week 8 too low.
            if week_index == 1:
                p_active = min(p_active, 0.78)
            elif week_index >= 4:
                # retained mature users decline slower; slightly lift long-term floor
                p_active = max(p_active, 0.035 if week_index < 8 else 0.055)

            if np.random.rand() < p_active:
                active_weeks.append(week_index)

        # Keep some natural gaps. A later active week does not force all previous weeks to be active.
        active_set = set(active_weeks)
        active_weeks = sorted(active_set)

        last_active_week = max(active_weeks) if active_weeks else 0

        # Milestones
        trial_week = None
        subscription_week = None
        cancellation_week = None

        if has_trial and max_observable_week >= 1:
            possible_trial_weeks = [w for w in [1, 2, 3] if w <= max_observable_week]
            if possible_trial_weeks:
                trial_week = int(np.random.choice(possible_trial_weeks, p=np.array([0.55, 0.30, 0.15])[:len(possible_trial_weeks)] / np.array([0.55, 0.30, 0.15])[:len(possible_trial_weeks)].sum()))

        if is_paid:
            if trial_week is not None:
                subscription_week = min(
                    max_observable_week,
                    trial_week + int(np.random.choice([0, 1, 2], p=[0.25, 0.55, 0.20]))
                )
            else:
                subscription_week = min(
                    max_observable_week,
                    int(np.random.choice([1, 2, 3], p=[0.45, 0.35, 0.20]))
                )

        # Milestone events are administrative; they do not automatically count as active usage.
        # However, paid users often show some post-subscription product usage.
        if subscription_week is not None and subscription_week + 1 <= max_observable_week and np.random.rand() < 0.30:
            active_set.add(subscription_week + 1)
        active_weeks = sorted(active_set)
        last_active_week = max(active_weeks) if active_weeks else 0

        churn_observable = last_active_week + 3 <= max_observable_week
        if is_paid and churn_observable:
            cancel_probability = {"basic": 0.24, "pro": 0.16}[final_plan]
            if np.random.rand() < cancel_probability:
                cancellation_week = min(
                    max_observable_week,
                    last_active_week + int(np.random.choice([1, 2, 3], p=[0.35, 0.45, 0.20]))
                )

        def state_at_week(week_index):
            if cancellation_week is not None and week_index >= cancellation_week:
                return final_plan, "cancelled"
            if subscription_week is not None and week_index >= subscription_week:
                return final_plan, "active"
            if trial_week is not None and week_index >= trial_week:
                return "trial", "trial"
            return "free", "free"

        # Signup event first
        add_event(user_id, signup_time, "signup", source, device, country, "free", "free", 0)

        early_core_count = 0

        # Generate milestone + activity events.
        for week_index in range(max_observable_week + 1):
            if trial_week == week_index:
                et = random_datetime_in_relative_week(signup_time, week_index)
                if et is not None and et > signup_time:
                    add_event(user_id, et, "trial_started", source, device, country, "trial", "trial", 0)

            if subscription_week == week_index:
                et = random_datetime_in_relative_week(signup_time, week_index)
                if et is not None and et > signup_time:
                    rev = 30 if final_plan == "basic" else 100
                    if final_plan == "basic" and np.random.rand() < 0.12:
                        rev = int(np.random.randint(25, 31))
                    if final_plan == "pro" and np.random.rand() < 0.12:
                        rev = int(np.random.randint(90, 101))
                    add_event(user_id, et, "subscription_started", source, device, country, final_plan, "active", rev)

            if week_index in active_weeks:
                plan_now, status_now = state_at_week(week_index)
                lam = expected_events_per_active_week(plan_now, reached_aha, week_index)
                n_events = int(np.random.poisson(lam))
                if week_index == 0:
                    n_events = max(1, n_events)
                n_events = min(max(0, n_events), 10)

                for _ in range(n_events):
                    et = random_datetime_in_relative_week(signup_time, week_index)
                    if et is None or et <= signup_time:
                        continue

                    event_name = choose_activity_event(source, reached_aha, plan_now, early_week=(week_index == 0))
                    if reached_aha and week_index == 0 and early_core_count < 2:
                        event_name = str(np.random.choice(CORE_EVENTS, p=[0.55, 0.35, 0.10]))

                    if event_name in CORE_EVENTS and week_index == 0 and et <= signup_time + timedelta(days=7):
                        early_core_count += 1

                    add_event(user_id, et, event_name, source, device, country, plan_now, status_now, 0)

        # Guarantee aha users have the events needed to infer aha moment from raw data.
        while reached_aha and early_core_count < 2 and signup_time + timedelta(days=7) <= END_DATE:
            et = signup_time + timedelta(
                days=int(np.random.randint(0, 7)),
                hours=int(np.random.randint(1, 23)),
                minutes=int(np.random.randint(0, 60)),
                seconds=int(np.random.randint(0, 60)),
            )
            if et > END_DATE:
                break
            plan_now, status_now = state_at_week(0)
            ev = str(np.random.choice(CORE_EVENTS, p=[0.55, 0.35, 0.10]))
            add_event(user_id, et, ev, source, device, country, plan_now, status_now, 0)
            early_core_count += 1

        if cancellation_week is not None:
            et = random_datetime_in_relative_week(signup_time, cancellation_week)
            if et is not None:
                add_event(user_id, et, "subscription_cancelled", source, device, country, final_plan, "cancelled", 0)

    df = pd.DataFrame(events)
    df = df.sort_values(["user_id", "event_time", "event_id"]).reset_index(drop=True)
    return df

# ==================================================
# DIRTY DATA
# ==================================================
def add_dirty_data(df: pd.DataFrame) -> pd.DataFrame:
    dirty = df.copy()

    # Typos / inconsistencies
    login_rows = dirty[dirty["event_name"] == "login"]
    if len(login_rows) > 0:
        dirty.loc[login_rows.sample(frac=0.01, random_state=42).index, "event_name"] = "log_in"

    signup_rows = dirty[dirty["event_name"] == "signup"]
    if len(signup_rows) > 0:
        dirty.loc[signup_rows.sample(frac=0.005, random_state=43).index, "event_name"] = "sign_up"

    dirty.loc[dirty.sample(frac=0.010, random_state=44).index, "country"] = "USA"
    dirty.loc[dirty.sample(frac=0.005, random_state=45).index, "country"] = "Indnesia"
    dirty.loc[dirty.sample(frac=0.020, random_state=46).index, "device"] = "Mobile"

    basic_rows = dirty[dirty["plan_type"] == "basic"]
    if len(basic_rows) > 0:
        dirty.loc[basic_rows.sample(frac=0.01, random_state=47).index, "plan_type"] = "Basic"

    # Missing categorical fields
    dirty.loc[dirty.sample(n=min(250, len(dirty)), random_state=48).index, "country"] = None
    dirty.loc[dirty.sample(n=min(350, len(dirty)), random_state=49).index, "device"] = None
    dirty.loc[dirty.sample(n=min(150, len(dirty)), random_state=50).index, "source"] = None

    # Multi-source users
    user_ids = dirty["user_id"].unique()
    selected_users = np.random.choice(user_ids, size=min(80, len(user_ids)), replace=False)

    for user_id in selected_users:
        user_rows = dirty[dirty["user_id"] == user_id]
        if len(user_rows) <= 1:
            continue
        change_idx = user_rows.sample(frac=0.30, random_state=int(user_id[1:]) % 9999).index
        for idx in change_idx:
            current = dirty.loc[idx, "source"]
            if pd.isna(current) or current not in SOURCES:
                dirty.loc[idx, "source"] = str(np.random.choice(SOURCES))
            else:
                dirty.loc[idx, "source"] = str(np.random.choice([s for s in SOURCES if s != current]))

    # Duplicate / near duplicate tracking rows with unique event_id
    duplicate_count = min(500, len(dirty))
    dup = dirty.sample(n=duplicate_count, random_state=51).copy()

    max_event_num = dirty["event_id"].str.replace("E", "", regex=False).astype(int).max()
    dup["event_id"] = [f"E{i:06d}" for i in range(max_event_num + 1, max_event_num + duplicate_count + 1)]

    # Some duplicates are exact timestamp, some are near-duplicates.
    shift_seconds = np.random.choice([0, 1, 2, 3, 5, 10, 15, 20, 25], size=duplicate_count)
    dup["event_time"] = dup["event_time"] + pd.to_timedelta(shift_seconds, unit="s")

    dirty = pd.concat([dirty, dup], ignore_index=True)
    dirty = dirty.sample(frac=1, random_state=52).reset_index(drop=True)
    return dirty

# ==================================================
# VALIDATION SUMMARY (PRINT ONLY)
# ==================================================
def print_validation_summary(df: pd.DataFrame):
    clean = clean_for_validation(df)

    print("\n==============================")
    print("RAW DATASET SUMMARY")
    print("==============================")
    print("Total rows:", len(df))
    print("Total unique users:", df["user_id"].nunique())
    print("Average events per user:", round(len(df) / df["user_id"].nunique(), 2))
    print("Date range:", df["event_time"].min(), "to", df["event_time"].max())

    print("\nEvent count by event_name:")
    print(df["event_name"].value_counts(dropna=False))

    print("\nUser count by source:")
    print(df.groupby("source", dropna=False)["user_id"].nunique().sort_values(ascending=False))

    print("\nCount by plan_type:")
    print(df["plan_type"].value_counts(dropna=False))

    print("\nCount by subscription_status:")
    print(df["subscription_status"].value_counts(dropna=False))

    duplicate_count = df.duplicated(subset=["user_id", "event_name", "event_time"], keep=False).sum()
    print("\nBasic duplicate count by user_id + event_name + event_time:", int(duplicate_count))
    print("event_id duplicate count:", int(df["event_id"].duplicated().sum()))

    print("\nMissing values per column:")
    print(df.isna().sum())

    forbidden = sorted([c for c in df.columns if c in FORBIDDEN_RAW_COLUMNS])
    print("\nForbidden derived columns present in raw dataset:", forbidden)

    # Signup validation
    signup_events = clean[clean["event_name_clean"] == "signup"].copy()
    signup_time = (
        signup_events.sort_values(["user_id", "event_time", "event_id"])
        .groupby("user_id")["event_time"]
        .min()
        .rename("signup_time")
    )
    print("\nSignup users after internal repair:", signup_time.index.nunique())
    print("Signup users equal total unique users:", signup_time.index.nunique() == clean["user_id"].nunique())

    first_events = (
        clean.sort_values(["user_id", "event_time", "event_id"])
        .groupby("user_id")
        .first()
        .reset_index()
    )
    print(
        "Share of users whose first event is signup after internal repair:",
        round((first_events["event_name_clean"] == "signup").mean(), 4),
    )

    merged = clean.merge(signup_time, on="user_id", how="left")
    print("Events before signup:", int((merged["event_time"] < merged["signup_time"]).sum()))

    # Internal retention fields for validation only
    activity = clean[clean["event_name_clean"].isin(ACTIVITY_EVENTS)].copy()
    activity = activity.merge(signup_time, on="user_id", how="left")
    activity["cohort_start_date"] = activity["signup_time"].apply(get_week_start)
    activity["event_week"] = activity["event_time"].apply(get_week_start)
    activity["cohort_index"] = ((activity["event_week"] - activity["cohort_start_date"]).dt.days // 7).astype(int)

    users = pd.DataFrame({"user_id": clean["user_id"].unique()}).merge(signup_time, on="user_id", how="left")
    users["cohort_start_date"] = users["signup_time"].apply(get_week_start)
    users["max_observable_week"] = ((get_week_start(END_DATE) - users["cohort_start_date"]).dt.days // 7).astype(int)

    first_touch = (
        clean.sort_values(["user_id", "event_time", "event_id"])
        .groupby("user_id")["source"]
        .first()
        .fillna("Unknown")
        .rename("first_touch_source")
    )
    users = users.merge(first_touch, on="user_id", how="left")

    latest_plan = (
        clean.sort_values(["user_id", "event_time", "event_id"])
        .groupby("user_id")["plan_type_clean"]
        .last()
        .rename("latest_plan_type")
    )
    users = users.merge(latest_plan, on="user_id", how="left")

    retained = (
        activity[activity["cohort_index"] >= 0]
        .drop_duplicates(["user_id", "cohort_index"])
        .groupby("cohort_index")["user_id"]
        .nunique()
        .rename("retained_users")
        .reset_index()
    )

    cohort_rows = []
    for w in range(0, 13):
        cohort_size = users[users["max_observable_week"] >= w]["user_id"].nunique()
        cohort_rows.append({"cohort_index": w, "cohort_size": cohort_size})
    cohort_sizes = pd.DataFrame(cohort_rows)

    ret = cohort_sizes.merge(retained, on="cohort_index", how="left")
    ret["retained_users"] = ret["retained_users"].fillna(0).astype(int)
    ret.loc[ret["cohort_index"] == 0, "retained_users"] = ret.loc[ret["cohort_index"] == 0, "cohort_size"]
    ret["retention_rate"] = (ret["retained_users"] / ret["cohort_size"]).round(4)

    print("\nApproximate overall retention by cohort_index:")
    print(ret.head(13))

    print("\nRetention by source summary:")
    source_rows = []
    for source in sorted(users["first_touch_source"].dropna().unique()):
        subset = users[users["first_touch_source"] == source]
        row = {"source": source}
        for w in [1, 2, 4, 8]:
            eligible = subset[subset["max_observable_week"] >= w]
            active_users = set(activity[activity["cohort_index"] == w]["user_id"].unique())
            row[f"week_{w}_retention"] = np.nan if len(eligible) == 0 else round(eligible["user_id"].isin(active_users).mean(), 4)
        source_rows.append(row)
    print(pd.DataFrame(source_rows))

    print("\nRetention by latest plan_type summary:")
    plan_rows = []
    for plan in sorted(users["latest_plan_type"].dropna().unique()):
        subset = users[users["latest_plan_type"] == plan]
        row = {"plan_type": plan}
        for w in [1, 4, 8]:
            eligible = subset[subset["max_observable_week"] >= w]
            active_users = set(activity[activity["cohort_index"] == w]["user_id"].unique())
            row[f"week_{w}_retention"] = np.nan if len(eligible) == 0 else round(eligible["user_id"].isin(active_users).mean(), 4)
        plan_rows.append(row)
    print(pd.DataFrame(plan_rows))

    # Aha moment validation from raw events
    clean_signup = clean.merge(signup_time, on="user_id", how="left")
    first7 = clean_signup[
        (clean_signup["event_time"] >= clean_signup["signup_time"])
        & (clean_signup["event_time"] <= clean_signup["signup_time"] + pd.Timedelta(days=7))
        & (clean_signup["event_name_clean"].isin(CORE_EVENTS))
    ]
    aha = first7.groupby("user_id").size().reset_index(name="core_event_count")
    aha["reached_aha_moment"] = aha["core_event_count"] >= 2
    users = users.merge(aha[["user_id", "reached_aha_moment"]], on="user_id", how="left")
    users["reached_aha_moment"] = users["reached_aha_moment"].fillna(False)

    print("\nAha moment validation:")
    print(users["reached_aha_moment"].value_counts())

    for status in [False, True]:
        subset = users[(users["reached_aha_moment"] == status) & (users["max_observable_week"] >= 4)]
        active_w4 = set(activity[activity["cohort_index"] == 4]["user_id"].unique())
        rate = np.nan if len(subset) == 0 else subset["user_id"].isin(active_w4).mean()
        print(f"Week 4 retention for aha_moment={status}: {round(rate, 4) if not pd.isna(rate) else np.nan}")

    # Churn validation
    last_activity = activity.groupby("user_id")["cohort_index"].max().rename("last_activity_cohort_index")
    users = users.merge(last_activity, on="user_id", how="left")
    users["last_activity_cohort_index"] = users["last_activity_cohort_index"].fillna(0).astype(int)
    users["estimated_churned"] = users["last_activity_cohort_index"] + 3 <= users["max_observable_week"]
    users["estimated_churn_week"] = np.where(users["estimated_churned"], users["last_activity_cohort_index"], np.nan)

    print("\nEstimated churn summary:")
    print("Estimated churned users:", int(users["estimated_churned"].sum()))
    print("Estimated churn rate:", round(users["estimated_churned"].mean(), 4))

    print("\nEstimated churned users by source:")
    print(users.groupby("first_touch_source")["estimated_churned"].mean().round(4))

    print("\nEstimated churned users by latest plan_type:")
    print(users.groupby("latest_plan_type")["estimated_churned"].mean().round(4))

    print("\nEstimated churn_week distribution:")
    print(users["estimated_churn_week"].value_counts(dropna=False).sort_index().head(15))

# ==================================================
# MAIN
# ==================================================
def main():
    df = generate_dataset()
    df = add_dirty_data(df)

    # Raw dataset must only include raw production-like fields.
    df = df[RAW_COLUMNS].copy()

    if df["event_id"].duplicated().any():
        raise ValueError("event_id duplicate found. This violates the raw data rule.")

    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\nDataset exported successfully: {OUTPUT_FILE}")
    print_validation_summary(df)

if __name__ == "__main__":
    main()
