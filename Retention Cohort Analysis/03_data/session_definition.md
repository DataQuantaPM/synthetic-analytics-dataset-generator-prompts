# Synthetic SaaS User Behavior Simulator v2.0

# Session Definition

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Session Philosophy
3. Session Lifecycle
4. Session Generation Rules
5. Session Schema
6. Session States
7. Session Metrics
8. Session Business Rules
9. Session Validation Rules
10. Session Quality Rules
11. Session Lineage
12. References

---

# 1. Purpose

This document defines how user sessions are generated throughout the simulation.

A session represents a continuous period of user interaction with the SaaS application.

Sessions serve as the bridge between users and behavioral events and are the foundation for engagement, retention, and usage analytics.

---

# 2. Session Philosophy

The simulator follows a session-based behavioral model similar to modern analytics platforms such as:

- Google Analytics 4
- Mixpanel
- Amplitude
- PostHog

Each session groups a sequence of related user interactions into a single unit of activity.

Every event (except Signup) belongs to one session.

---

# 3. Session Lifecycle

A session progresses through the following lifecycle.

```text
Session Created
        │
        ▼
Login Event
        │
        ▼
User Activity
        │
        ▼
Additional Events
        │
        ▼
Session Ends
```

A session ends when:

- the user becomes inactive,
- the maximum session duration is reached,
- or the day ends (depending on configuration).

---

# 4. Session Generation Rules

Sessions are generated automatically by the Session Engine.

Generation process:

1. User becomes active.
2. A new session_id is created.
3. Login event is generated.
4. Product events are generated.
5. Session duration is calculated.
6. Session closes.

---

## Session Frequency

The number of sessions depends on:

- engagement_score
- lifecycle_state
- persona
- subscription_plan
- active scenario modifiers

Highly engaged users naturally generate more sessions.

---

## Session Timing

Each session has:

- session_start
- session_end
- duration_minutes

All events must occur between these timestamps.

---

# 5. Session Schema

| Column | Type | Nullable | Description | Example |
|---------|------|----------|-------------|---------|
| session_id | TEXT | No | Unique session identifier | S000001 |
| user_id | TEXT | No | Session owner | U000001 |
| session_start | DATETIME | No | Session start | 2026-01-05 09:15 |
| session_end | DATETIME | No | Session end | 2026-01-05 09:48 |
| duration_minutes | INTEGER | No | Session duration | 33 |
| total_events | INTEGER | No | Number of events inside session | 7 |
| lifecycle_state | TEXT | No | User state during session | Active |

---

## Primary Key

session_id

---

## Foreign Key

user_id → users.csv

---

# 6. Session States

A session itself can exist in one of the following states.

| State | Description |
|--------|-------------|
| Created | Session initialized |
| Active | User is interacting |
| Idle | Temporary inactivity |
| Closed | Session finished |

Only Closed sessions are exported.

---

# 7. Session Metrics

The simulator calculates several session-level metrics.

| Metric | Description |
|---------|-------------|
| Session Count | Number of sessions |
| Avg Session Duration | Average duration |
| Median Session Duration | Median duration |
| Events per Session | Average event count |
| Sessions per User | User engagement |
| Active Days | Number of active days |

These metrics are commonly used in Product Analytics dashboards.

---

# 8. Session Business Rules

The following business rules always apply.

### Rule 1

Every session belongs to exactly one user.

---

### Rule 2

Every session has exactly one Login event.

---

### Rule 3

Every event (except Signup) belongs to exactly one session.

---

### Rule 4

session_start must occur before session_end.

---

### Rule 5

Events must occur within the session window.

```text
session_start

≤

event_timestamp

≤

session_end
```

---

### Rule 6

Session duration must be greater than zero.

---

### Rule 7

A user cannot have overlapping sessions.

---

### Rule 8

Session IDs are immutable.

---

# 9. Session Validation Rules

The Validation Engine checks:

✓ unique session_id

✓ valid user_id

✓ valid timestamps

✓ no overlapping sessions

✓ positive duration

✓ all events linked to existing session

✓ chronological ordering

---

# 10. Session Quality Rules

Dirty data injection may intentionally introduce:

- duplicated sessions
- missing session_id
- orphan events
- incorrect duration
- timestamp drift
- invalid ordering

These anomalies are injected only after the clean simulation has completed.

---

# 11. Session Lineage

```text
UserGenerator
        │
        ▼
Lifecycle Engine
        │
        ▼
Session Engine
        │
        ▼
sessions.csv
        │
        ▼
Event Engine
        │
        ▼
events.csv
        │
        ▼
Retention
Churn
Aha Moment
Session Analytics
```

The Session Engine is responsible only for generating sessions.

Behavioral events are generated afterward by the Event Engine.

---

# References

- architecture/state_machine.md
- architecture/execution_pipeline.md
- data_dictionary.md
- event_dictionary.md
- business_rules.md
