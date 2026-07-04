# Synthetic SaaS User Behavior Simulator v2.0

# User Lifecycle State Machine

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. State Machine Philosophy
3. Lifecycle Overview
4. Lifecycle States
5. State Transition Diagram
6. Transition Rules
7. Hidden Variable Influence
8. Scenario Influence
9. State Outputs
10. Terminal States
11. Validation Rules
12. References

---

# 1. Purpose

This document defines the lifecycle state machine governing every simulated user.

Rather than generating events randomly, the simulator first determines the user's current lifecycle state. The active state then controls which actions, sessions, and events the user is allowed to generate.

The state machine guarantees behavioral consistency across the entire simulation.

---

# 2. State Machine Philosophy

The simulator follows a finite state machine (FSM).

Every user occupies exactly one lifecycle state at any given point in time.

A user may transition to another state only if all transition conditions are satisfied.

State transitions are driven by:

- Hidden Variables
- Business Rules
- Personas
- Active Scenarios

Events never trigger state changes directly.

Instead, both events and state transitions are consequences of the user's underlying behavioral model.

---

# 3. Lifecycle Overview

The default lifecycle is illustrated below.

```

Visitor

↓

Signup

↓

Exploring

↓

Learning

↓

Adopting

↓

Trial

↓

Basic

↓

Pro

↓

Advocate

```

Alternative paths include:

```

Signup

↓

Exploring

↓

Dormant

↓

Reactivated

↓

Learning

```

or

```

Signup

↓

Learning

↓

Churned

```

---

# 4. Lifecycle States

| State | Description |
|---------|-------------|
| Visitor | User has not yet signed up (optional for future versions) |
| Signup | Account has been created |
| Exploring | User is discovering the product |
| Learning | User starts using core features |
| Adopting | Product becomes part of the workflow |
| Trial | User activates the free trial |
| Basic | Paid Basic subscription |
| Pro | Paid Pro subscription |
| Advocate | Highly engaged power user |
| Dormant | Temporarily inactive |
| Churned | Permanently inactive |
| Reactivated | Returns after dormancy |

Only one lifecycle state may be active at any time.

---

# 5. State Transition Diagram

```

Visitor

↓

Signup

↓

Exploring

↓

Learning

↓

Adopting

↓

Trial

↓

Basic

↓

Pro

↓

Advocate

```

Possible side transitions

```

Exploring

↓

Dormant

↓

Reactivated

↓

Learning

```

```

Learning

↓

Churned

```

```

Basic

↓

Cancelled

↓

Dormant

```

---

# 6. Transition Rules

## Signup → Exploring

Requirements

- Signup completed
- Initial session generated

---

## Exploring → Learning

Requirements

- Multiple exploratory sessions
- Increased Engagement Score
- Core features discovered

---

## Learning → Adopting

Requirements

- Aha Moment achieved
- Product usage becomes consistent

---

## Adopting → Trial

Requirements

- Eligible for trial
- High Intent Score

---

## Trial → Basic

Requirements

- Successful conversion
- Positive Health Score
- Low Price Sensitivity

---

## Basic → Pro

Requirements

- Collaboration demand increases
- High Engagement Score
- High Adoption Score

---

## Any Active State → Dormant

Occurs when activity falls below the inactivity threshold.

---

## Dormant → Reactivated

Requires renewed engagement.

---

## Dormant → Churned

Occurs after prolonged inactivity.

---

## Pro → Advocate

Requirements

- Very high engagement
- Frequent collaboration
- Long-term retention

---

# 7. Hidden Variable Influence

Hidden variables determine transition probabilities.

Examples

| Variable | Influence |
|------------|-------------------------|
| Engagement Score | Activity level |
| Adoption Score | Product maturity |
| Intent Score | Upgrade likelihood |
| Health Score | Churn risk |
| Collaboration Score | Team expansion |
| Price Sensitivity | Paid conversion |

The simulator never transitions solely based on elapsed time.

---

# 8. Scenario Influence

Business scenarios modify transition probabilities.

Examples

| Scenario | Primary Impact |
|------------|---------------------------|
| Weak Onboarding | Slower Exploring → Learning |
| Feature Discovery Problem | Lower Learning → Adopting |
| Low Quality Ads | Lower Trial conversion |
| Pricing Resistance | Lower Trial → Basic |
| High Churn | Faster Active → Dormant |

