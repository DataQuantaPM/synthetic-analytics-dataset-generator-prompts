# Synthetic SaaS User Behavior Simulator v2.0

# Revenue Definition

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Revenue Philosophy
3. Revenue Lifecycle
4. Revenue Sources
5. Revenue Schema
6. Revenue Metrics
7. Revenue Business Rules
8. Revenue Validation Rules
9. Revenue Quality Rules
10. Revenue Lineage
11. Revenue Configuration
12. References

---

# 1. Purpose

This document defines how revenue is generated throughout the simulator.

Revenue is produced from subscription billing events and represents the financial outcome of user lifecycle progression.

Unlike behavioral events, revenue records represent financial transactions rather than user interactions.

---

# 2. Revenue Philosophy

The simulator follows a subscription-based SaaS revenue model.

Revenue is generated only when a valid subscription enters a billable state.

The simulator supports recurring revenue rather than one-time purchases.

Revenue generation is deterministic and directly tied to the subscription lifecycle.

---

# 3. Revenue Lifecycle

Revenue follows the lifecycle below.

```text
Signup
    │
    ▼
Trial
    │
    ▼
Paid Subscription
    │
    ▼
Monthly Billing
    │
    ▼
Renewal
    │
    ▼
Upgrade / Downgrade
    │
    ▼
Cancellation
```

Revenue only exists while a subscription remains billable.

---

# 4. Revenue Sources

Revenue can originate from several business actions.

| Source | Description |
|---------|-------------|
| New Subscription | First successful payment |
| Monthly Renewal | Recurring monthly billing |
| Upgrade | User upgrades to a higher plan |
| Downgrade | Reduced subscription value |
| Reactivation | User subscribes again after churn |

Refunds are optional and controlled by simulator configuration.

---

# 5. Revenue Event Mapping

Revenue is generated based on specific subscription lifecycle events rather than general product activity.

This mapping defines which events create financial transactions and how each transaction should be classified.

Behavioral events such as `login` or `feature_used` never generate revenue directly.

---

## Revenue Event Flow

```text
signup
    │
    ▼
trial_started
    │
    ▼
subscription_started
    │
    ▼
payment_success
    │
    ▼
Monthly Renewal
    │
    ├──────────────┐
    ▼              ▼
Upgrade      Downgrade
    │              │
    └──────┬───────┘
           ▼
Cancellation
           │
           ▼
Reactivation (optional)
```

Revenue is always generated **after** a successful subscription state transition.

---

## Event → Revenue Mapping

| Subscription Event | Revenue Generated | Revenue Type | Notes |
|--------------------|------------------|--------------|-------|
| signup | No | None | User registration only |
| login | No | None | Behavioral event |
| dashboard_view | No | None | Behavioral event |
| feature_used | No | None | Product usage only |
| report_created | No | None | Product usage only |
| invite_team_member | No | None | Collaboration event |
| trial_started | No | Trial | Trial is free |
| subscription_started | Yes | New Business | First successful paid subscription |
| payment_success | Yes | Billing | Monthly recurring payment |
| subscription_renewed | Yes | Renewal | Existing subscription renewed |
| subscription_upgraded | Yes | Expansion | Higher plan generates additional MRR |
| subscription_downgraded | Yes | Contraction | Lower plan reduces MRR |
| subscription_cancelled | No | Churn | Stops future recurring revenue |
| subscription_reactivated | Yes | Reactivation | Returning paying customer |
| refund_issued *(optional)* | Yes | Refund | Negative revenue if enabled |

---

## Revenue Type Definitions

| Revenue Type | Description |
|--------------|-------------|
| New Business | First payment from a new customer |
| Renewal | Regular recurring billing |
| Expansion | Additional revenue from an upgrade |
| Contraction | Reduced recurring revenue after downgrade |
| Reactivation | Revenue from a previously churned customer |
| Refund | Negative revenue transaction (optional) |

---

## Billing Logic

Revenue follows these business rules.

### First Payment

```text
Trial

↓

Subscription Started

↓

Payment Success

↓

Revenue Record Created
```

---

### Monthly Renewal

```text
Active Subscription

↓

Billing Date Reached

↓

Payment Success

↓

Revenue Record Created
```

---

### Upgrade

```text
Basic Plan

↓

Upgrade

↓

Pro Plan

↓

Expansion Revenue
```

Only the incremental increase is classified as **Expansion Revenue**.

---

### Downgrade

```text
Pro Plan

↓

Downgrade

↓

Basic Plan

↓

Contraction Revenue
```

The simulator records the reduction in recurring revenue while keeping historical billing records intact.

---

### Cancellation

```text
Active Subscription

↓

Cancellation

↓

No Future Billing
```

Historical revenue remains unchanged.

Future recurring revenue is no longer generated.

---

## Revenue Generation Priority

If multiple subscription events occur on the same day, the simulator processes them in the following order.

| Priority | Event |
|----------|-------|
| 1 | subscription_started |
| 2 | payment_success |
| 3 | subscription_upgraded |
| 4 | subscription_downgraded |
| 5 | subscription_cancelled |
| 6 | subscription_reactivated |

