# Synthetic SaaS User Behavior Simulator v2.0

# Retention Definition

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Retention Philosophy
3. Retention Types
4. Cohort Definition
5. Active User Definition
6. Retention Calculation
7. Retention Dataset Schema
8. Business Rules
9. Validation Rules
10. Edge Cases
11. Data Lineage
12. Tableau Usage
13. References

---

# 1. Purpose

This document defines how user retention is calculated throughout the simulator.

Retention is one of the primary Product Analytics metrics used to measure user engagement over time.

The simulator generates a retention-ready analytical table that can be consumed directly by SQL and Tableau.

---

# 2. Retention Philosophy

The simulator adopts **Classic Weekly Cohort Retention**.

Users are grouped according to the week in which they signed up.

Retention measures whether those users return and perform meaningful product activity during subsequent weeks.

This definition closely mirrors retention analysis used in SaaS Product Analytics.

---

## Why Weekly Cohorts?

Weekly cohorts provide a balance between:

- daily noise
- monthly granularity

Weekly retention is especially suitable for B2B SaaS products where users may not return every day but are expected to engage regularly.

---

# 3. Retention Types

The simulator focuses on **Classic Retention**.

Other retention definitions are documented for reference.

| Type | Supported | Description |
|--------|:---------:|------------|
| Classic Retention | ✓ | User active in week N |
| Rolling Retention | Future | User active on or after week N |
| Bracket Retention | Future | User active within a range |
| Unbounded Retention | Future | User ever returns |

Only Classic Retention is exported by default.

---

# 4. Cohort Definition

Users belong to exactly one cohort.

The cohort is determined by the Monday of the signup week.

Example

| Signup Date | Cohort Week |
|--------------|-------------|
| 2026-01-07 | 2026-01-05 |
| 2026-01-09 | 2026-01-05 |
| 2026-01-13 | 2026-01-12 |

Each user remains in the same cohort permanently.

---

# 5. Active User Definition

A user is considered **retained** if they perform at least one meaningful product activity during a given cohort week.

Supported activity events:

- login
- dashboard_view
- feature_used
- report_created
- invite_team_member

Passive events such as payment processing are excluded.

---

## Week Index

Retention uses a zero-based cohort index.

| Cohort Index | Meaning |
|--------------|---------|
| 0 | Signup Week |
| 1 | First Week After Signup |
| 2 | Second Week |
| ... | ... |

Week 0 always equals 100%.

---

# 6. Retention Calculation

The simulator calculates retention as:

```text
Retention Rate

=

Retained Users

───────────────

Cohort Size
```

The retention table includes:

- cohort_size
- retained_users
- retention_rate_pct

Retention is calculated independently for every cohort and segmentation.

---

## Supported Segmentations

Retention may be filtered by:

- Acquisition Source
- Country
- Device
- Early Plan
- Latest Plan

These dimensions are preserved during SQL transformation.

---

# 7. Retention Dataset Schema

| Column | Description |
|----------|-------------|
| signup_week | Cohort week |
| cohort_index | Week number |
| cohort_size | Number of users in cohort |
| retained_users | Active users |
| retention_rate_pct | Retention percentage |
| first_touch_source | Acquisition source |
| first_touch_country | Country |
| first_touch_device | Device |
| early_plan_type | Initial plan |
| latest_plan_type | Current plan |

---

# 8. Business Rules

The following rules always apply.

### Rule 1

Every user belongs to one cohort only.

---

### Rule 2

Week 0 retention is always 100%.

---

### Rule 3

Users may skip intermediate weeks.

Example

Week 0 ✓

Week 1 ✗

Week 2 ✓

Week 2 still counts as retained.

---

### Rule 4

Retention is based on user activity, not session count.

---

### Rule 5

Multiple events during the same week count as one retained user.

---

### Rule 6

Duplicate events must not increase retained_users.

---

# 9. Validation Rules

The Validation Engine checks:

✓ Week 0 = Cohort Size

✓ Retention ≤ Cohort Size

✓ No duplicate retained users

✓ Valid cohort_index

✓ Valid signup_week

✓ Retention percentage between 0–100

---

# 10. Edge Cases

The simulator handles several edge cases.

### User Never Returns

Retained only in Week 0.

---

### User Skips Weeks

User remains retained in later weeks if activity resumes.

---

### Duplicate Events

Removed during SQL deduplication.

---

### Missing Events

User is not counted as retained.

---

### Timestamp Drift

Corrected during SQL cleaning before retention calculation.

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
Deduplicated Events
      │
      ▼
Retention SQL
      │
      ▼
retention_table
      │
      ▼
Tableau Dashboard
```

The retention table is always derived from the cleaned event dataset.

---

# 12. Tableau Usage

The exported retention table is optimized for Tableau.

Recommended visualizations:

- Cohort Heatmap
- Retention Trend
- Source Comparison
- Device Comparison
- Country Comparison
- Plan Comparison

Recommended filters:

- signup_week
- source
- country
- device
- early_plan_type
- latest_plan_type

---

# 13. Retention Interpretation Guide

Retention curves reveal how effectively the product keeps users engaged after signup.

Rather than focusing only on percentages, Product Analysts should interpret the *shape* of the retention curve and identify the underlying business behavior.

This section provides guidance for interpreting common retention patterns generated by the simulator.

---

# Reading a Retention Curve

A typical retention curve consists of:

```text
100%

