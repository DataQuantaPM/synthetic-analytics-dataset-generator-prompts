# Synthetic SaaS User Behavior Simulator v2.0

# Abstract Generator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Generator Philosophy
3. Generator Hierarchy
4. Abstract Generator Interface
5. Generator Lifecycle
6. Runtime Contract
7. Dataset Contract
8. Generator Responsibilities
9. Generator Rules
10. References

---

# 1. Purpose

This document defines the common abstraction shared by all business generators.

Rather than implementing business logic, the Abstract Generator provides a standardized execution model that all generators inherit.

Its objectives are to:

- eliminate duplicated logic
- standardize execution
- simplify extension
- enforce consistent runtime behavior

---

# 2. Generator Philosophy

Every generator follows the same execution pattern.

```text
Receive Runtime Context

↓

Read Configuration

↓

Read Required Dataset(s)

↓

Generate Output

↓

Validate Internal Result

↓

Publish Dataset

↓

Return Generator Result
```

Only the business generation logic differs between generators.

---

# 3. Generator Hierarchy

```text
AbstractEngine

        │

        ▼

AbstractGenerator

        │

────────────────────────────────────────

        │

        ├── UserGenerator

        ├── SessionGenerator

        ├── EventGenerator

        ├── SubscriptionGenerator

        ├── RevenueGenerator

        └── RetentionGenerator
```

Every business generator extends Abstract Generator.

---

# 4. Abstract Generator Interface

Every generator implements the following interface.

| Method | Responsibility |
|----------|----------------|
| prepare() | Prepare generation |
| generate() | Generate business entities |
| validate_output() | Validate generated dataset |
| publish() | Register dataset into Runtime Context |
| cleanup() | Release temporary resources |

---

## prepare()

Responsibilities

- read Runtime Context
- read Resolved Configuration
- load required datasets
- initialize random stream

---

## generate()

Responsibilities

- execute business generation logic
- create dataset
- collect metrics

---

## validate_output()

Responsibilities

- verify schema
- verify row count
- verify business constraints

---

## publish()

Responsibilities

- register generated dataset
- update Runtime Context

---

## cleanup()

Responsibilities

- remove temporary objects
- finalize runtime metrics

---

# 5. Generator Lifecycle

Every generator follows the same lifecycle.

```text
CREATED

↓

PREPARING

↓

READY

↓

GENERATING

↓

VALIDATING

↓

PUBLISHING

↓

COMPLETED
```

If an unrecoverable error occurs

```text
GENERATING

↓

FAILED
```

---

# 6. Runtime Contract

Each generator receives Runtime Context.

```text
RuntimeContext

├── resolved_config

├── datasets

├── random_manager

├── logger

├── metrics

└── runtime_metadata
```

Generators must never construct their own runtime services.

---

# 7. Dataset Contract

Every generator consumes one or more datasets and produces exactly one primary dataset.

| Generator | Input Dataset(s) | Output Dataset |
|------------|------------------|----------------|
| User Generator | None | Users |
| Session Generator | Users | Sessions |
| Event Generator | Users, Sessions | Events |
| Subscription Generator | Events | Subscriptions |
| Revenue Generator | Subscriptions | Revenue |
| Retention Generator | Events | Retention |

Generated datasets become available through the Runtime Context.

---

# 8. Generator Responsibilities

Each generator is responsible for:

- generating exactly one business entity
- maintaining deterministic behavior
- recording execution metrics
- validating generated output
- publishing datasets
- reporting execution status

Generators are **not** responsible for:

- configuration resolution
- output export
- dirty data injection
- global validation
- orchestration

---

# 9. Generator Rules

## Rule 1

One generator produces one primary dataset.

---

## Rule 2

Generators never invoke other generators directly.

---

## Rule 3

Generators consume only published datasets.

---

## Rule 4

Generators never modify datasets produced by other generators.

---

## Rule 5

Generators use only their assigned random stream.

---

## Rule 6

Business logic belongs exclusively inside generate().

---

## Rule 7

Generated datasets must be published before downstream generators execute.

---

## Rule 8

Every generator must produce execution metrics.

---

# References

- engine_contract.md
- architecture.md
- dependency_graph.md
- simulation_pipeline.md
- validation_contract.md
