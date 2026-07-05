# Synthetic SaaS User Behavior Simulator v2.0

# Validation Framework

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Validation Philosophy
3. Validation Pipeline
4. Validation Stages
5. Validation Categories
6. Validation Execution Order
7. Validation Results
8. Failure Handling
9. Reporting
10. Data Lineage
11. References

---

# 1. Purpose

This document defines the validation framework responsible for ensuring that every generated dataset satisfies the simulator's structural, temporal, and business requirements before being released.

Validation guarantees that:

- clean datasets are internally consistent,
- dirty datasets remain recoverable,
- business rules are preserved,
- analytical outputs remain trustworthy.

The Validation Engine is executed automatically during every simulation.

---

# 2. Validation Philosophy

Validation follows four core principles.

## Correctness

Generated data must satisfy all mandatory business rules.

---

## Consistency

Relationships between entities must remain logically valid.

---

## Transparency

Every validation produces an explicit PASS, WARNING, or FAIL result.

---

## Reproducibility

Running the simulator with the same seed should produce identical validation outcomes.

---

# 3. Validation Pipeline

Validation occurs after all simulation engines complete their work.

```text
Configuration
        │
        ▼
Simulation Engines
        │
        ▼
Generated Dataset
        │
        ▼
Validation Engine
        │
        ├──────────────┐
        ▼              ▼
PASS          WARNING / FAIL
        │              │
        ▼              ▼
Export      Validation Report
```

Only validated datasets proceed to export.

---

# 4. Validation Stages

Validation is divided into sequential stages.

## Stage 1 — Schema Validation

Ensures that every dataset contains the expected columns and data types.

Checks include:

- required columns
- column types
- nullable constraints

---

## Stage 2 — Entity Validation

Validates each table independently.

Examples:

- unique primary keys
- valid enum values
- mandatory attributes

---

## Stage 3 — Relationship Validation

Verifies referential integrity.

Examples:

- session → user
- event → session
- subscription → user
- revenue → subscription

---

## Stage 4 — Temporal Validation

Ensures chronological consistency.

Examples:

- signup before login
- session start before session end
- event inside session
- billing after subscription

---

## Stage 5 — Business Rule Validation

Verifies lifecycle and product rules.

Examples:

- no purchase before signup
- free plan generates no revenue
- one active subscription per user
- Week 0 retention = 100%

---

## Stage 6 — Statistical Validation

Evaluates whether generated distributions match the intended simulation targets.

Examples:

- acquisition source distribution
- country distribution
- plan distribution
- retention targets
- churn targets

---

## Stage 7 — Dirty Data Validation

Confirms that injected anomalies remain within configured limits.

Examples:

- duplicate rate
- missing value rate
- timestamp drift rate
- label variation rate

---

# 5. Validation Categories

| Category | Purpose |
|----------|---------|
| Schema | Dataset structure |
| Entity | Individual table correctness |
| Relationship | Foreign key consistency |
| Temporal | Chronological consistency |
| Business | Product logic |
| Statistical | Distribution realism |
| Dirty Data | Controlled anomaly validation |

Each category produces an independent validation summary.

---

# 6. Validation Coverage Matrix

The Validation Coverage Matrix provides a comprehensive overview of which validation categories apply to each generated dataset.

This matrix serves as both implementation documentation for the Validation Engine and an audit checklist for ensuring complete validation coverage.

---

## Coverage Matrix

| Dataset | Schema | Entity | Relationship | Temporal | Business | Statistical | Dirty Data | Blocking Failure |
|----------|:------:|:------:|:------------:|:--------:|:--------:|:-----------:|:----------:|:----------------:|
| users.csv | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | Yes |
| sessions.csv | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Yes |
| events.csv | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Yes |
| subscriptions.csv | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Yes |
| revenue.csv | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Yes |
| retention_table.csv | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | No |
| churn_table.csv | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | No |
| validation_report.json | ✓ | ✓ | — | — | ✓ | ✓ | — | No |

---

## Validation Responsibility

Each validation category is handled by a dedicated validator.

| Validation Category | Responsible Module |
|---------------------|--------------------|
| Schema Validation | SchemaValidator |
| Entity Validation | EntityValidator |
| Relationship Validation | RelationshipValidator |
| Temporal Validation | TemporalValidator |
| Business Validation | BusinessRuleValidator |
| Statistical Validation | StatisticalValidator |
| Dirty Data Validation | DirtyDataValidator |

Each validator operates independently and reports its own results.

---

## Validation Timing

Validation occurs at different stages of the simulation pipeline.

| Validation | Execution Stage |
|------------|-----------------|
| Schema | Immediately after dataset creation |
| Entity | After each entity is generated |
| Relationship | After all datasets are generated |
| Temporal | After event generation |
| Business | After lifecycle simulation |
| Statistical | Before export |
| Dirty Data | After anomaly injection |

