# Synthetic SaaS User Behavior Simulator v2.0

# Revenue Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Revenue Model
7. Generation Workflow
8. Revenue Attributes
9. Revenue Generation Strategy
10. Revenue Rules
11. Runtime Metrics
12. Engine Contract
13. References

---

# 1. Purpose

The Revenue Engine generates financial outcomes based on each customer's subscription lifecycle.

Rather than determining who purchases the product, the Revenue Engine converts commercial subscription states into financial transactions.

The generated Revenue Dataset represents the official financial records of the simulation and serves as the primary source for business metrics such as MRR, ARR, ARPU, LTV, and total revenue.

---

# 2. Responsibilities

The Revenue Engine is responsible for:

- generating revenue transactions
- calculating subscription payments
- generating renewals
- generating upgrades
- generating downgrades
- generating refunds (optional)
- publishing the Revenue Dataset

The Revenue Engine is **not** responsible for:

- purchase decisions
- subscription states
- lifecycle progression
- user behavior
- retention calculation
- churn determination

Those responsibilities belong to upstream engines.

---

# 3. Engine Position

```text
Subscription Engine

↓

Revenue Engine

↓

Clean Dataset Registry
```

The Revenue Engine executes after subscription generation.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- Lifecycle Profiles
- Weekly Activity Profiles
- Session Dataset
- Event Dataset
- Subscription Dataset
- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration

- simulator_config
- benchmark_profiles
- probability_config
- revenue_definition
- revenue_mapping

---

# 5. Outputs

Primary Output

Revenue Dataset

Published to

Simulation Context

Each subscription timeline is converted into financial transactions.

---

# 6. Revenue Model

Revenue is generated from subscription events rather than user events.

Typical revenue sources include:

- new subscriptions
- renewals
- upgrades
- downgrades
- one-time purchases
- add-ons

Every revenue record represents one financial transaction.

Revenue generation is deterministic under identical configuration and random seed.

---

# 7. Generation Workflow

```text
Load Subscription Dataset

↓

Determine Billable Events

↓

Calculate Transaction Amount

↓

Generate Invoice Date

↓

Assign Revenue Type

↓

Validate Revenue Timeline

↓

Publish Revenue Dataset
```

---

# 8. Revenue Attributes

Each revenue transaction contains:

| Attribute | Description |
|------------|-------------|
| revenue_id | Unique revenue identifier |
| user_id | Customer identifier |
| subscription_id | Related subscription |
| transaction_date | Transaction timestamp |
| revenue_type | New / Renewal / Upgrade / Downgrade / Refund |
| billing_cycle | Monthly / Annual |
| plan_name | Purchased plan |
| amount | Transaction amount |
| currency | Transaction currency |
| is_successful | Payment status |

Revenue records are immutable after generation.

---

# 9. Revenue Generation Strategy

Revenue generation depends on:

- subscription timeline
- selected plan
- billing cycle
- renewal schedule
- upgrade history
- downgrade history
- benchmark configuration
- scenario modifiers

Typical behavior

### Monthly Plans

Generate recurring monthly transactions.

### Annual Plans

Generate annual transactions.

### Upgrades

Generate incremental revenue.

### Downgrades

Generate reduced recurring revenue.

### Cancelled Users

Generate no future revenue.

Revenue calculations are configuration-driven.

---

# 10. Revenue Rules

The Revenue Engine ensures:

- every transaction belongs to one subscription
- transactions occur after subscription activation
- renewal dates follow billing cycles
- cancelled subscriptions generate no future revenue
- refunds never exceed previous payments
- transaction dates remain chronological
- revenue generation is reproducible

The engine never:

- change subscription states
- generate user events
- modify lifecycle progression
- determine churn

---

# 11. Runtime Metrics

Recorded metrics include:

- total revenue
- MRR
- ARR
- ARPU
- LTV estimate
- average transaction value
- revenue by plan
- revenue by acquisition source
- successful payment rate
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 12. Engine Contract

Input

RuntimeContext

Consumes

- Subscription Dataset
- Random Manager

Produces

- Revenue Dataset

Publishes

Simulation Context

Returns

EngineResult

---

# 13. References

- simulation_master_spec.md
- subscription_engine.md
- revenue_definition.md
- revenue_mapping.md
- benchmark_profiles.md
- probability_config.md
- generator_master_spec.md
- engine_contract.md