This guarantees deterministic revenue generation.

---

## Relationship with Revenue KPIs

Each revenue type contributes differently to business metrics.

| Revenue Type | MRR | ARR | ARPU | LTV |
|--------------|:---:|:---:|:----:|:---:|
| New Business | ✓ | ✓ | ✓ | ✓ |
| Renewal | ✓ | ✓ | ✓ | ✓ |
| Expansion | ✓ | ✓ | ✓ | ✓ |
| Contraction | ✓ | ✓ | ✓ | ✓ |
| Reactivation | ✓ | ✓ | ✓ | ✓ |
| Refund | ✓ | ✓ | ✓ | ✓ |

---

## Validation Rules

The Validation Engine verifies:

- Revenue is never generated before a paid subscription exists.
- Every revenue record references a valid subscription.
- Billing periods do not overlap.
- Revenue types match the triggering subscription event.
- Expansion and contraction amounts match plan price differences.
- Cancelled subscriptions do not generate future recurring revenue.

Any violation is reported in the QA report.

---

# 5. Revenue Schema

| Column | Type | Nullable | Description | Example |
|---------|------|----------|-------------|---------|
| revenue_id | TEXT | No | Unique revenue record | REV000001 |
| subscription_id | TEXT | No | Subscription reference | SUB000001 |
| user_id | TEXT | No | Paying user | U000001 |
| billing_date | DATE | No | Billing date | 2026-03-01 |
| billing_period | TEXT | No | Monthly period | 2026-03 |
| plan | TEXT | No | Active subscription plan | Basic |
| amount | REAL | No | Revenue amount | 29.00 |
| currency | TEXT | No | Billing currency | USD |
| revenue_type | TEXT | No | Revenue category | Renewal |

---

## Primary Key

revenue_id

---

## Foreign Keys

subscription_id → subscriptions.csv

user_id → users.csv

---

# 6. Revenue Metrics

The simulator supports common SaaS revenue metrics.

| Metric | Description |
|---------|-------------|
| MRR | Monthly Recurring Revenue |
| ARR | Annual Recurring Revenue |
| ARPU | Average Revenue Per User |
| Paying Users | Active paying customers |
| Expansion Revenue | Revenue gained from upgrades |
| Contraction Revenue | Revenue lost from downgrades |
| Churned Revenue | Revenue lost after cancellations |
| Lifetime Revenue | Total revenue generated by a user |

These metrics can be calculated directly from revenue.csv.

---

# 7. Revenue Business Rules

The following business rules always apply.

### Rule 1

Revenue cannot exist without a valid subscription.

---

### Rule 2

Every revenue record belongs to exactly one subscription.

---

### Rule 3

Billing dates must occur after the subscription start date.

---

### Rule 4

Cancelled subscriptions cannot generate future recurring revenue.

---

### Rule 5

Trial users do not generate revenue.

---

### Rule 6

Revenue amount must match the active subscription plan.

---

### Rule 7

Revenue cannot be negative unless refunds are enabled.

---

### Rule 8

Recurring revenue follows the configured billing interval.

---

# 8. Revenue Validation Rules

The Validation Engine verifies:

✓ unique revenue_id

✓ valid subscription_id

✓ valid user_id

✓ positive revenue amount

✓ billing date consistency

✓ one billing record per billing period

✓ revenue matches subscription status

---

# 9. Revenue Quality Rules

Dirty data injection may intentionally create:

- duplicate billing records
- missing billing events
- incorrect billing amount
- wrong currency
- delayed billing dates
- orphan revenue records

These anomalies are injected only after the clean dataset has been generated.

---

# 10. Revenue Lineage

```text
Subscription Engine
        │
        ▼
subscriptions.csv
        │
        ▼
Revenue Engine
        │
        ▼
revenue.csv
        │
        ▼
Revenue KPIs
        │
        ├──────────────┐
        ▼              ▼
MRR            Paying Users
        │              │
        ▼              ▼
ARR            ARPU
        │              │
        └──────┬───────┘
               ▼
      Tableau Revenue Dashboard
```

Revenue is derived exclusively from the subscription lifecycle and should never be generated directly from behavioral events.

---

# 11. Revenue Configuration

The simulator supports configurable financial parameters.

| Configuration | Default | Description |
|---------------|--------:|-------------|
| Billing Cycle | Monthly | Billing interval |
| Currency | USD | Default currency |
| Trial Price | 0 | Free trial amount |
| Free Plan Price | 0 | Free plan amount |
| Basic Plan Price | 29 | Monthly Basic subscription |
| Pro Plan Price | 79 | Monthly Pro subscription |
| Refund Enabled | No | Allow refund generation |
| Renewal Probability | Configurable | Monthly renewal probability |
| Upgrade Probability | Configurable | Upgrade likelihood |
| Downgrade Probability | Configurable | Downgrade likelihood |

All values are configurable through simulation settings.

---

# References

- subscription_lifecycle.md
- pricing.md
- data_dictionary.md
- architecture/execution_pipeline.md
