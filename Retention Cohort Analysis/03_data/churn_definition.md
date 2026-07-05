# Synthetic SaaS User Behavior Simulator v2.0

# Churn Definition

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Churn Philosophy
3. Churn Types
4. Churn Lifecycle
5. Churn Detection Logic
6. Churn Dataset Schema
7. Business Rules
8. Validation Rules
9. Edge Cases
10. Data Lineage
11. Tableau Usage
12. Churn Interpretation Guide
13. References

---

# 1. Purpose

This document defines how behavioral churn is calculated within the simulator.

Behavioral churn measures when users stop engaging with the product rather than when they cancel a subscription.

The simulator produces a churn-ready analytical table for SQL analysis and Tableau dashboards.

---

# 2. Churn Philosophy

The simulator measures **behavioral churn**.

A user is considered churned when they remain inactive for longer than the configured inactivity threshold.

This definition reflects product engagement rather than billing status.

Behavioral churn is often more useful for Product Analytics because it detects declining engagement before revenue is lost.

---

## Why Behavioral Churn?

Behavioral churn enables earlier intervention.

A user who has stopped using the product is already at high risk of cancelling later.

Monitoring inactivity provides opportunities for:

- lifecycle campaigns
- product improvements
- reactivation programs
- customer success outreach

---

# 3. Churn Types

The simulator recognizes multiple churn concepts.

| Type | Supported | Description |
|------|:---------:|-------------|
| Behavioral Churn | ✓ | User becomes inactive |
| Subscription Churn | Future | Subscription cancelled |
| Revenue Churn | Future | MRR decreases |
| Logo Churn | Future | Customer leaves entirely |

Behavioral churn is exported by default.

---

# 4. Churn Lifecycle

```text
Signup
    │
    ▼
Active
    │
    ▼
Inactive
    │
    ▼
Dormant
    │
    ▼
Churned
    │
    └───────────────┐
                    ▼
              Reactivated
```

A churned user may return later if reactivation is enabled.

---

# 5. Churn Detection Logic

The simulator determines churn using the user's last recorded activity.

```text
Last Activity

+

Inactivity Threshold

=

Churn Date
```

The default inactivity threshold is configurable.

---

## Last Activity

A user's last activity is defined as the most recent occurrence of one of the following events:

- login
- dashboard_view
- feature_used
- report_created
- invite_team_member

Passive events are ignored.

---

## Churn Week

Churn is reported using weekly granularity.

```text
Churn Week

=

Week containing

Last Activity + Threshold
```

---

## Reactivation

If a user performs a valid activity after being classified as churned:

- churn status is removed;
- a reactivation event may be generated (optional);
- future retention calculations continue normally.

---

# 6. Churn Risk Levels

While **Churn Status** identifies users who have already churned, **Churn Risk Level** estimates the likelihood that an active user will churn in the near future.

Risk levels are based on the number of days since the user's last meaningful activity.

This classification enables proactive intervention before a user reaches the churn threshold.

---

## Risk Classification

| Days Since Last Activity | Risk Level | Description |
|--------------------------:|------------|-------------|
| 0–6 | Healthy | User is actively engaging with the product. |
| 7–13 | Low Risk | Slight reduction in activity but still within normal behavior. |
| 14–27 | Medium Risk | Engagement is declining and the user should be monitored. |
| 28–41 | High Risk | User is approaching the inactivity threshold and is likely to churn. |
| 42+ | Churned | User exceeds the inactivity threshold and is classified as churned. |

The default inactivity threshold is **42 days**, but it can be configured through the simulator settings.

---

## Risk Transition

Users naturally move between risk levels as inactivity increases.

```text
Healthy
    │
    ▼
Low Risk
    │
    ▼
Medium Risk
    │
    ▼
High Risk
    │
    ▼
Churned
```

If the user performs a valid activity at any point, the inactivity timer resets and the user immediately returns to the **Healthy** state.

---

## Reset Logic

The following events reset the inactivity timer:

- login
- dashboard_view
- feature_used
- report_created
- invite_team_member

Passive events such as billing or subscription renewals do **not** reset churn risk.

---

## Business Interpretation

| Risk Level | Business Meaning | Suggested Product Action |
|------------|------------------|--------------------------|
| Healthy | User is regularly engaged. | Continue delivering product value. |
| Low Risk | Early signs of declining engagement. | Monitor usage patterns. |
| Medium Risk | User may abandon the product soon. | Trigger educational emails, feature recommendations, or in-app guidance. |
| High Risk | User is very likely to churn. | Prioritize re-engagement campaigns, customer success outreach, or targeted promotions. |
| Churned | User is inactive beyond the configured threshold. | Focus on win-back campaigns or analyze churn causes. |

---

## Relationship with Product Metrics

Churn Risk should be analyzed together with other behavioral indicators.

