# Synthetic SaaS User Behavior Simulator v2.0

# Lifecycle Generator Specification

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
7. Lifecycle Model
8. Generation Workflow
9. Lifecycle Transition Logic
10. Transition Constraints
11. Initial & Terminal States
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Lifecycle Generator assigns business lifecycle states to users over time.

Unlike event generation, lifecycle generation represents the user's business progression through the SaaS product.

It determines which lifecycle milestones each user reaches and when those transitions occur.

These lifecycle states become the foundation for downstream Event, Subscription, Retention, Revenue, and Churn generators.

---

# 2. Responsibilities

The Lifecycle Generator is responsible for:

- determining lifecycle progression
- assigning lifecycle timestamps
- enforcing valid state transitions
- preventing impossible lifecycle paths
- publishing lifecycle records

The Lifecycle Generator is **not** responsible for:

- generating raw events
- generating subscriptions
- calculating revenue
- calculating retention
- predicting churn

---

# 3. Generator Position

```text
Users

↓

Sessions

↓

Lifecycle Generator

↓

Lifecycle Dataset

↓

Event Generator
```

Lifecycle defines business progression before behavioral events are generated.

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

Configuration

- benchmark_profiles
- probability_config
- scenario_config

---

# 5. Outputs

Primary Dataset

Lifecycle

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| user_id | User identifier |
| lifecycle_state | Current lifecycle state |
| entered_at | Timestamp when state is entered |
| previous_state | Previous lifecycle state |
| transition_reason | Scenario or probability trigger |
| lifecycle_order | Sequential order |

Primary Key

(user_id, lifecycle_state)

Foreign Key

user_id → Users.user_id

---

# 7. Lifecycle Model

Supported lifecycle states

```text
SIGNED_UP

↓

EMAIL_VERIFIED

↓

ONBOARDING_STARTED

↓

ONBOARDING_COMPLETED

↓

ACTIVATED

↓

TRIAL

↓

PAID

↓

RETAINED

↓

CHURN_RISK

↓

CHURNED
```

Not every user reaches every state.

Progression depends on benchmark profiles, probabilities, personas, and active scenarios.

---

# 8. Generation Workflow

```text
Load Users

↓

Load Sessions

↓

Assign Initial State

↓

Evaluate Transition Probabilities

↓

Generate Lifecycle Timeline

↓

Validate State Order

↓

Publish Lifecycle Dataset
```

---

# 9. Lifecycle Transition Logic

Transitions are evaluated sequentially.

Example

```text
SIGNED_UP

↓

EMAIL_VERIFIED

↓

ONBOARDING_STARTED

↓

ONBOARDING_COMPLETED

↓

ACTIVATED

↓

TRIAL

↓

PAID
```

Each transition is governed by:

- persona
- acquisition source
- benchmark profile
- active scenarios
- probability configuration

Transition timestamps must remain chronological.

---

# 10. Transition Constraints

The following rules always apply.

A user:

- cannot skip mandatory lifecycle states
- cannot move backwards
- cannot repeat the same lifecycle state
- cannot have overlapping lifecycle timestamps
- cannot transition after reaching CHURNED

Lifecycle progression always follows the predefined state machine.

---

# 11. Initial & Terminal States

Initial State

```text
SIGNED_UP
```

Possible terminal states

```text
PAID

RETAINED

CHURN_RISK

CHURNED
```

Terminal states depend on simulated user behavior.

---

# 12. Internal Validation

Before publication, the generator validates:

- valid lifecycle order
- chronological timestamps
- unique state per user
- valid transition paths
- no skipped mandatory states
- valid initial state
- valid terminal state

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- lifecycle records generated
- transition counts
- conversion between states
- average transition time
- completion rate
- abandonment rate
- execution time
- validation warnings

---

# 14. Generator Contract

Input

RuntimeContext

Consumes

- Users Dataset
- Sessions Dataset

Produces

Lifecycle Dataset

Publishes

Lifecycle Dataset

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- state_machine.md
- business_rules.md
- benchmark_profiles.md
- abstract_generator.md
