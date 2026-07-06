# Synthetic SaaS User Behavior Simulator v2.0

# Duplicate Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Duplicate Injection Model
7. Execution Workflow
8. Duplicate Strategies
9. Target Selection
10. Duplicate Rules
11. Internal Validation
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Duplicate Engine introduces realistic duplicate records into generated datasets.

The objective is to simulate production systems where duplicate data may occur due to retries, synchronization issues, pipeline failures, or distributed system behavior.

The engine preserves business realism while intentionally degrading data quality.

---

# 2. Responsibilities

The Duplicate Engine is responsible for:

- selecting records for duplication
- creating duplicate records
- preserving schema compatibility
- recording duplicate statistics
- publishing updated datasets

The Duplicate Engine is **not** responsible for:

- generating business entities
- modifying business logic
- changing dataset schemas
- introducing other anomaly types

---

# 3. Engine Position

```text
Clean Dataset

↓

Duplicate Engine

↓

Dataset With Duplicates

↓

Missing Value Engine
```

Duplicate injection is typically executed before other anomaly engines.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Dataset

One or more datasets published by the Generator Layer.

Configuration

- dirty_data_config
- probability_config

---

# 5. Outputs

Primary Output

Modified dataset containing injected duplicate records.

Published to:

Dirty Dataset Registry

---

# 6. Duplicate Injection Model

Duplicate records simulate operational failures rather than user behavior.

Typical causes include:

- API retry
- Event replay
- ETL rerun
- Message queue redelivery
- Offline synchronization
- Network timeout retry

Injected duplicates should resemble realistic production anomalies.

---

# 7. Execution Workflow

```text
Load Dataset

↓

Read Duplicate Configuration

↓

Select Candidate Records

↓

Generate Duplicate Copies

↓

Apply Duplicate Strategy

↓

Validate Dataset

↓

Publish Dataset
```

---

# 8. Duplicate Strategies

Supported strategies

## Exact Duplicate

The duplicated record is identical to the original.

Example

```
event_name = page_view

timestamp = 10:00:15
```

↓

Duplicate

```
event_name = page_view

timestamp = 10:00:15
```

---

## Near Duplicate

One or more non-key attributes are slightly modified.

Examples

- timestamp shifted by 1–3 seconds
- metadata reordered
- nullable field changed

Business meaning remains identical.

---

## Burst Duplicate

A record is duplicated multiple times within a short interval.

Example

```
purchase

purchase

purchase
```

Simulates repeated retries.

---

# 9. Target Selection

Duplicate targets are selected according to configuration.

Supported scopes

- Entire dataset
- Dataset percentage
- Specific event types
- Specific user segments
- Specific lifecycle states

Target selection is deterministic under the configured random seed.

---

# 10. Duplicate Rules

The following rules apply:

- schema must remain unchanged
- duplicate ratio follows configuration
- duplicated records retain referential integrity
- duplicated records must remain analyzable
- duplicate injection must be reproducible

The engine never creates invalid schemas.

---

# 11. Internal Validation

Before publication, the engine validates:

- schema preserved
- duplicate ratio within configured bounds
- referential integrity maintained
- duplicate records successfully created
- dataset remains readable

Publication occurs only after successful validation.

---

# 12. Runtime Metrics

Recorded metrics include:

- duplicate records injected
- duplicate percentage
- affected datasets
- affected event types
- execution time
- validation warnings

Metrics are published to the Runtime Metrics registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

Published Dataset

Produces

Dataset With Duplicates

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