| Metric | Why It Matters |
|---------|----------------|
| Session Frequency | Declining sessions often precede higher churn risk. |
| Feature Adoption | Users with low feature adoption typically progress to higher risk levels. |
| Aha Moment | Users who never reach the Aha Moment have elevated churn risk. |
| Retention | High retention cohorts generally contain a larger proportion of Healthy users. |
| Revenue | Increasing churn risk among paying users may indicate future revenue loss. |

---

## Example Timeline

```text
Day 0      Login
Day 5      Dashboard View
Day 12     No Activity      → Low Risk
Day 20     No Activity      → Medium Risk
Day 35     No Activity      → High Risk
Day 42     No Activity      → Churned
Day 48     Login            → Reactivated → Healthy
```

This example illustrates that churn is **not necessarily permanent**. A user can re-engage with the product and re-enter the active lifecycle.

---

## Analytical Usage

The `churn_risk_level` field can be used to:

- Monitor users approaching churn.
- Segment engagement campaigns.
- Measure the effectiveness of reactivation initiatives.
- Prioritize Customer Success outreach.
- Build predictive churn models.
- Compare risk distributions across acquisition sources, plans, countries, and devices.

Unlike the binary `churned` flag, `churn_risk_level` provides a graduated view of user health, enabling earlier and more targeted business actions.

---

# 7. Churn Dataset Schema

| Column | Description |
|----------|-------------|
| user_id | User identifier |
| signup_week | Original cohort |
| last_activity_date | Most recent active date |
| last_activity_week | Week of last activity |
| churn_date | Estimated churn date |
| churn_week | Churn week |
| days_since_last_activity | Days inactive |
| churned | 0 / 1 |
| reactivated | 0 / 1 |
| first_touch_source | Acquisition source |
| first_touch_country | Country |
| first_touch_device | Device |
| early_plan_type | Initial plan |
| latest_plan_type | Current plan |

---

# 8. Business Rules

The following rules always apply.

### Rule 1

Every user has at most one active churn status.

---

### Rule 2

Churn is based on inactivity rather than subscription cancellation.

---

### Rule 3

Signup alone does not count as activity.

A user who signs up but never performs a meaningful action is considered inactive immediately after the inactivity threshold.

---

### Rule 4

Only meaningful product interactions reset the inactivity timer.

---

### Rule 5

Users may reactivate after churn.

---

### Rule 6

Duplicate events must not affect last activity calculations.

---

### Rule 7

The latest valid activity always determines churn.

---

# 9. Validation Rules

The Validation Engine checks:

✓ churn_date ≥ last_activity_date

✓ valid inactivity threshold

✓ no duplicate churn records

✓ valid user_id

✓ valid last activity

✓ churned ∈ {0,1}

✓ reactivated ∈ {0,1}

---

# 10. Edge Cases

### User Never Returns

User churns after the inactivity threshold expires.

---

### User Has Signup Only

Signup does not reset inactivity.

The user churns without ever becoming active.

---

### User Returns After Churn

User becomes reactivated.

---

### Duplicate Events

Ignored after SQL deduplication.

---

### Missing Events

May cause earlier churn classification.

---

### Timestamp Drift

Corrected during SQL cleaning before churn calculation.

---

# 11. Data Lineage

```text
users.csv
      │
      ▼
sessions.csv
      │
      ▼
events.csv
      │
      ▼
SQL Cleaning
      │
      ▼
Last Activity Calculation
      │
      ▼
Churn SQL
      │
      ▼
churn_table
      │
      ▼
Tableau Dashboard
```

The churn table is always derived from the cleaned event dataset.

---

# 12. Tableau Usage

Recommended visualizations:

- Churn Trend
- Churn by Cohort
- Churn by Acquisition Source
- Churn by Country
- Churn by Device
- Churn by Plan
- Reactivation Trend

Recommended filters:

- signup_week
- source
- country
- device
- early_plan_type
- latest_plan_type

---

# 13. Churn Interpretation Guide

## Healthy Pattern

Low churn with gradual growth over time indicates stable user engagement.

---

## High Early Churn

A large number of users churn shortly after signup.

Possible causes:

- weak onboarding
- poor activation
- low product value

---

## Segment-Specific Churn

Compare churn across:

- acquisition channels
- countries
- devices
- subscription plans

High churn concentrated in one segment often indicates a localized product or marketing issue.

---

## Reactivation

A meaningful reactivation rate suggests that dormant users can be recovered through product improvements or engagement campaigns.

---

## Relationship with Other Metrics

Churn should always be analyzed alongside:

- Retention
- Funnel Conversion
- Aha Moment
- Session Frequency
- Revenue

Analyzing churn in isolation may lead to misleading conclusions.

---

# References

- retention_definition.md
- session_definition.md
- event_dictionary.md
- data_dictionary.md
