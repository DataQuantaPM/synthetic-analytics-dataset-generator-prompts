# Synthetic SaaS User Behavior Simulator v2.0

# Retention Generator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Generator Position
4. Inputs
5. Outputs
6. Dataset Schema
7. Retention Generation Model
8. Generation Workflow
9. Retention Logic
10. Retention Window
11. Activity Pattern Generation
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Retention Generator determines whether users continue returning to the product after their initial activation.

Unlike the Session Generator, which creates individual sessions, the Retention Generator models long-term engagement behavior across the simulation period.

The generated retention dataset supports cohort analysis, retention reporting, stickiness metrics, and future churn simulation.

---

# 2. Responsibilities

The Retention Generator is responsible for:

- generating retention outcomes
- assigning return activity
- determining active periods
- calculating retention windows
- publishing the Retention dataset

The Retention Generator is **not** responsible for:

- generating sessions
- generating events
- calculating revenue
- predicting churn

---

# 3. Generator Position

```text
Users

↓

Sessions

↓

Lifecycle

↓

Events

↓

Subscriptions

↓

Revenue

↓

Retention Generator

↓

Retention Dataset

↓

Churn Generator
```

Retention is generated after user behavior and subscription history have been established.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Datasets

- Users
- Sessions
- Lifecycle
- Events
- Subscriptions

Configuration

- benchmark_profiles
- probability_config
- scenario_config
- retention_definition

---

# 5. Outputs

Primary Dataset

Retention

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| user_id | User identifier |
| cohort_date | Signup date |
| retention_window | D1 / D7 / D14 / D30 / D60 / D90 |
| retained | Boolean retention flag |
| first_return | First return timestamp |
| active_days | Number of active days |
| active_sessions | Number of sessions in window |
| activity_level | Low / Medium / High |

Primary Key

(user_id, retention_window)

Foreign Key

user_id → Users.user_id

---

# 7. Retention Generation Model

Retention is determined by long-term user engagement.

Retention probability depends on:

- persona
- acquisition source
- lifecycle progression
- subscription status
- benchmark profile
- active scenarios

Retention is generated independently for each configured retention window.

---

# 8. Generation Workflow

```text
Load Users

↓

Load Sessions

↓

Load Lifecycle

↓

Load Events

↓

Load Subscriptions

↓

Determine Retention Eligibility

↓

Evaluate Retention Probability

↓

Generate Return Activity

↓

Validate Dataset

↓

Publish Dataset
```

---

# 9. Retention Logic

Retention follows business behavior rather than random sampling.

Example

```text
Explorer

↓

D1 Retained

↓

D7 Lost

↓

D30 Lost
```

Power User

```text
D1 Retained

↓

D7 Retained

↓

D30 Retained

↓

D90 Retained
```

Retention probabilities are configurable.

---

# 10. Retention Window

Supported windows

- Day 1
- Day 7
- Day 14
- Day 30
- Day 60
- Day 90

Additional windows may be configured.

Each window is evaluated independently while preserving chronological consistency.

---

# 11. Activity Pattern Generation

For retained users the generator determines:

- number of active days
- number of sessions
- engagement level
- return timing

Higher engagement generally produces stronger retention.

---

# 12. Internal Validation

Before publication, the generator validates:

- valid user_id
- valid retention window
- chronological return timestamps
- non-negative active days
- valid activity level
- consistency between sessions and retention status

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- retained users
- retention rate by window
- retention by acquisition source
- retention by persona
- average active days
- average active sessions
- execution time
- validation warnings

---

# 14. Generator Contract

Input

RuntimeContext

Consumes

- Users Dataset
- Sessions Dataset
- Lifecycle Dataset
- Events Dataset
- Subscriptions Dataset

Produces

Retention Dataset

Publishes

Retention Dataset

Returns

GeneratorResult

---

# 15. References

- generator_master_spec.md
- retention_definition.md
- benchmark_profiles.md
- scenario_config.md
- abstract_generator.md