Scenarios influence probabilities but never violate valid state transitions.

---

# 9. State Outputs

Each lifecycle state controls expected behavior.

| State | Typical Sessions | Feature Usage | Upgrade Probability |
|----------|----------------:|--------------:|--------------------:|
| Exploring | Low | Low | Very Low |
| Learning | Medium | Medium | Low |
| Adopting | Medium | High | Medium |
| Trial | High | High | High |
| Basic | High | High | Medium |
| Pro | Very High | Very High | High |
| Advocate | Very High | Extremely High | N/A |
| Dormant | None | None | None |
| Churned | None | None | None |

---

# 10. Allowed Events by State

Each lifecycle state determines which events may be generated.

Events not listed for the current state are considered invalid and must not be generated unless explicitly triggered by another lifecycle transition.

| Lifecycle State | Allowed Events | Typical Session Frequency | Primary Goal | Possible Next States |
|-----------------|----------------|--------------------------|--------------|----------------------|
| Signup | signup, email_verified | One-time | Create account | Exploring |
| Exploring | login, dashboard_view, profile_updated | Low | Discover the product | Learning, Dormant |
| Learning | login, dashboard_view, feature_used, report_created | Medium | Learn core workflows | Adopting, Dormant |
| Adopting | login, dashboard_view, feature_used, report_created, invite_team_member | Medium–High | Integrate product into workflow | Trial, Basic, Dormant |
| Trial | trial_started, login, dashboard_view, feature_used, report_created, invite_team_member | High | Evaluate premium features | Basic, Expired, Dormant |
| Basic | login, dashboard_view, feature_used, report_created, invite_team_member, subscription_renewed | High | Maintain active subscription | Pro, Dormant, Cancelled |
| Pro | login, dashboard_view, feature_used, report_created, invite_team_member, subscription_renewed, subscription_upgraded | Very High | Maximize product value | Advocate, Dormant, Cancelled |
| Advocate | login, dashboard_view, feature_used, report_created, invite_team_member, referral_sent | Very High | Drive expansion and referrals | Dormant |
| Dormant | login, reactivated | Very Low | Return to active usage | Reactivated, Churned |
| Reactivated | reactivated, login, dashboard_view, feature_used | Medium | Resume product adoption | Learning, Adopting |
| Churned | *(No user-generated events)* | None | Terminal State | None |

---

## Event Restrictions

The simulator enforces the following restrictions:

- A user cannot generate events outside the list defined for the current lifecycle state.
- Subscription events are only valid during subscription-related states.
- Collaboration events require at least the Adopting state.
- Referral events are only available to Advocate users.
- Churned users cannot generate any events.
- Dormant users remain inactive until a successful reactivation occurs.

---

## State Capability Matrix

| Capability | Signup | Exploring | Learning | Adopting | Trial | Basic | Pro | Advocate | Dormant | Reactivated | Churned |
|------------|:------:|:---------:|:--------:|:--------:|:-----:|:-----:|:---:|:---------:|:--------:|:------------:|:--------:|
| Login | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Dashboard Access | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Core Feature Usage | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Report Creation | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Team Invitation | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ |
| Subscription Upgrade | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Subscription Renewal | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| Referral | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |

---

## Validation Rules

During simulation, the Event Engine validates every generated event against the user's current lifecycle state.

Any event that violates the state capability matrix is rejected before being written to the dataset.

This guarantees that every event sequence remains consistent with the user's lifecycle progression.

# 11. Terminal States

Terminal states represent the end of active lifecycle progression.

Current terminal states:

- Churned

Future versions may introduce:

- Account Deleted
- Organization Closed
- Fraudulent Account

---

# 12. Validation Rules

Before export, the simulator validates:

- One active state per user
- No impossible transitions
- Chronological state order
- Valid subscription alignment
- Valid lifecycle completion
- State consistency with generated events

Datasets violating lifecycle integrity are rejected.

---

# References

- business_rules.md
- simulation_spec.md
- pricing.md
- subscription_lifecycle.md
- execution_pipeline.md