│■■■■■■■■■■■■■■■■ Week 0

│■■■■■■■■

│■■■■■

│■■■

│■■

│■

└────────────────────────────

W0 W1 W2 W3 W4 W5
```

The objective is **not** to keep Week 0 high (it is always 100%), but to minimize unnecessary drop-offs and maintain a stable long-term retention level.

---

# Common Retention Patterns

## 1. Healthy SaaS Retention

```text
100%

│■■■■■■■■■■■■

│■■■■■■■

│■■■■■

│■■■■

│■■■

│■■■
```

### Interpretation

Users continue returning after onboarding.

The product consistently delivers value.

### Possible Causes

- Effective onboarding
- Strong product-market fit
- High feature adoption
- Good activation experience

### Recommended Action

Continue optimizing acquisition while preserving the onboarding experience.

---

## 2. Large Drop After Week 0

```text
100%

│■■■■■■■■■■■■

│■■

│■

│■

│■
```

### Interpretation

Most users never become active after signing up.

The product fails to convert new users into engaged users.

### Possible Causes

- Poor onboarding
- Confusing interface
- Weak activation flow
- Low perceived product value

### Recommended Action

Investigate:

- onboarding completion
- activation rate
- Aha Moment achievement

---

## 3. Gradual Decline

```text
100%

│■■■■■■■■■■■■

│■■■■■■■

│■■■■■■

│■■■■■

│■■■■

│■■■
```

### Interpretation

Users naturally become less active over time.

This is expected behavior for most SaaS products.

### Possible Causes

- Normal usage decay
- Reduced business need
- Seasonal usage

### Recommended Action

Improve long-term engagement through:

- product updates
- notifications
- collaboration features
- habit-forming workflows

---

## 4. Plateau After Initial Drop

```text
100%

│■■■■■■■■■■■■

│■■■■

│■■■

│■■■

│■■■

│■■■
```

### Interpretation

A core group of loyal users continues using the product.

The product has found its retained audience.

### Possible Causes

- Strong product-market fit
- High customer satisfaction
- Sticky workflow

### Recommended Action

Focus on increasing activation into this retained user group.

---

## 5. Sudden Drop After Trial Ends

```text
100%

│■■■■■■■■■■■■

│■■■■■■

│■■■■■

│■■■■

│■

│■
```

### Interpretation

Users engage during the trial but fail to convert into paying customers.

### Possible Causes

- Trial value not demonstrated
- Pricing concerns
- Weak upgrade messaging
- Low perceived ROI

### Recommended Action

Analyze:

- Trial-to-paid conversion
- Pricing experiments
- Upgrade funnel
- Feature gating

---

## 6. Recovery After Several Weeks

```text
100%

│■■■■■■■■■■■■

│■■■■

│■■

│■■■■

│■■■
```

### Interpretation

Some users temporarily become inactive before returning.

This indicates reactivation behavior.

### Possible Causes

- Weekly workflow
- Monthly reporting cycle
- Seasonal usage
- Marketing re-engagement

### Recommended Action

Measure:

- Reactivation rate
- Dormant period
- Email campaign effectiveness

---

# Segment-Level Interpretation

Different user segments often produce different retention curves.

| Segment | Typical Interpretation |
|----------|------------------------|
| Organic | Higher long-term retention due to stronger purchase intent |
| Ads | Faster acquisition but often lower retention quality |
| Referral | Strong engagement driven by trust and recommendations |
| Mobile | More frequent but shorter sessions |
| Desktop | Lower frequency with deeper product usage |
| Free Plan | Higher churn risk |
| Paid Plan | Better long-term retention |

Segment comparison often provides more actionable insights than overall retention alone.

---

# Relationship with Other Metrics

Retention should never be analyzed in isolation.

| Metric | Why It Matters |
|---------|----------------|
| Funnel Conversion | Identifies where users drop before becoming retained |
| Aha Moment | Explains whether users reached product value early |
| Churn Rate | Measures permanent user loss |
| Session Frequency | Indicates engagement intensity |
| Feature Adoption | Reveals which behaviors drive retention |
| Revenue | Connects user retention to business outcomes |

A decline in retention should always be investigated alongside these complementary metrics.

---

# Diagnostic Checklist

When retention declines unexpectedly, investigate the following questions:

- Did onboarding completion decrease?
- Did fewer users reach the Aha Moment?
- Did acquisition sources change?
- Did product usage patterns shift?
- Was there a pricing or subscription change?
- Did session frequency decline?
- Was a new feature or UI introduced?
- Did data quality or event tracking change?

Following this checklist helps distinguish between genuine business issues and measurement problems.

---

# Analyst Best Practices

When interpreting retention:

- Focus on trends rather than isolated weeks.
- Compare cohorts over time.
- Analyze retention by acquisition source, country, device, and plan.
- Validate unusual patterns against raw event data.
- Avoid drawing conclusions from small cohort sizes.
- Combine retention analysis with funnel, churn, and Aha Moment metrics.

Retention is most valuable when used as part of a broader product health assessment rather than as a standalone KPI.

---

# References

- event_dictionary.md
- churn_definition.md
- session_definition.md
- data_dictionary.md