This staged approach allows errors to be detected as early as possible.

---

## Blocking vs Non-Blocking Validation

Not every validation failure should stop the simulation.

### Blocking Validations

Simulation export is stopped if any of the following fail:

- Invalid primary keys
- Missing required columns
- Broken foreign keys
- Impossible lifecycle transitions
- Revenue before subscription
- Invalid timestamps
- Duplicate primary keys

---

### Non-Blocking Validations

The simulator continues while issuing warnings for:

- Slight distribution drift
- Minor duplicate rate deviations
- Missing optional fields
- Higher-than-expected dirty data percentage
- Country distribution imbalance
- Device distribution imbalance

These issues affect realism but do not invalidate the dataset.

---

## Validation Summary Example

```text
Schema Validation ............. PASS

Entity Validation ............. PASS

Relationship Validation ....... PASS

Temporal Validation ........... PASS

Business Rules ................. PASS

Statistical Validation ......... WARNING

Dirty Data Validation .......... PASS

----------------------------------------

Overall Status ................. PASS
```

---

## Validation Coverage by Pipeline Stage

```text
Configuration
      │
      ▼
User Generator
      │
      ├──────── Schema
      ├──────── Entity
      ▼
Session Generator
      │
      ├──────── Schema
      ├──────── Entity
      ├──────── Relationship
      ▼
Event Generator
      │
      ├──────── Temporal
      ├──────── Business
      ▼
Subscription Generator
      │
      ├──────── Business
      ▼
Revenue Generator
      │
      ├──────── Business
      ▼
Validation Engine
      │
      ├──────── Statistical
      ├──────── Dirty Data
      ▼
Export
```

This visualization highlights that validation is distributed throughout the pipeline rather than performed as a single final step.

---

## Coverage Goals

The Validation Framework is designed to achieve the following objectives:

| Objective | Target |
|-----------|--------|
| Schema Coverage | 100% |
| Entity Coverage | 100% |
| Relationship Coverage | 100% |
| Temporal Coverage | 100% |
| Business Rule Coverage | 100% |
| Statistical Coverage | 100% |
| Dirty Data Coverage | 100% |

Every exported dataset should pass all mandatory validation checks before being considered production-ready for analytical use.

---

# 7. Validation Execution Order

Validation always follows the same sequence.

```text
Schema

↓

Entity

↓

Relationship

↓

Temporal

↓

Business

↓

Statistics

↓

Dirty Data
```

Earlier failures prevent later stages from executing when they would produce misleading results.

---

# 8. Validation Results

Each validation rule returns one of four statuses.

| Status | Meaning | Action |
|---------|---------|--------|
| PASS | Validation successful | Continue |
| INFO | Informational observation | Continue |
| WARNING | Minor issue detected | Continue with caution |
| FAIL | Critical validation failed | Stop export |

---

## Example Output

| Validation | Result |
|------------|--------|
| Schema Validation | PASS |
| Entity Validation | PASS |
| Relationship Validation | PASS |
| Temporal Validation | PASS |
| Business Rules | PASS |
| Statistical Validation | WARNING |
| Dirty Data Validation | PASS |

Overall Result

```text
Simulation Status

PASS
```

---

# 9. Failure Handling

The Validation Engine responds differently depending on severity.

### PASS

Simulation proceeds normally.

---

### INFO

Recorded in the validation report only.

---

### WARNING

Dataset is exported with warnings.

Warnings indicate deviations that remain analytically acceptable.

---

### FAIL

Dataset export is blocked.

Typical causes include:

- broken foreign keys
- impossible lifecycle transitions
- invalid timestamps
- duplicate primary keys
- corrupted subscriptions

---

# 10. Reporting

Every simulation generates a validation report.

Typical report sections include:

## Summary

- simulation timestamp
- configuration profile
- simulator version
- validation duration

---

## Validation Statistics

- total checks
- passed checks
- warnings
- failed checks

---

## Quality Metrics

- duplicate rate
- missing values
- orphan records
- invalid timestamps
- business rule violations

---

## Recommended Actions

If warnings or failures occur, suggested remediation steps are included in the report.

---

# 11. Data Lineage

```text
Configuration
        │
        ▼
Simulation Engines
        │
        ▼
Generated Dataset
        │
        ▼
Validation Engine
        │
        ├──────────────┐
        ▼              ▼
Validation Report
        │
        ▼
Approved Dataset
        │
        ▼
Dirty Data Injection
        │
        ▼
Raw Export
```

Validation is always performed before dirty data injection.

A second validation pass may optionally be executed after anomaly injection to verify recoverability.

---

# References

- data_quality_rules.md
- dirty_data_definition.md
- business_rules.md
- state_machine.md
- execution_pipeline.md
