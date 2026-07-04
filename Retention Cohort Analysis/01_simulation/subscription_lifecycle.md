# Synthetic SaaS User Behavior Simulator v2.0

# Subscription Lifecycle

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Lifecycle Philosophy
3. Subscription States
4. State Transition Diagram
5. State Transition Rules
6. Lifecycle Events
7. Billing Lifecycle
8. Renewal Rules
9. Cancellation Rules
10. Reactivation Rules
11. Validation Rules
12. References

---

# 1. Purpose

This document defines the lifecycle of user subscriptions within the simulator.

Unlike the user lifecycle, the subscription lifecycle focuses exclusively on plan activation, billing, renewal, cancellation, expiration, and reactivation.

The objective is to generate realistic subscription behavior for Product Analytics and Revenue Analytics.

---

# 2. Lifecycle Philosophy

A user's subscription state is independent from the user's engagement level.

Examples:

- An active user may remain on the Free plan.
- A paid subscriber may become inactive before cancelling.
- A churned user may later reactivate.

Subscription behavior is driven by:

- Hidden Variables
- User Persona
- Business Scenarios
- Pricing Rules

---

# 3. Subscription States

The simulator supports the following subscription states.

| State | Description |
|--------|-------------|
| None | No subscription has been activated |
| Trial | User is currently in the free trial period |
| Active | User has an active paid subscription |
| Expired | Trial or paid subscription has expired |
| Cancelled | Subscription has been cancelled |
| Renewed | Subscription has been successfully renewed |
| Reactivated | Previously inactive subscription becomes active again |

---

# 4. State Transition Diagram

```

                Signup
                   │
                   ▼
                Free Plan
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
    Trial Activated      Stay Free
        │
        ▼
 Trial Expiration
        │
 ┌──────┴─────────┐
 │                │
 ▼                ▼
Upgrade        Expired
 │                │
 ▼                ▼
Active Paid   Back to Free
 │
 ▼
Renewal Cycle
 │
 ├───────────────┐
 │               │
 ▼               ▼
Renewed      Cancelled
                  │
                  ▼
             Reactivated

```

---

# 5. State Transition Rules

## None → Trial

Conditions:

- User is eligible.
- Trial is enabled.
- User accepts trial.

---

## None → Free

Occurs immediately after signup when no trial is started.

---

## Trial → Active

Conditions:

- Trial period completed.
- User upgrades.
- Billing succeeds.

---

## Trial → Expired

Occurs when the trial ends without conversion.

---

## Expired → Free

User continues using the free plan after trial expiration.

---

## Active → Renewed

Occurs after a successful recurring payment.

---

## Active → Cancelled

Occurs when the user cancels the subscription.

Cancellation takes effect at the end of the billing cycle.

---

## Cancelled → Reactivated

Conditions:

- User returns.
- Payment succeeds.

---

# 6. Transition Reasons

| Transition              | Possible Reasons                                                     |
| ----------------------- | -------------------------------------------------------------------- |
| Trial → Active          | Reached Aha Moment, High Intent Score, Successful Team Collaboration |
| Trial → Expired         | Low Engagement, Low Feature Adoption, High Price Sensitivity         |
| Active → Cancelled      | Low Product Value, Budget Constraints, Competitive Switch            |
| Cancelled → Reactivated | New Feature Release, Marketing Campaign, Referral Invitation         |


---

# 7. Lifecycle Events

Each transition generates one event.

| Transition | Event |
|------------|-------|
| Signup | signup |
| Trial Activated | trial_started |
| Trial Expired | trial_expired |
| Upgrade | subscription_upgraded |
| Renewal | subscription_renewed |
| Cancellation | subscription_cancelled |
| Reactivation | subscription_reactivated |

Events must always occur in chronological order.

---

# 8. Billing Lifecycle

Recurring billing follows this sequence.

```

Active Subscription

↓

Billing Date

↓

Payment Attempt

↓

Success?

↓

Yes → Renewal

↓

No

↓

Grace Period

↓

Cancelled

```

Future versions may simulate payment failures.

---

# 9. Renewal Rules

Renewal probability depends on:

- Health Score
- Engagement Score
- Product Adoption
- Business Scenario

Higher engagement increases renewal probability.

---

# 10. Cancellation Rules

Cancellation probability increases when:

- Engagement decreases.
- Aha Moment is not reached.
- Activity declines.
- Pricing resistance is high.

Cancellation does not immediately remove product access.

---

# 11. Reactivation Rules

Reactivation may occur when:

- User returns after inactivity.
- Marketing campaigns succeed.
- Product value increases.

Reactivated users preserve their historical activity.

---

# 12. Validation Rules

Before export, the simulator validates:

- Valid subscription chronology
- Billing consistency
- Renewal consistency
- Cancellation consistency
- Revenue consistency
- Duplicate subscription events
- Impossible transitions

Invalid lifecycle paths are rejected.

---

# References

- pricing.md
- business_rules.md
- state_machine.md
- simulation_spec.md
