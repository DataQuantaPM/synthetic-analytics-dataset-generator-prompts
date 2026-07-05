# Synthetic SaaS User Behavior Simulator v2.0

# Revenue Generator Specification

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
7. Revenue Generation Model
8. Generation Workflow
9. Revenue Recognition Logic
10. Revenue Components
11. Currency & Pricing
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Revenue Generator creates financial records representing revenue generated from user subscriptions.

Unlike the Subscription Generator, which models commercial agreements, the Revenue Generator models monetary transactions and recognized revenue.

The generated dataset serves as the primary source for business reporting and financial analytics.

---

# 2. Responsibilities

The Revenue Generator is responsible for:

- generating revenue transactions
- calculating transaction amounts
- recognizing recurring revenue
- recording upgrades and downgrades
- generating refund records (if enabled)
- publishing the Revenue dataset

The Revenue Generator is **not** responsible for:

- subscription lifecycle decisions
- payment gateway simulation
- accounting journal entries
- tax calculation
- churn prediction

---

# 3. Generator Position

```text
Users

↓

Lifecycle

↓

Events

↓

Subscriptions

↓

Revenue Generator

↓

Revenue Dataset

↓

Retention Generator
```

Revenue is generated only after subscription records exist.

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
- Subscriptions

Configuration

- pricing
- benchmark_profiles
- probability_config
- simulator_config

---

# 5. Outputs

Primary Dataset

Revenue

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| revenue_id | Unique revenue identifier |
| subscription_id | Related subscription |
| user_id | User identifier |
| transaction_time | Revenue timestamp |
| revenue_type | Initial / Renewal / Upgrade / Downgrade / Refund |
| amount | Revenue amount |
| currency | Currency |
| billing_cycle | Monthly / Annual |
| plan | Subscription plan |
| recognized | Boolean revenue recognition flag |

Primary Key

revenue_id

Foreign Keys

subscription_id → Subscriptions.subscription_id

user_id → Users.user_id

---

# 7. Revenue Generation Model

Revenue is generated from valid subscription activities.

Supported revenue types

- Initial Purchase
- Renewal
- Upgrade
- Downgrade Adjustment
- Refund (optional)

Revenue is generated only for commercial events that produce monetary value.

---

# 8. Generation Workflow

```text
Load Users

↓

Load Subscriptions

↓

Determine Billable Records

↓

Calculate Transaction Amount

↓

Generate Revenue Timeline

↓

Assign Revenue Type

↓

Validate Revenue

↓

Publish Dataset
```

---

# 9. Revenue Recognition Logic

Revenue follows subscription history.

Example

```text
Trial

↓

Starter Purchase

↓

Monthly Renewal

↓

Upgrade to Pro

↓

Annual Renewal

↓

Cancellation
```

Recognized revenue is recorded for every billable subscription event.

Future invoices are not generated beyond the simulation window.

---

# 10. Revenue Components

Supported revenue categories

- New Revenue
- Renewal Revenue
- Expansion Revenue
- Contraction Revenue
- Refunded Revenue

Each transaction belongs to exactly one revenue category.

---

# 11. Currency & Pricing

Pricing is determined by:

- subscription plan
- pricing configuration
- billing cycle
- country (optional regional pricing)

Supported currencies are configurable.

Default currency is defined in `pricing.md`.

---

# 12. Internal Validation

Before publication, the generator validates:

- unique revenue_id
- valid subscription_id
- valid user_id
- non-negative amount (except refunds if represented as negative values)
- valid revenue type
- chronological transaction timeline
- pricing consistency
- billing cycle consistency

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- revenue transactions generated
- total revenue
- recurring revenue
- average revenue per user (ARPU)
- average revenue per paying user (ARPPU)
- revenue by plan
- revenue by billing cycle
- execution time
- validation warnings

---

# 14. Generator Contract

Input

RuntimeContext

Consumes

- Users Dataset
- Subscriptions Dataset

Produces

Revenue Dataset

Publishes

Revenue Dataset

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- pricing.md
- revenue_definition.md
- subscription_generator.md
- benchmark_profiles.md
- abstract_generator.md
