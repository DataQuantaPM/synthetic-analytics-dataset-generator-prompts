# Synthetic SaaS User Behavior Simulator v2.0

# Dirty Data Definition

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Data Quality Philosophy
3. Injection Strategy
4. Dirty Data Categories
5. Injection Configuration
6. Dirty Data Rules
7. Validation Strategy
8. Cleaning Expectations
9. Data Lineage
10. Business Considerations
11. References

---

# 1. Purpose

This document defines how realistic data quality issues are intentionally injected into the synthetic SaaS dataset.

Unlike random noise generation, dirty data is introduced using controlled business rules that simulate common production data problems encountered by Product Analytics teams.

The objective is to produce datasets that require realistic SQL cleaning, validation, and analytical reasoning.

---

# 2. Data Quality Philosophy

The simulator follows three principles.

## Realistic

Data anomalies should resemble issues found in production environments.

---

## Controlled

Every anomaly is generated according to configurable probabilities.

No anomaly should completely invalidate the dataset.

---

## Recoverable

The clean dataset always remains internally consistent.

Dirty data is applied only after clean data generation, allowing analysts to reconstruct the original information through cleaning pipelines.

---

# 3. Injection Strategy

Dirty data is injected as the final step of the simulation pipeline.

```text
User Generator
        │
        ▼
Lifecycle Engine
        │
        ▼
Session Engine
        │
        ▼
Event Engine
        │
        ▼
Revenue Engine
        │
        ▼
Validation
        │
        ▼
Clean Dataset
        │
        ▼
Dirty Data Injector
        │
        ▼
Raw Dataset
```

The simulator always preserves a clean internal dataset before anomalies are introduced.

---

# 4. Dirty Data Categories

The simulator supports the following categories.

---

## 4.1 Missing Values

Description

Random removal of non-critical values.

Examples

- missing country
- missing device
- missing campaign
- missing session_id (configurable)

Typical Causes

- SDK failure
- network interruption
- optional field omission

---

## 4.2 Duplicate Records

Description

Duplicate rows are intentionally inserted.

Possible Targets

- login
- dashboard_view
- feature_used

Duplicates may be exact or near-duplicates.

Typical Causes

- retry mechanism
- client-side replay
- ingestion duplication

---

## 4.3 Inconsistent Labels

Description

Different labels representing the same business concept.

Examples

```
signup

Signup

SIGNUP

sign_up

user_signup
```

Typical Causes

- inconsistent tracking implementation
- multiple engineering teams
- legacy instrumentation

---

## 4.4 Timestamp Drift

Description

Event timestamps are shifted forward or backward.

Examples

```
09:15

↓

09:13
```

or

```
09:15

↓

09:19
```

Typical Causes

- client clock mismatch
- timezone conversion
- delayed upload

---

## 4.5 Event Ordering Errors

Description

Events appear in an impossible chronological order.

Example

```
feature_used

↓

login
```

Typical Causes

- asynchronous event upload
- delayed queue processing

---

## 4.6 Orphan Records

Description

Foreign keys reference missing parent records.

Examples

- event without session
- session without user
- revenue without subscription

Typical Causes

- partial ingestion
- failed synchronization

---

## 4.7 Delayed Tracking

Description

Events arrive later than their actual occurrence.

Example

```
Actual

10:05

Recorded

10:18
```

Typical Causes

- offline usage
- batch synchronization
- mobile buffering

---

## 4.8 Impossible Values

Description

Invalid attribute values.

Examples

```
Negative revenue

Week = -3

Duration = -15

Future signup

Unknown lifecycle state
```

These anomalies are generated only when explicitly enabled.

---

# 5. Injection Configuration

Every anomaly type is independently configurable.

| Category | Default | Configurable |
|-----------|---------|:------------:|
| Missing Values | 2% | ✓ |
| Duplicate Events | 3% | ✓ |
| Label Variants | 2% | ✓ |
| Timestamp Drift | 2% | ✓ |
| Event Reordering | 1% | ✓ |
| Delayed Tracking | 2% | ✓ |
| Orphan Records | Disabled | ✓ |
| Impossible Values | Disabled | ✓ |

Percentages represent probabilities applied after clean data generation.

---

# 6. Dirty Data Rules

The following rules always apply.

### Rule 1

Dirty data must never exceed configured probabilities.

---

### Rule 2

Critical identifiers (`user_id`, `event_id`) remain unique unless duplicate simulation is enabled.

---

### Rule 3

Revenue integrity is preserved unless financial anomalies are explicitly enabled.

---

### Rule 4

Dirty data must remain recoverable through SQL cleaning.

---

### Rule 5

No anomaly may permanently corrupt the clean dataset.

---

# 7. Validation Strategy

The simulator validates both datasets.

## Clean Dataset

Must satisfy:

- referential integrity
- chronological consistency
- valid lifecycle transitions
- complete business rules

---

## Dirty Dataset

May violate selected rules according to the configured anomaly profile while remaining analytically usable.

---

# 8. Cleaning Expectations

The simulator is designed so analysts should perform common cleaning tasks before analysis.

Typical cleaning includes:

- deduplicate events
- standardize event names
- remove impossible timestamps
- repair ordering
- handle missing values
- validate foreign keys
- rebuild funnel order

These tasks intentionally mirror real Product Analytics workflows.

---

# 9. Data Lineage

```text
Simulation
      │
      ▼
Validated Clean Dataset
      │
      ▼
Dirty Data Injector
      │
      ▼
Raw Export
      │
      ▼
SQL Cleaning
      │
      ▼
Analytics Tables
```

The raw export should always be considered the analytical starting point.

---

# 10. Business Considerations

The inclusion of dirty data serves educational and analytical purposes.

It enables users to:

- practice SQL cleaning
- validate analytical pipelines
- test dashboard robustness
- simulate production-quality datasets
- improve data quality awareness

Dirty data is intentionally limited to realistic levels so that business insights remain recoverable after proper cleaning.

---

# References

- event_dictionary.md
- session_definition.md
- revenue_definition.md
- retention_definition.md
- churn_definition.md
- business_rules.md
