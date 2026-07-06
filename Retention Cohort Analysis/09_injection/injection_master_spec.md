# Synthetic SaaS User Behavior Simulator v2.0

# Injection Layer Master Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Injection Philosophy
3. Injection Layer Architecture
4. Injection Categories
5. Injection Pipeline
6. Injection Contracts
7. Injection Scope
8. Runtime Responsibilities
9. Design Principles
10. Extension Strategy
11. References

---

# 1. Purpose

The Injection Layer intentionally introduces realistic data quality issues into otherwise valid synthetic datasets.

The objective is to simulate production-grade datasets where analysts must perform data cleaning, validation, and anomaly detection before analysis.

The Injection Layer never creates business behavior.

It only modifies dataset quality.

---

# 2. Injection Philosophy

The Injection Layer follows six architectural principles.

## Post Generation

Injection occurs only after all generators have completed successfully.

---

## Config Driven

All injected anomalies originate from configuration.

No anomaly is hardcoded.

---

## Controlled Chaos

Injected issues are realistic but remain statistically controlled.

---

## Reproducible

Using the same random seed produces identical injected anomalies.

---

## Independent

Each Injection Engine is responsible for one anomaly category.

---

## Optional

Every Injection Engine may be enabled or disabled independently.

---

# 3. Injection Layer Architecture

```text
Generated Datasets
        │
        ▼
Injection Registry
        │
────────────────────────────────────────────
        │
        ▼
Dirty Data Engine
        │
        ▼
Duplicate Engine
        │
        ▼
Missing Value Engine
        │
        ▼
Timestamp Engine
        │
        ▼
Event Order Engine
────────────────────────────────────────────
        │
        ▼
Dirty Dataset Registry
```

Injection Engines execute according to the configured pipeline.

---

# 4. Injection Categories

| Engine | Purpose |
|---------|---------|
| Dirty Data Engine | Orchestrates all injections |
| Duplicate Engine | Creates duplicate records |
| Missing Value Engine | Introduces NULL or missing fields |
| Timestamp Engine | Alters timestamps |
| Event Order Engine | Produces out-of-order events |

Future engines may be added without modifying existing implementations.

---

# 5. Injection Pipeline

Every Injection Engine follows the same execution lifecycle.

```text
Load Dataset

↓

Read Configuration

↓

Select Target Records

↓

Inject Anomaly

↓

Internal Validation

↓

Publish Dataset
```

Each engine operates on the output of the previous engine.

---

# 6. Injection Contracts

Every Injection Engine must:

- consume one or more datasets
- read only injection configuration
- preserve schema compatibility
- record injected anomalies
- publish updated datasets
- return InjectionResult

Injection Engines must never:

- generate new business entities
- alter business rules
- modify runtime configuration
- bypass the Dataset Registry

---

# 7. Injection Scope

Injection can be applied at multiple levels.

| Scope | Description |
|--------|-------------|
| Global | Entire dataset |
| Dataset | Specific dataset only |
| Column | Specific columns |
| Row | Selected records |
| Segment | Specific user segments (e.g. Ads, Mobile, Country) |

Scopes are defined through configuration.

---

# 8. Runtime Responsibilities

Each Injection Engine is responsible for:

- loading published datasets
- selecting target records
- injecting configured anomalies
- validating output schema
- publishing modified datasets
- recording execution metrics

The following responsibilities belong outside Injection Engines:

- business generation
- validation orchestration
- exporting datasets
- analytics

---

# 9. Design Principles

## Preserve Schema

Injection must never change dataset schemas.

---

## Preserve Referential Integrity (Unless Configured)

Foreign keys remain valid unless an injection explicitly targets referential integrity.

---

## Configurable Severity

Injection intensity is configurable.

Examples

- Low
- Medium
- High

---

## Observable

Every injected anomaly is recorded.

---

## Deterministic

Injected records remain reproducible using the same configuration and random seed.

---

## Layer Isolation

Each Injection Engine is independent and interchangeable.

---

# 10. Extension Strategy

Future Injection Engines may include:

- Inconsistent Label Engine
- Orphan Record Engine
- Late Arrival Engine
- Timezone Drift Engine
- Schema Drift Engine
- Type Mismatch Engine
- Duplicate Session Engine

Each new engine must implement the Injection Contract and register with the Injection Registry.

---

# 11. References

- dirty_data_definition.md
- data_quality_rules.md
- validation_contract.md
- generator_master_spec.md
- dirty_data_config.md
