# Synthetic SaaS User Behavior Simulator v2.0

# Churn Generator Specification

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
7. Churn Generation Model
8. Generation Workflow
9. Churn Decision Logic
10. Churn Categories
11. Churn Timestamp Assignment
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Churn Generator determines whether and when users permanently stop engaging with the SaaS product.

Unlike the Retention Generator, which models continued engagement, the Churn Generator identifies the end of a user's active lifecycle based on historical behavior and business rules.

The generated churn dataset supports churn analysis, customer health monitoring, cohort reporting, and business forecasting.

---

# 2. Responsibilities

The Churn Generator is responsible for:

- determining churn status
- assigning churn timestamps
- assigning churn category
- assigning churn reason
- publishing the Churn dataset

The Churn Generator is **not** responsible for:

- generating sessions
- generating events
- generating subscriptions
- generating revenue
- calculating retention

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

Retention

↓

Churn Generator

↓

Churn Dataset
```

The Churn Generator is the final business generator executed by the Simulation Engine.

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
- Revenue
- Retention

Configuration

- benchmark_profiles
- probability_config
- churn_definition
- scenario_config

---

# 5. Outputs

Primary Dataset

Churn

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| user_id | User identifier |
| churned | Boolean churn flag |
| churn_date | Churn timestamp |
| churn_category | Voluntary / Involuntary |
| churn_reason | Primary churn reason |
| lifetime_days | Days from signup to churn |
| final_plan | Last subscription plan |
| final_lifecycle_state | Last lifecycle state |
| final_activity_level | Last engagement level |

Primary Key

user_id

Foreign Key

user_id → Users.user_id

---

# 7. Churn Generation Model

Churn is determined using historical user behavior rather than isolated probabilities.

Evaluation considers:

- lifecycle progression
- retention history
- session frequency
- event activity
- subscription status
- revenue history
- benchmark profile
- active scenarios

A user is evaluated only after the full simulation timeline has been generated.

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

Load Revenue

↓

Load Retention

↓

Evaluate Churn Eligibility

↓

Assign Churn Status

↓

Assign Churn Reason

↓

Validate Dataset

↓

Publish Dataset
```

---

# 9. Churn Decision Logic

Churn is evaluated using accumulated behavioral signals.

Example

```text
Low Activity

↓

Retention Decline

↓

Subscription Cancelled

↓

No Return Activity

↓

CHURNED
```

Users with sustained engagement remain active.

Churn probability is configurable but constrained by business rules.

---

# 10. Churn Categories

Supported categories

### Voluntary

Examples

- User cancelled subscription
- Product no longer needed
- Switched to competitor

---

### Involuntary

Examples

- Payment failure
- Subscription expired
- Account disabled

Each churned user belongs to exactly one category.

---

# 11. Churn Timestamp Assignment

Churn timestamps are assigned after the user's final meaningful activity.

Rules

- must occur after the final retained activity
- must occur after the final subscription event
- must remain inside the simulation window
- must be chronologically valid

---

# 12. Internal Validation

Before publication, the generator validates:

- valid user_id
- valid churn status
- chronological churn timestamp
- churn after last activity
- valid churn category
- valid churn reason
- lifetime_days ≥ 0

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- churned users
- churn rate
- voluntary churn
- involuntary churn
- average customer lifetime
- churn by acquisition source
- churn by plan
- churn by persona
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
- Revenue Dataset
- Retention Dataset

Produces

Churn Dataset

Publishes

Churn Dataset

Returns

GeneratorResult

---

# 15. References

- generator_master_spec.md
- churn_definition.md
- retention_generator.md
- benchmark_profiles.md
- abstract_generator.md
