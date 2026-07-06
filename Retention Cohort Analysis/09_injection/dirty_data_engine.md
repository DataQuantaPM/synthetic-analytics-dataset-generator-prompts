# Synthetic SaaS User Behavior Simulator v2.0

# Dirty Data Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Engine Architecture
7. Execution Workflow
8. Injection Planning
9. Engine Orchestration
10. Report Generation
11. Internal Validation
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Dirty Data Engine is the orchestration layer responsible for executing all enabled data quality injection engines.

Unlike individual Injection Engines, the Dirty Data Engine does not inject anomalies itself.

Instead, it coordinates the execution order, manages dataset publication, aggregates execution reports, and produces the final dirty datasets.

It serves as the entry point for the entire Injection Layer.

---

# 2. Responsibilities

The Dirty Data Engine is responsible for:

- resolving enabled injection engines
- building the execution plan
- executing injection engines
- managing dataset versions
- collecting injection reports
- publishing dirty datasets

The Dirty Data Engine is **not** responsible for:

- injecting duplicate records
- generating missing values
- modifying timestamps
- reordering events

These responsibilities belong to dedicated Injection Engines.

---

# 3. Engine Position

```text
Clean Dataset Registry

↓

Dirty Data Engine

↓

Duplicate Engine

↓

Missing Value Engine

↓

Timestamp Engine

↓

Event Order Engine

↓

Dirty Dataset Registry
```

The Dirty Data Engine coordinates execution but never performs individual anomaly injection.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Datasets

Clean datasets published by the Generator Layer.

Configuration

- dirty_data_config
- simulator_config

---

# 5. Outputs

Primary Outputs

- Dirty Datasets
- Injection Report
- Dataset Version Metadata

Published to:

Dirty Dataset Registry

---

# 6. Engine Architecture

```text
Dirty Data Engine

│

├── Resolve Configuration

├── Build Execution Plan

├── Execute Injection Engines

├── Aggregate Reports

├── Publish Dirty Dataset

└── Return Engine Result
```

The Dirty Data Engine acts purely as an orchestrator.

---

# 7. Execution Workflow

```text
Load Clean Datasets

↓

Read Injection Configuration

↓

Resolve Enabled Engines

↓

Determine Execution Order

↓

Execute Injection Engines

↓

Validate Final Dataset

↓

Generate Injection Report

↓

Publish Dirty Dataset
```

Execution order is configurable but deterministic.

---

# 8. Injection Planning

Before execution, the Dirty Data Engine constructs an Injection Plan.

The plan specifies:

- enabled engines
- execution order
- target datasets
- target columns
- severity level
- random stream assignment

Each engine receives only its assigned portion of the plan.

---

# 9. Engine Orchestration

Each Injection Engine executes independently.

Example execution sequence:

```text
Duplicate Engine

↓

Missing Value Engine

↓

Timestamp Engine

↓

Event Order Engine
```

The Dirty Data Engine ensures that:

- dependencies are respected
- engines execute once
- outputs are published between stages
- failures are recorded

---

# 10. Report Generation

After execution, the Dirty Data Engine aggregates all Injection Results.

The final Injection Report includes:

- engines executed
- anomalies injected
- records modified
- execution duration
- warnings
- errors
- dataset version

The report is published alongside the dirty datasets.

---

# 11. Internal Validation

Before publication, the engine validates:

- execution order completed
- required engines executed
- dataset schema preserved
- report successfully generated
- dataset successfully published

If validation fails, publication is aborted.

---

# 12. Runtime Metrics

Recorded metrics include:

- engines executed
- total records modified
- anomalies by type
- execution time
- dirty dataset size
- validation warnings

Metrics are published to the Runtime Metrics registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- Clean Dataset Registry

Produces

- Dirty Dataset Registry
- Injection Report

Coordinates

- Duplicate Engine
- Missing Value Engine
- Timestamp Engine
- Event Order Engine

Returns

EngineResult

---

# 14. References

- injection_master_spec.md
- dirty_data_config.md
- dirty_data_definition.md
- validation_contract.md
- engine_contract.md
