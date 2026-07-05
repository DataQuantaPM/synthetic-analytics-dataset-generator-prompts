# Synthetic SaaS User Behavior Simulator v2.0

# Subscription Generator Specification

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
7. Subscription Lifecycle Model
8. Generation Workflow
9. Subscription State Logic
10. Billing Cycle Assignment
11. Plan Assignment & Changes
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Subscription Generator creates subscription records that represent the commercial relationship between users and the SaaS product.

Unlike lifecycle states or events, subscription records describe contractual access to product plans over time.

These records provide the foundation for revenue generation and subscription analytics.

---

# 2. Responsibilities

The Subscription Generator is responsible for:

- creating subscription records
- assigning subscription plans
- determining subscription start dates
- generating plan upgrades and downgrades
- generating renewals
- generating cancellations
- publishing the Subscription dataset

The Subscription Generator is **not** responsible for:

- payment transactions
- invoice generation
- revenue recognition
- churn prediction

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

Subscription Generator

↓

Subscriptions Dataset

↓

Revenue Generator
```

Subscriptions are generated after business progression has been established.

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
- Lifecycle
- Events

Configuration

- benchmark_profiles
- probability_config
- pricing
- subscription_lifecycle

---

# 5. Outputs

Primary Dataset

Subscriptions

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| subscription_id | Unique subscription identifier |
| user_id | User identifier |
| plan | Subscription plan |
| billing_cycle | Monthly / Annual |
| subscription_status | Current subscription status |
| started_at | Subscription start time |
| ended_at | Subscription end time (nullable) |
| renewal_date | Next renewal date |
| previous_plan | Previous plan (nullable) |
| transition_reason | Upgrade, downgrade, renewal, cancellation |

Primary Key

subscription_id

Foreign Key

user_id → Users.user_id

---

# 7. Subscription Lifecycle Model

Supported subscription states

```text
NO_SUBSCRIPTION

↓

TRIAL

↓

ACTIVE

↓

RENEWED

↓

DOWNGRADED

↓

UPGRADED

↓

CANCELLED

↓

EXPIRED
```

Not every user reaches every state.

State transitions depend on lifecycle progression, pricing configuration, benchmark profiles, and active scenarios.

---

# 8. Generation Workflow

```text
Load Users

↓

Load Lifecycle

↓

Load Events

↓

Determine Subscription Eligibility

↓

Assign Initial Plan

↓

Generate Subscription Timeline

↓

Assign Billing Cycle

↓

Generate Renewals & Changes

↓

Validate Dataset

↓

Publish Dataset
```

---

# 9. Subscription State Logic

Subscriptions follow a chronological timeline.

Example

```text
TRIAL

↓

ACTIVE

↓

RENEWED

↓

UPGRADED

↓

ACTIVE

↓

CANCELLED

↓

EXPIRED
```

Allowed transitions are defined by the Subscription Lifecycle configuration.

Backward transitions that violate business rules are prohibited.

---

# 10. Billing Cycle Assignment

Each subscription is assigned a billing cycle.

Supported values

- Monthly
- Annual

Billing cycle assignment may depend on:

- country
- plan
- benchmark profile
- persona

Renewal dates are calculated based on the billing cycle.

---

# 11. Plan Assignment & Changes

Supported plans

- Free
- Starter
- Pro
- Business
- Enterprise

Possible plan transitions

- Trial → Starter
- Starter → Pro
- Pro → Business
- Business → Enterprise

Downgrades are also supported where permitted by business rules.

Plan changes are recorded as separate subscription transitions.

---

# 12. Internal Validation

Before publication, the generator validates:

- unique subscription_id
- valid user_id
- valid subscription status
- chronological subscription timeline
- valid billing cycle
- valid plan
- valid renewal dates
- no overlapping active subscriptions for the same user

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- subscriptions generated
- active subscriptions
- trial users
- paid users
- renewals
- upgrades
- downgrades
- cancellations
- plan distribution
- billing cycle distribution
- execution time
- validation warnings

---

# 14. Generator Contract

Input

RuntimeContext

Consumes

- Users Dataset
- Lifecycle Dataset
- Events Dataset

Produces

Subscriptions Dataset

Publishes

Subscriptions Dataset

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- subscription_lifecycle.md
- pricing.md
- benchmark_profiles.md
- abstract_generator.md
