# Synthetic SaaS User Behavior Simulator v2.0

# Validation Contract

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Validation Philosophy
3. Validation Architecture
4. Validation Lifecycle
5. Validation Interface
6. Validation Result Contract
7. Validation Categories
8. Runtime Contract
9. Validation Rules
10. References

---

# 1. Purpose

The Validation Contract defines the standard architecture for validating generated datasets during simulation.

Rather than defining validation rules themselves, this document specifies how the Validation Engine executes, reports, and communicates validation results.

Every validation component must follow this contract.

---

# 2. Validation Philosophy

Validation follows five principles.

## Independent

Validation never modifies datasets.

---

## Deterministic

The same dataset always produces the same validation result.

---

## Read Only

Validators inspect data only.

They never repair data.

---

## Layered

Validation occurs at multiple levels.

- schema
- dataset
- business
- system

---

## Comprehensive

Validation continues until every enabled validator has executed.

Validation results are aggregated into a single report.

---

# 3. Validation Architecture

```text
Generated Dataset
        │
        ▼
Validation Engine
        │
        ├── Schema Validator
        ├── Dataset Validator
        ├── Business Validator
        ├── Relationship Validator
        ├── Benchmark Validator
        └── QA Validator
                │
                ▼
      Validation Report
```

Validation components operate independently.

Each validator produces partial results that are combined into a final Validation Report.

---

# 4. Validation Lifecycle

Every validator follows the same lifecycle.

```text
INITIALIZED

↓

READY

↓

VALIDATING

↓

REPORTING

↓

COMPLETED
```

If validation cannot continue:

```text
VALIDATING

↓

FAILED
```

---

# 5. Validation Interface

Every validator implements the following interface.

| Method | Responsibility |
|----------|----------------|
| initialize() | Prepare validator |
| validate() | Execute validation logic |
| report() | Produce validation result |
| finalize() | Cleanup resources |

---

## initialize()

Responsibilities

- receive Runtime Context
- prepare validation resources

---

## validate()

Responsibilities

- inspect datasets
- execute validation rules
- collect findings

---

## report()

Responsibilities

- generate Validation Result
- classify findings
- calculate summary metrics

---

## finalize()

Responsibilities

- release temporary resources
- record execution metrics

---

# 6. Validation Result Contract

Each validator returns a standardized Validation Result.

```text
ValidationResult

├── validator_name
├── status
├── passed
├── warnings
├── errors
├── execution_time
├── metrics
└── details
```

---

## Status

Supported values

- PASS
- WARNING
- FAIL
- SKIPPED

---

## Metrics

Example metrics

- rules evaluated
- rules passed
- rules failed
- execution duration

---

# 7. Validation Categories

Validation is divided into independent categories.

| Category | Purpose |
|----------|---------|
| Schema | Validate column structure |
| Dataset | Validate row-level integrity |
| Business | Validate business rules |
| Relationship | Validate foreign keys and references |
| Benchmark | Compare against configured targets |
| QA | Validate overall data quality |

Each category may contain multiple validators.

---

# 8. Runtime Contract

Validation Engine receives Runtime Context.

```text
RuntimeContext

├── resolved_config
├── datasets
├── logger
├── metrics
├── runtime_metadata
└── execution_state
```

Validation Engine may read Runtime Context but must not modify generated datasets.

---

# 9. Validation Rules

## Rule 1

Validation never changes datasets.

---

## Rule 2

Validators execute independently.

---

## Rule 3

Validation occurs only after all generators complete.

---

## Rule 4

Validation Report aggregates every validator result.

---

## Rule 5

Validation failures are reported but never silently ignored.

---

## Rule 6

Validation metrics are recorded for every validator.

---

## Rule 7

Validation must complete before Output Engine executes.

---

## Rule 8

All validation results must be reproducible.

---

# References

- core_master_spec.md
- architecture.md
- engine_contract.md
- abstract_generator.md
- simulation_pipeline.md
- validation.md
- qa_rules.md
