# Synthetic SaaS Retention Dataset Prompt

## Purpose

This prompt is designed to generate a realistic synthetic SaaS event dataset for retention and cohort analysis.

The dataset can be used for analytics portfolio projects, SQL practice, dashboarding, and business case analysis.

The main goal is to create event-level data that behaves like a real SaaS product system, so learners can practice analyzing user retention, churn, acquisition quality, feature usage, and business impact.

---

<br>

## Who This Is For

This prompt is best for learners who already understand basic analytics concepts such as:

- Event-level data
- Cohort analysis
- Retention rate
- Churn analysis
- SQL aggregation
- User journey analysis
- Basic SaaS business logic

If you are completely new to data analytics, it is better to start with a simpler public dataset first before building a custom synthetic dataset.

---

<br>

## What This Prompt Generates

The prompt generates a raw SaaS event dataset for a retention and cohort analysis case study.

The dataset is designed to answer questions such as:

- How does user retention change by weekly signup cohort?
- Which cohort has the weakest retention?
- Which acquisition source brings the most retained users?
- Do paid users retain better than free users?
- Does early feature usage improve retention?
- Which user segment should be prioritized for retention improvement?

The dataset should be exported as:

```text
saas_retention_events_raw.csv
```

This should be the only output file.

No validation table should be exported.

---

<br>

## Expected Raw Dataset Schema

The raw dataset should look like production event data, not a pre-aggregated analytics table.

| Column                | Description                                  |
| --------------------- | -------------------------------------------- |
| `event_id`            | Unique identifier for each event             |
| `user_id`             | Unique identifier for each user              |
| `event_time`          | Timestamp of the event                       |
| `event_name`          | Type of user event                           |
| `source`              | User acquisition source                      |
| `device`              | User device                                  |
| `country`             | User country                                 |
| `plan_type`           | User plan at the time of the event           |
| `subscription_status` | Subscription status at the time of the event |
| `revenue`             | Revenue generated from subscription events   |

The raw dataset should not include analytical or derived fields such as:

- `signup_date`
- `signup_week`
- `cohort_start_date`
- `event_week`
- `cohort_index`
- `max_observable_week`
- `churned`
- `churn_status`
- `churn_week`
- `is_core_feature`
- `reached_aha_moment`

These fields should be calculated later during SQL analysis.

---
<br>

## What Makes This Dataset Realistic

This dataset is designed to include realistic SaaS event behavior, not just random rows.

Key realism layers include:

- Sequential user behavior after signup
- Weekly user activity patterns
- Retention decay over time
- Acquisition source differences
- Plan changes over time
- Event-level plan_type and subscription_status
- Early feature usage behavior
- Aha moment logic
- Churn behavior with observation-window awareness
- Messy data such as typos, null values, duplicates, and inconsistent labels

The dataset should not be too perfect.

For example:

- Not all ads users should be bad
- Not all referral users should be good
- Some free users should still retain
- Some paid users should still churn
- Some users without aha moment should still stay active
- Some users with aha moment should still churn

The goal is to make the dataset realistic enough for meaningful analysis.

Important Analytical Rules
1. Raw Data Should Stay Raw

The raw dataset should only contain event-level facts.

Fields such as cohort index, churn status, and aha moment should be calculated in SQL, not included in the raw dataset.

This makes the analysis more realistic and demonstrates actual analytical skill.

2. Plan Type Must Be Event-Level

plan_type must represent the user's plan at the time of each event, not the user's final plan.

Example:

Event	Correct plan_type
signup	free
login before trial	free
trial_started	trial
subscription_started	basic/pro
activity after subscription	basic/pro

Do not assign a final paid plan to all historical events.

That would make paid vs free retention analysis biased.

3. Subscription Status Must Be Event-Level

subscription_status should also represent the user’s status at the time of each event.

Example:

Event	Correct subscription_status
signup	free
trial_started	trial
subscription_started	active
subscription_cancelled	cancelled
4. Churn Must Respect Observation Window

A user should only be considered churned if there is enough time to observe inactivity.

For example, if a user signs up close to the end of the dataset period, they should not be automatically counted as churned just because they do not have future activity.

The churn logic should respect the observation window.

Later in SQL, churn should be calculated using logic such as:

last_activity_cohort_index + 3 <= max_observable_week

This prevents late signup cohorts from being incorrectly counted as churned.

5. Event ID Must Remain Unique

Duplicate or near-duplicate tracking rows should receive a new event_id.

This simulates double-tracking issues without breaking event ID uniqueness.

A duplicate tracking row may have:

Same user_id
Same or similar event_name
Same or very close event_time
Same source/device/country
New unique event_id
Dataset Size

Target size:

Around 100,000 event rows
Unique users can adjust naturally
Approximate user count can be around 8,000–15,000 users

The dataset does not need to be exactly 100,000 rows.

Realistic behavior is more important than hitting the exact row count.

Event Names

The dataset should include these events:

signup
login
dashboard_view
feature_used
report_created
invite_team_member
trial_started
subscription_started
subscription_cancelled

Activity events for retention analysis:

login
dashboard_view
feature_used
report_created
invite_team_member

Non-activity events:

signup
trial_started
subscription_started
subscription_cancelled

This distinction is important because retention should measure whether users return to use the product, not just whether they have administrative subscription events.

Retention Logic

The dataset should show natural retention decay over time.

Expected overall pattern:

Week	Approximate Retention
Week 0	100%
Week 1	~60%
Week 2	~42%
Week 3	~30%
Week 4	~23%
Week 5	~18%
Week 6	~14%
Week 7	~11%
Week 8	~9%

