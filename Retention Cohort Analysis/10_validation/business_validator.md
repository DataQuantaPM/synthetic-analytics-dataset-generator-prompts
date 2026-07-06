# Synthetic SaaS User Behavior Simulator v2.0

# Business Validator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Validator Position
4. Inputs
5. Outputs
6. Business Validation Model
7. Validation Workflow
8. Validation Categories
9. Business Rules
10. Validation Rules
11. Internal Validation
12. Runtime Metrics
13. Validator Contract
14. References

---

# 1. Purpose

The Business Validator verifies that generated datasets follow valid SaaS business logic and customer lifecycle rules.

Unlike the Statistical Validator, which evaluates distributions and metrics, the Business Validator evaluates business consistency between entities, events, subscriptions, revenue, retention, and churn.

Its objective is to detect logically impossible customer journeys before datasets are published.

---

# 2. Responsibilities

The Business Validator is responsible for:

- validating lifecycle transitions
- validating event sequences
- validating subscription logic
- validating revenue consistency
- validating retention consistency
- validating churn consistency
- producing business validation reports

The Business Validator is **not** responsible for:

- statistical validation
- schema validation
- duplicate detection
- modifying datasets

---

# 3. Validator Position

```text
Validation Engine

↓

Business Validator

↓

Validation Result
```

The validator executes independently within the Validation Layer.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- Logger
- Metrics

Required Datasets

- Users
- Sessions
- Lifecycle
- Events
- Subscriptions
- Revenue
- Retention
- Churn

Configuration

- validation_config
- benchmark_profiles

---

# 5. Outputs

Primary Outputs

- Business Validation Result
- Business Rule Violations
- Business Validation Report

Published to:

Validation Registry

---

# 6. Business Validation Model

Business validation focuses on logical consistency across the complete customer journey.

Validation includes:

- lifecycle progression
- event dependencies
- subscription transitions
- revenue generation
- retention progression
- churn consistency

Business validation evaluates relationships rather than aggregate metrics.

---

# 7. Validation Workflow

```text
Load Datasets

↓

Load Business Rules

↓

Evaluate Lifecycle

↓

Evaluate Event Flow

↓

Evaluate Subscription Logic

↓

Evaluate Revenue Logic

↓

Evaluate Retention Logic

↓

Evaluate Churn Logic

↓

Generate Findings

↓

Publish Validation Result
```

---

# 8. Validation Categories

Supported categories

## Lifecycle Validation

Examples

- Signup before activation
- Activation before purchase
- Valid lifecycle progression

---

## Event Validation

Examples

- Purchase after trial
- Login before feature usage
- Session starts before session ends

---

## Subscription Validation

Examples

- Upgrade path
- Downgrade path
- Cancellation flow
- Renewal flow

---

## Revenue Validation

Examples

- Revenue only after payment
- Refund after purchase
- Positive transaction amount

---

## Retention Validation

Examples

- D30 implies D7
- Retained users must have activity
- Active users remain eligible

---

## Churn Validation

Examples

- Churn after last activity
- Churn after cancellation
- Churn not before signup

---

# 9. Business Rules

Typical business rules include:

| Rule | Expected |
|-------|----------|
| Signup → Trial | Allowed |
| Trial → Purchase | Allowed |
| Purchase → Trial | Not Allowed |
| Session End → Session Start | Not Allowed |
| Revenue Before Purchase | Not Allowed |
| Churn Before Signup | Not Allowed |

Business rules are configurable.

---

# 10. Validation Rules

The validator ensures:

- lifecycle transitions are valid
- event ordering follows business flow
- subscription states are consistent
- revenue follows payment events
- retention follows activity
- churn follows customer lifecycle

The validator never modifies datasets.

---

# 11. Internal Validation

Before publication, the validator verifies:

- all business rules evaluated
- required datasets available
- findings generated
- report successfully created

---

# 12. Runtime Metrics

Recorded metrics include:

- business rules evaluated
- passed rules
- failed rules
- warnings
- rule violations by category
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Validator Contract

Input

RuntimeContext

Consumes

- Published Datasets

Produces

- Business Validation Result
- Business Rule Violation Report

Publishes

Validation Registry

Returns

ValidationResult

---

# 14. References

- validation_master_spec.md
- state_machine.md
- lifecycle_generator.md
- subscription_generator.md
- revenue_generator.md
- retention_generator.md
- churn_generator.md
- validation_contract.md
