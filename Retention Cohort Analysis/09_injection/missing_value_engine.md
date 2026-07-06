# Synthetic SaaS User Behavior Simulator v2.0

# Missing Value Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Missing Value Injection Model
7. Execution Workflow
8. Missing Value Strategies
9. Target Selection
10. Missing Value Rules
11. Internal Validation
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Missing Value Engine introduces realistic missing values into generated datasets.

The objective is to simulate production environments where certain fields are unavailable due to system limitations, optional inputs, synchronization delays, or data collection failures.

The engine intentionally reduces data completeness while preserving dataset integrity.

---

# 2. Responsibilities

The Missing Value Engine is responsible for:

- selecting target columns
- selecting target records
- replacing values with NULL or missing values
- preserving dataset schema
- recording injection statistics
- publishing updated datasets

The Missing Value Engine is **not** responsible for:

- creating duplicate records
- modifying timestamps
- reordering events
- changing business logic

---

# 3. Engine Position

```text
Dataset With Duplicates

↓

Missing Value Engine

↓

Dataset With Missing Values

↓

Timestamp Engine
```

Missing value injection occurs after duplicate injection by default.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Dataset

Dirty Dataset Registry

Configuration

- dirty_data_config
- probability_config

---

# 5. Outputs

Primary Output

Dataset containing injected missing values.

Published to:

Dirty Dataset Registry

---

# 6. Missing Value Injection Model

Missing values simulate incomplete information rather than incorrect information.

Typical causes include:

- optional fields
- SDK version mismatch
- client-side failures
- API timeout
- consent restrictions
- network interruptions
- partial synchronization

Injected missing values remain statistically controlled and reproducible.

---

# 7. Execution Workflow

```text
Load Dataset

↓

Read Missing Value Configuration

↓

Select Target Columns

↓

Select Target Records

↓

Inject Missing Values

↓

Validate Dataset

↓

Publish Dataset
```

---

# 8. Missing Value Strategies

Supported strategies

## Completely Random

Randomly select eligible cells.

Suitable for low-severity simulation.

---

## Column-Based

Inject missing values into configured columns.

Example

```
campaign

country

device
```

---

## Segment-Based

Inject missing values only for specific segments.

Examples

- Mobile users
- Ads traffic
- Specific countries

---

## Correlated Missing

Missing values depend on another attribute.

Example

```
device = Mobile

↓

campaign missing
```

This simulates realistic production behavior.

---

# 9. Target Selection

Injection targets may be selected by:

- dataset
- column
- user segment
- acquisition source
- lifecycle state
- event type
- probability

Selection is deterministic under the configured random seed.

---

# 10. Missing Value Rules

The following rules apply:

- schema must remain unchanged
- primary keys must never become NULL
- foreign keys must never become NULL unless explicitly configured
- required business fields are protected by default
- injection ratio follows configuration
- reproducibility is guaranteed

---

# 11. Internal Validation

Before publication, the engine validates:

- schema preserved
- protected columns unchanged
- configured missing ratio achieved
- dataset remains readable
- referential integrity maintained

Publication occurs only after successful validation.

---

# 12. Runtime Metrics

Recorded metrics include:

- missing values injected
- affected columns
- affected datasets
- missing ratio
- execution time
- validation warnings

Metrics are published to the Runtime Metrics registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

Dirty Dataset

Produces

Dataset With Missing Values

Publishes

Updated Dirty Dataset

Returns

InjectionResult

---

# 14. References

- injection_master_spec.md
- dirty_data_definition.md
- dirty_data_config.md
- validation_contract.md
