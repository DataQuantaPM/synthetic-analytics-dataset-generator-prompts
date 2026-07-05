# Synthetic SaaS User Behavior Simulator v2.0

# Engine Contract

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Contract Philosophy
3. Engine Lifecycle
4. Engine Interface
5. Runtime Contract
6. Engine Result Contract
7. Engine State
8. Error Handling
9. Contract Rules
10. References

---

# 1. Purpose

The Engine Contract defines the minimum interface that every executable engine within the simulator must implement.

It guarantees that all engines:

- expose a consistent lifecycle
- receive the same runtime context
- return standardized results
- report execution status uniformly

The Simulation Engine interacts only with this contract.

---

# 2. Contract Philosophy

Every engine follows the same execution model.

```text
Initialize

↓

Validate

↓

Execute

↓

Finalize

↓

Return Result
```

Business logic differs between engines, but lifecycle behavior remains identical.

---

# 3. Engine Lifecycle

Every engine progresses through the following stages.

```text
CREATED
    │
    ▼
INITIALIZED
    │
    ▼
READY
    │
    ▼
RUNNING
    │
    ▼
COMPLETED
```

If execution fails:

```text
RUNNING

↓

FAILED
```

The lifecycle is managed by the Simulation Engine.

---

# 4. Engine Interface

Every engine must expose the following methods.

| Method | Purpose |
|---------|---------|
| initialize() | Prepare engine resources |
| validate() | Validate prerequisites |
| execute() | Perform engine logic |
| finalize() | Release resources |
| get_result() | Return execution result |

---

## initialize()

Responsibilities

- receive RuntimeContext
- initialize internal state
- prepare dependencies

Input

- RuntimeContext

Output

- Engine initialized

---

## validate()

Responsibilities

- verify prerequisites
- ensure required datasets exist
- validate configuration

Output

- Validation status

---

## execute()

Responsibilities

- perform business logic
- produce datasets or artifacts
- update RuntimeContext if applicable

Output

- EngineResult

---

## finalize()

Responsibilities

- release temporary resources
- write runtime metrics
- update execution status

---

## get_result()

Returns a standardized EngineResult object.

---

# 5. Runtime Contract

Every engine receives the same RuntimeContext.

```text
RuntimeContext

├── resolved_config
├── random_manager
├── logger
├── metrics
├── datasets
├── execution_state
└── runtime_metadata
```

Engines must not access configuration or shared services outside the RuntimeContext.

---

# 6. Engine Result Contract

Every engine returns a standardized result.

```text
EngineResult

├── engine_name
├── status
├── start_time
├── end_time
├── duration
├── output
├── metrics
├── warnings
└── errors
```

---

## Status Values

Supported statuses:

- SUCCESS
- FAILED
- SKIPPED
- WARNING

---

## Output

The engine-specific artifact.

Examples

| Engine | Output |
|---------|--------|
| User Generator | Users Dataset |
| Session Generator | Sessions Dataset |
| Event Generator | Events Dataset |
| Validation Engine | Validation Report |
| Output Engine | Export Manifest |

---

# 7. Engine State

Each engine maintains an internal execution state.

```text
CREATED

↓

INITIALIZED

↓

VALIDATED

↓

RUNNING

↓

COMPLETED
```

State transitions are recorded in RuntimeContext.

---

# 8. Error Handling

All engines follow the same failure policy.

If an error occurs:

1. Stop execution.
2. Record the error.
3. Preserve runtime metrics.
4. Return FAILED status.
5. Allow the Simulation Engine to determine whether execution continues.

Engines must never terminate the application directly.

---

# 9. Contract Rules

## Rule 1

Every engine must implement the full lifecycle.

---

## Rule 2

Every engine receives RuntimeContext.

---

## Rule 3

Every engine returns EngineResult.

---

## Rule 4

Engines must not communicate directly.

Communication occurs only through RuntimeContext.

---

## Rule 5

Engines must never modify ResolvedConfig.

---

## Rule 6

Business logic belongs only inside execute().

---

## Rule 7

All runtime events should be logged.

---

## Rule 8

Execution metrics must be recorded before finalize() completes.

---

# References

- core_master_spec.md
- architecture.md
- dependency_graph.md
- simulation_pipeline.md
- abstract_generator.md
- validation_contract.md
