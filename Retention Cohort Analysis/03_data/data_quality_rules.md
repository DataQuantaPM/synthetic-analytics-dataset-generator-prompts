# Synthetic SaaS User Behavior Simulator v2.0

# Data Quality Rules

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Data Quality Philosophy
3. Validation Layers
4. Data Quality Dimensions
5. Entity Validation Rules
6. Relationship Validation Rules
7. Temporal Validation Rules
8. Business Validation Rules
9. Dirty Data Constraints
10. Data Quality Report
11. Quality Levels
12. Data Lineage
13. References

---

# 1. Purpose

This document defines the data quality standards that every generated dataset must satisfy.

The simulator distinguishes between:

- Clean Dataset (fully validated)
- Dirty Dataset (controlled anomalies)

Both datasets must comply with the quality framework described in this document.

---

# 2. Data Quality Philosophy

The simulator follows four principles.

## Accuracy

Generated values should represent realistic SaaS behavior.

---

## Consistency

Related datasets must remain logically consistent.

---

## Completeness

Critical business fields must always exist.

---

## Recoverability

Injected anomalies must be recoverable using realistic SQL cleaning techniques.

---

# 3. Validation Layers

Validation is performed in multiple stages.

```text
User Generation
        │
        ▼
Entity Validation
        │
        ▼
Relationship Validation
        │
        ▼
Business Rule Validation
        │
        ▼
Clean Dataset
        │
        ▼
Dirty Data Injection
        │
        ▼
Quality Validation
        │
        ▼
Raw Dataset
```

Each stage validates a different aspect of data quality.

---

# 4. Data Quality Dimensions

The simulator evaluates the following quality dimensions.

| Dimension | Description |
|------------|-------------|
| Completeness | Required fields are populated |
| Uniqueness | Duplicate primary keys do not exist |
| Consistency | Related datasets agree with each other |
| Validity | Values conform to business rules |
| Accuracy | Generated values are realistic |
| Integrity | Foreign keys remain valid |
| Timeliness | Events occur within valid time windows |
| Recoverability | Dirty data can be repaired |

---

# 5. Entity Validation Rules

Each entity must satisfy the following requirements.

## Users

✓ Unique user_id

✓ Valid signup date

✓ Valid acquisition source

✓ Valid lifecycle state

---

## Sessions

✓ Unique session_id

✓ Existing user_id

✓ Positive duration

✓ session_start < session_end

---

## Events

✓ Unique event_id

✓ Valid event_name

✓ Existing session_id

✓ Existing user_id

✓ Valid timestamp

---

## Subscriptions

✓ Unique subscription_id

✓ Existing user_id

✓ Valid plan

✓ Valid status

---

## Revenue

✓ Unique revenue_id

✓ Existing subscription_id

✓ Positive amount

✓ Valid billing period

---

# 6. Relationship Validation Rules

Relationships between entities must remain consistent.

| Parent | Child | Validation |
|---------|-------|------------|
| User | Session | Every session belongs to one user |
| User | Event | Every event belongs to one user |
| Session | Event | Every event belongs to one session |
| User | Subscription | One active subscription at a time |
| Subscription | Revenue | Revenue references a valid subscription |

---

# 7. Temporal Validation Rules

Time consistency is verified across the dataset.

## User

Signup occurs before all future activities.

---

## Session

Session Start

↓

Events

↓

Session End

---

## Subscription

Trial

↓

Paid

↓

Renewal

↓

Cancellation

---

## Revenue

Billing occurs only during active subscription periods.

---

# 8. Business Validation Rules

The simulator enforces realistic business behavior.

### User Lifecycle

Users cannot skip lifecycle states.

Example:

```
Signup

↓

Purchase
```

Invalid

---

Correct:

```
Signup

↓

Activation

↓

Trial

↓

Purchase
```

---

### Session

A session must contain exactly one login event.

---

### Retention

Week 0 retention equals cohort size.

---

### Churn

Last activity must occur before churn date.

---

### Revenue

Free plans cannot generate recurring revenue.

---

# 9. Dirty Data Constraints

Dirty data is intentionally generated under controlled limits.

| Dirty Data | Maximum Default Rate |
|-------------|--------------------:|
| Missing Values | 2% |
| Duplicate Events | 3% |
| Label Variants | 2% |
| Timestamp Drift | 2% |
| Event Ordering | 1% |
| Delayed Tracking | 2% |
| Orphan Records | Disabled |
| Impossible Values | Disabled |

Critical business entities are protected unless explicitly configured otherwise.

---

# 10. Data Quality Report

After generation, the simulator produces a quality summary.

Example:

| Check | Status |
|---------|--------|
| User Validation | PASS |
| Session Validation | PASS |
| Event Validation | PASS |
| Revenue Validation | PASS |
| Referential Integrity | PASS |
| Duplicate Detection | PASS |
| Dirty Data Injection | PASS |

Additional statistics include:

- total users
- total sessions
- total events
- duplicate count
- missing values
- orphan records
- invalid timestamps

---

# 11. Quality Levels

The simulator classifies data quality into four levels.

| Level | Description |
|---------|-------------|
| Level 1 | Perfect clean dataset |
| Level 2 | Minor realistic anomalies |
| Level 3 | Production-like dirty dataset |
| Level 4 | Stress testing dataset |

Default generation uses **Level 2**, balancing realism with analytical usability.

---

# 12. Data Lineage

```text
Configuration
      │
      ▼
Simulation Engines
      │
      ▼
Validation Engine
      │
      ▼
Clean Dataset
      │
      ▼
Dirty Data Injector
      │
      ▼
Quality Validation
      │
      ▼
Raw Dataset
      │
      ▼
SQL Cleaning
      │
      ▼
Analytics Dataset
```

Quality validation occurs before and after dirty data injection to ensure recoverability.

---

# References

- dirty_data_definition.md
- business_rules.md
- data_dictionary.md
- event_dictionary.md
- session_definition.md
- revenue_definition.md
- retention_definition.md
- churn_definition.md
