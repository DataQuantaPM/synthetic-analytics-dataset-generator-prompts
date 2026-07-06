# Synthetic SaaS User Behavior Simulator v2.0

# Statistical Validator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Validator Position
4. Inputs
5. Outputs
6. Statistical Validation Model
7. Validation Workflow
8. Validation Categories
9. Benchmark Comparison
10. Validation Rules
11. Internal Validation
12. Runtime Metrics
13. Validator Contract
14. References

---

# 1. Purpose

The Statistical Validator evaluates whether generated datasets remain statistically realistic.

Rather than validating individual records, the validator examines distributions, proportions, conversion rates, retention metrics, revenue metrics, and benchmark alignment.

Its objective is to detect unrealistic simulations before datasets are published.

---

# 2. Responsibilities

The Statistical Validator is responsible for:

- validating statistical distributions
- validating benchmark compliance
- validating conversion metrics
- validating retention metrics
- validating revenue metrics
- producing statistical validation reports

The Statistical Validator is **not** responsible for:

- business rule validation
- schema validation
- duplicate detection
- modifying datasets

---

# 3. Validator Position

```text
Validation Engine

↓

Statistical Validator

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
- Events
- Subscriptions
- Revenue
- Retention
- Churn

Configuration

- benchmark_profiles
- validation_config

---

# 5. Outputs

Primary Outputs

- Statistical Validation Result
- Statistical Metrics
- Benchmark Comparison Report

Published to:

Validation Registry

---

# 6. Statistical Validation Model

Validation focuses on aggregate behavior rather than individual records.

Example metrics include:

- conversion rate
- retention rate
- churn rate
- plan distribution
- acquisition source distribution
- ARPU
- revenue distribution
- activity distribution

Observed values are compared against configured benchmark profiles.

---

# 7. Validation Workflow

```text
Load Datasets

↓

Read Benchmark Profile

↓

Calculate Statistical Metrics

↓

Compare Against Benchmarks

↓

Identify Deviations

↓

Generate Findings

↓

Publish Validation Result
```

---

# 8. Validation Categories

Supported validation categories

## Funnel Metrics

Examples

- signup → activation
- activation → trial
- trial → purchase

---

## Retention Metrics

Examples

- D1
- D7
- D30
- D90

---

## Revenue Metrics

Examples

- MRR
- ARR
- ARPU
- ARPPU

---

## Distribution Metrics

Examples

- acquisition source
- device
- country
- subscription plan
- lifecycle stage

---

## Churn Metrics

Examples

- churn rate
- voluntary churn
- involuntary churn

---

# 9. Benchmark Comparison

Observed metrics are compared against configured benchmark ranges.

Example

| Metric | Benchmark | Observed | Status |
|----------|-----------|----------|--------|
| D30 Retention | 30–40% | 36% | PASS |
| Purchase Rate | 6–8% | 6.5% | PASS |
| Churn Rate | 4–8% | 12% | WARNING |

Tolerance thresholds are configurable.

---

# 10. Validation Rules

The validator ensures:

- distributions remain realistic
- benchmark ranges are respected
- ratios remain within configured tolerance
- extreme outliers are reported
- metrics are reproducible

The validator never modifies datasets.

---

# 11. Internal Validation

Before publication, the validator verifies:

- all required metrics calculated
- benchmark profile loaded
- comparison completed
- report generated successfully

---

# 12. Runtime Metrics

Recorded metrics include:

- metrics evaluated
- benchmark comparisons
- passed metrics
- warnings
- failed metrics
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Validator Contract

Input

RuntimeContext

Consumes

- Published Datasets

Produces

- Statistical Validation Result
- Benchmark Comparison Report

Publishes

Validation Registry

Returns

ValidationResult

---

# 14. References

- validation_master_spec.md
- benchmark.md
- benchmark_profiles.md
- validation_contract.md
- revenue_definition.md
- retention_definition.md
- churn_definition.md
