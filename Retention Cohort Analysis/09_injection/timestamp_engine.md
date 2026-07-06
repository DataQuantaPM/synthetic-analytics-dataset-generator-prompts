# Synthetic SaaS User Behavior Simulator v2.0

# Timestamp Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Timestamp Injection Model
7. Execution Workflow
8. Timestamp Anomaly Strategies
9. Target Selection
10. Timestamp Rules
11. Internal Validation
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Timestamp Engine introduces realistic timestamp anomalies into generated datasets.

The objective is to simulate production environments where event timestamps differ from their actual occurrence time due to infrastructure, client devices, synchronization delays, or ingestion pipelines.

The engine intentionally degrades temporal accuracy while preserving dataset usability.

---

# 2. Responsibilities

The Timestamp Engine is responsible for:

- modifying timestamps
- introducing temporal anomalies
- preserving schema compatibility
- recording timestamp injection statistics
- publishing updated datasets

The Timestamp Engine is **not** responsible for:

- generating duplicate records
- creating missing values
- reordering events
- modifying business logic

---

# 3. Engine Position

```text
Dataset With Missing Values

↓

Timestamp Engine

↓

Dataset With Timestamp Anomalies

↓

Event Order Engine
```

Timestamp anomalies are injected before event ordering anomalies.

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

Dataset containing timestamp anomalies.

Published to:

Dirty Dataset Registry

---

# 6. Timestamp Injection Model

Timestamp anomalies simulate production timing issues.

Typical causes include:

- client clock drift
- delayed ingestion
- offline synchronization
- batch processing
- message queue delay
- timezone conversion errors
- clock skew
- late event arrival

Timestamp anomalies remain deterministic under the configured random seed.

---

# 7. Execution Workflow

```text
Load Dataset

↓

Read Timestamp Configuration

↓

Select Target Records

↓

Select Injection Strategy

↓

Modify Timestamps

↓

Validate Dataset

↓

Publish Dataset
```

---

# 8. Timestamp Anomaly Strategies

Supported strategies

## Time Shift

Move timestamps forward or backward.

Example

```
10:00:15

↓

10:00:27
```

---

## Clock Drift

Gradually shift timestamps within a session.

Example

```
+1 sec

+2 sec

+5 sec

+8 sec
```

---

## Late Arrival

Events occur at the correct business time but appear much later.

Example

```
Occurred

10:00

↓

Recorded

10:17
```

---

## Batch Delay

A group of events receives the same delay.

Example

```
+15 minutes
```

Applied to an entire batch.

---

## Timezone Offset

Shift timestamps by a configured timezone difference.

Example

```
UTC+7

↓

UTC+8
```

---

# 9. Target Selection

Timestamp anomalies may target:

- specific datasets
- event types
- sessions
- users
- countries
- devices
- lifecycle states

Selection follows configuration and remains reproducible.

---

# 10. Timestamp Rules

The following rules apply:

- schema must remain unchanged
- timestamp datatype must remain valid
- timestamps remain inside the simulation window unless explicitly configured
- primary keys are unaffected
- injection ratio follows configuration
- reproducibility is guaranteed

---

# 11. Internal Validation

Before publication, the engine validates:

- schema preserved
- timestamp datatype valid
- configured anomaly ratio achieved
- dataset remains readable
- required timestamps still exist

Publication occurs only after successful validation.

---

# 12. Runtime Metrics

Recorded metrics include:

- timestamps modified
- affected datasets
- affected sessions
- anomaly distribution
- average time shift
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

Dataset With Timestamp Anomalies

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
