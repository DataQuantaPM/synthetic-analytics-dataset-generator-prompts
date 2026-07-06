# Synthetic SaaS User Behavior Simulator v2.0

# Event Order Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Event Order Injection Model
7. Execution Workflow
8. Event Order Strategies
9. Target Selection
10. Ordering Rules
11. Internal Validation
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Event Order Engine introduces realistic event sequencing anomalies into generated datasets.

The objective is to simulate production environments where events arrive or are processed in an unexpected order due to asynchronous systems, delayed processing, distributed architectures, or ingestion pipelines.

Unlike the Timestamp Engine, which modifies event timestamps, the Event Order Engine modifies the logical ordering of events.

---

# 2. Responsibilities

The Event Order Engine is responsible for:

- modifying event sequence
- breaking logical event ordering
- preserving dataset schema
- recording ordering anomalies
- publishing updated datasets

The Event Order Engine is **not** responsible for:

- modifying timestamps
- generating duplicate records
- generating missing values
- altering business rules

---

# 3. Engine Position

```text
Dataset With Timestamp Anomalies

↓

Event Order Engine

↓

Final Dirty Dataset
```

This is the final Injection Engine executed before validation and export.

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

Dataset containing event ordering anomalies.

Published to:

Dirty Dataset Registry

---

# 6. Event Order Injection Model

Event ordering anomalies simulate failures in distributed systems.

Typical causes include:

- asynchronous processing
- message queue reordering
- delayed consumers
- event replay
- race conditions
- concurrent processing
- eventual consistency
- multi-region replication

The engine modifies logical event order while preserving reproducibility.

---

# 7. Execution Workflow

```text
Load Dataset

↓

Read Event Order Configuration

↓

Select Target Sessions

↓

Select Ordering Strategy

↓

Modify Event Sequence

↓

Validate Dataset

↓

Publish Dataset
```

---

# 8. Event Order Strategies

Supported strategies

## Adjacent Swap

Swap two neighboring events.

Example

```
page_view

button_click
```

↓

```
button_click

page_view
```

---

## Lifecycle Violation

Reverse lifecycle-related events.

Example

```
trial_started

↓

purchase
```

↓

```
purchase

↓

trial_started
```

---

## Session Boundary Violation

Move events outside their expected session flow.

Example

```
session_end

↓

page_view
```

---

## Random Reordering

Randomly reorder a configured subset of events within a session.

Used for high-severity simulations.

---

## Cross-Session Reassignment (Optional)

Move selected events into another session belonging to the same user.

Simulates synchronization failures.

---

# 9. Target Selection

Ordering anomalies may target:

- specific datasets
- event types
- sessions
- lifecycle stages
- user segments
- acquisition sources

Target selection is configuration-driven and deterministic.

---

# 10. Ordering Rules

The following rules apply:

- schema must remain unchanged
- event identifiers remain unique
- injection ratio follows configuration
- ordering anomalies remain reproducible
- referential integrity is preserved unless explicitly configured otherwise

---

# 11. Internal Validation

Before publication, the engine validates:

- schema preserved
- configured anomaly ratio achieved
- dataset remains readable
- required identifiers remain valid
- ordering modifications successfully applied

Publication occurs only after successful validation.

---

# 12. Runtime Metrics

Recorded metrics include:

- reordered events
- affected sessions
- affected users
- ordering strategy distribution
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

Dataset With Event Order Anomalies

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
