# Synthetic SaaS User Behavior Simulator v2.0

# Subscription Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Subscription Model
7. Generation Workflow
8. Subscription Attributes
9. Subscription Generation Strategy
10. Subscription State Machine
11. Subscription Rules
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Subscription Engine simulates each customer's commercial relationship with the SaaS product.

Using lifecycle progression, user behavior, hidden variables, and benchmark probabilities, the engine determines subscription status transitions throughout the simulation.

The generated subscription timeline becomes the foundation for downstream revenue generation.

---

# 2. Responsibilities

The Subscription Engine is responsible for:

- generating subscription states
- determining trial participation
- determining paid conversion
- generating subscription lifecycle
- assigning plan transitions
- publishing the Subscription Dataset

The Subscription Engine is **not** responsible for:

- payment transactions
- invoices
- revenue calculations
- retention metrics
- churn metrics

Those responsibilities belong to downstream engines.

---

# 3. Engine Position

```text
Event Engine

↓

Subscription Engine

↓

Revenue Engine
```

The Subscription Engine executes after all product events have been generated.

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
- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration

- simulator_config
- probability_config
- scenario_config
- benchmark_profiles

---

# 5. Outputs

Primary Output

Subscription Dataset

Published to

Simulation Context

Each User Blueprint is enriched with subscription information.

---

# 6. Subscription Model

A subscription represents the commercial state of a customer.

The Subscription Engine determines:

- whether the customer starts a trial
- whether the customer converts
- which plan is selected
- whether upgrades occur
- whether cancellations occur

Subscription progression is deterministic under identical configuration and random seed.

---

# 7. Generation Workflow

```text
Load Event Dataset

↓

Determine Trial Eligibility

↓

Determine Trial Conversion

↓

Assign Subscription Plan

↓

Generate Subscription Timeline

↓

Generate Plan Changes

↓

Validate State Machine

↓

Publish Subscription Dataset
```

---

# 8. Subscription Attributes

Each subscription contains:

| Attribute | Description |
|------------|-------------|
| subscription_id | Unique subscription identifier |
| user_id | Subscription owner |
| subscription_status | Current subscription state |
| plan_name | Assigned plan |
| billing_cycle | Monthly / Annual |
| subscription_start | Start date |
| subscription_end | End date |
| renewal_date | Next renewal |
| cancellation_date | Optional cancellation |
| upgrade_count | Number of upgrades |
| downgrade_count | Number of downgrades |

These attributes remain immutable after generation.

---

# 9. Subscription Generation Strategy

Subscription decisions depend on:

- purchase affinity
- product fit
- engagement score
- activation success
- lifecycle state
- feature adoption
- benchmark profile
- scenario modifiers

Typical behavior

### High Product Fit

Higher paid conversion.

### High Engagement

Higher renewal probability.

### High Churn Risk

Higher cancellation probability.

### Enterprise Personas

Higher annual plan adoption.

Subscription probabilities are configuration-driven.

---

# 10. Subscription State Machine

Subscription follows a valid commercial state machine.

```text
Free

↓

Trial

↓

Paid

↓

Renewed

↓

Upgraded

↓

Downgraded

↓

Cancelled

↓

Expired
```

Not every customer reaches every state.

Transitions are forward-only unless explicitly configured.

Invalid transitions are prohibited.

---

# 11. Subscription Rules

The Subscription Engine ensures:

- subscriptions begin after signup
- trials occur before paid conversion
- upgrades require an active subscription
- downgrades require an existing paid plan
- cancelled subscriptions cannot renew
- subscription timelines remain chronological
- subscription generation is reproducible

The engine never:

- generates payment amounts
- creates invoices
- modifies events
- changes lifecycle states

---

# 12. Runtime Metrics

Recorded metrics include:

- subscriptions generated
- trial users
- paid users
- conversion rate
- plan distribution
- upgrade distribution
- downgrade distribution
- cancellation rate
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- Event Dataset
- Lifecycle Profiles
- Hidden Variable Profiles
- Random Manager

Produces

- Subscription Dataset

Publishes

Simulation Context

Returns

EngineResult

---

# 14. References

- simulation_master_spec.md
- event_engine.md
- revenue_engine.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