The main bottleneck should happen between Week 1 and Week 3.

This represents users who tried the product early but failed to build a usage habit or reach the product’s core value.

Aha Moment Logic

The dataset should include behavior that allows the analyst to calculate aha moment later in SQL.

Aha moment definition:

A user reaches aha moment if they perform at least 2 core feature events within the first 7 days after signup.

Core feature events:

feature_used
report_created
invite_team_member

Users who reach aha moment should generally have higher retention after Week 2.

However, this should not be deterministic.

Some users who reach aha moment may still churn, and some users who do not reach aha moment may still remain active.

Source Behavior Logic

Acquisition source should affect retention, but not determine it completely.

Suggested source distribution:

Source	Approximate Share
ads	40%
organic	30%
referral	20%
social	10%

Expected behavior:

Referral
Highest retention
More likely to use core features
More likely to reach aha moment
More likely to convert to paid plan
Organic
Strong retention
Stable behavior
Moderate to good paid conversion
Healthy core feature usage
Ads
Highest volume
Lower retention
More users churn early
Lower aha moment rate
Lower paid conversion than organic/referral
Social
Lower volume
Weak retention
Many users active only in early weeks
Lower core feature usage
Plan and Subscription Logic

Plan type should affect retention.

Expected behavior:

Free Users
Lowest retention
Many churn after Week 1 or Week 2
Lower core feature usage
Trial Users
Medium retention
Some convert to basic/pro
Trial should happen after signup and some activity
Basic Users
Higher retention
Revenue around $30 on subscription_started
Pro Users
Highest retention
Revenue around $100 on subscription_started
More likely to use core features and invite team members

Plan and subscription status should change logically over time:

free → trial → basic/pro

or in some cases:

free → basic/pro
Revenue Logic

For the first version, revenue should be simple.

Revenue should only appear on:

subscription_started

Rules:

Basic plan revenue: around $30
Pro plan revenue: around $100
All non-subscription events: revenue = 0

This dataset does not need full recurring revenue logic yet.

So revenue analysis should be treated as subscription-start revenue, not full recurring revenue.

Dirty Data Logic

The dataset should include realistic data quality issues, but not so much that the analysis becomes unusable.

Include:

Inconsistent or typo values

Examples:

log_in → login
sign_up → signup
USA → US
Indnesia → Indonesia
Mobile → mobile
Basic → basic
Missing values

Some rows can have missing values in:

country
device
source

But missing values should not be too many.

Duplicate tracking events

Add around 300–700 duplicate or near-duplicate rows.

Duplicates should have a new unique event_id.

Multi-source users

Add around 50–100 users with more than one source due to tracking or attribution issues.

Later in SQL, first-touch source can be calculated using the first event per user.

Dirty Data Guardrails

Dirty data should not break the core retention logic.

Rules:

Do not create missing user_id
Do not create missing event_time
Every user must have a recoverable signup event
Signup should remain recoverable even if written as sign_up
Dirty data should mostly affect categorical fields and duplicate event rows
Expected SQL Analysis

The raw dataset should support the following SQL analysis:

1. Data Cleaning
Fix log_in → login
Fix sign_up → signup
Fix USA → US
Fix Indnesia → Indonesia
Fix Mobile → mobile
Fix Basic → basic
Handle null source/country/device
Remove duplicate tracking events
2. Cohort Fields

Calculate:

signup_date
signup_week
cohort_start_date
event_week
cohort_index
max_observable_week
3. Retention Analysis

Calculate:

Weekly retention
Cohort retention heatmap
Retention curve
Retention by source
Retention by plan type
Retention by device/country
4. Churn Analysis

Calculate:

churned
churn_status
churn_week
Churn by source
Churn by plan type
5. Aha Moment Analysis

Calculate:

Core feature usage in first 7 days
Users who reached aha moment
Retention of aha moment vs non-aha users
6. Business Recommendations

Use the analysis to answer:

Which users churn fastest?
Which source brings better retained users?
Which segment should be prioritized?
Does early feature usage improve retention?
What action should the product or growth team take?
Quality Check Summary

After generating the dataset, check:

Total rows are close to 100,000
Total unique users are reasonable
Average events per user is realistic
Date range is correct
Each user has one recoverable signup event
Signup is the first event for each user
There are no events before signup
event_id is unique
plan_type reflects the user’s state at the time of event
Retention declines naturally over time
Week 1–3 shows a clear retention drop
Source effects are visible but not deterministic
Aha moment users retain better than non-aha users
Dirty data exists but does not break core analysis
No derived analytics fields are included in the raw dataset
Limitations

This is a synthetic dataset, not real company data.

It is useful for:

Learning
Portfolio building
SQL practice
Dashboarding
Analytics workflow simulation

But it should not be treated as evidence of real SaaS behavior.

The assumptions inside the dataset should be reviewed and adjusted depending on the business case.

How to Customize This Prompt

You can modify:

Business context
Event names
Date range
Number of users
Total event rows
Retention pattern
Source distribution
Dirty data level
Monetization logic
Churn definition
Aha moment definition
Industry/domain

For example, this structure can be adapted for:

E-commerce retention
Fintech app usage
Marketplace repeat behavior
Subscription app churn
HR platform engagement
Learning platform retention
Key Reminder

Public datasets are useful, but they may not always match the case study you want to build.

A custom synthetic dataset gives you more control over the business problem, data structure, and analytical story.

However, customization also requires stronger assumptions.

A realistic dataset is not just about generating rows.

It is about designing behavior that makes sense.
