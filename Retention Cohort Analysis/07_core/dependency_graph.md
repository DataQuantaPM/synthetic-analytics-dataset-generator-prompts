# Synthetic SaaS User Behavior Simulator v2.0

# Core Dependency Graph

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Dependency Philosophy
3. High-Level Dependency Graph
4. Dependency Layers
5. Component Dependencies
6. Dependency Matrix
7. Allowed Dependency Rules
8. Forbidden Dependencies
9. Dependency Validation
10. References

---

# 1. Purpose

This document defines the dependency relationships between Core components.

Its objectives are to:

- prevent circular dependencies
- maintain loose coupling
- establish dependency direction
- simplify testing and extensibility

The Core Layer is designed as a Directed Acyclic Graph (DAG).

---

# 2. Dependency Philosophy

The simulator follows four dependency principles.

## One Direction

Dependencies always flow downward.

Higher-level components orchestrate lower-level components.

---

## Dependency Inversion

Components depend on contracts rather than concrete implementations whenever possible.

---

## No Circular Dependencies

No component may directly or indirectly depend on itself.

---

## Single Responsibility

A component should depend only on the services required to fulfill its responsibility.

---

# 3. High-Level Dependency Graph

```text
                    ResolvedConfig
                          │
                          ▼
                    RuntimeContext
                          │
                          ▼
                  SimulationEngine
                          │
                          ▼
                   EngineRegistry
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 RandomManager      RuntimeMetrics      Logger
        │
        ▼
┌──────────────────────────────────────────────────────┐
│               Generator Layer                        │
│                                                      │
│  UserGenerator                                       │
│        │                                             │
│        ▼                                             │
│  SessionGenerator                                    │
│        │                                             │
│        ▼                                             │
│  EventGenerator                                      │
│        │                                             │
│        ▼                                             │
│ SubscriptionGenerator                                │
│        │                                             │
│        ▼                                             │
│ RevenueGenerator                                     │
│        │                                             │
│        ▼                                             │
│ RetentionGenerator                                   │
└──────────────────────────────────────────────────────┘
                          │
                          ▼
                  DirtyDataEngine
                          │
                          ▼
                 ValidationEngine
                          │
                          ▼
                    OutputEngine
```

The dependency graph is strictly acyclic.

---

# 4. Dependency Layers

The Core Layer is divided into dependency levels.

| Level | Components |
|--------|------------|
| L0 | Resolved Configuration |
| L1 | Runtime Context |
| L2 | Simulation Engine |
| L3 | Shared Services |
| L4 | Business Generators |
| L5 | Quality Engines |
| L6 | Output Engine |

Components may only depend on the same layer or lower layers through defined contracts.

---

# 5. Component Dependencies

## Simulation Engine

Depends on:

- Runtime Context
- Engine Registry

Never depends on individual generators.

---

## Engine Registry

Depends on:

- Engine Contracts

Never depends on business implementations.

---

## Runtime Context

Depends on:

- Resolved Configuration
- Random Manager
- Logger
- Runtime Metrics

---

## User Generator

Depends on:

- Runtime Context

Produces:

- Users

---

## Session Generator

Depends on:

- Runtime Context
- Generated Users

Produces:

- Sessions

---

## Event Generator

Depends on:

- Runtime Context
- Users
- Sessions

Produces:

- Events

---

## Subscription Generator

Depends on:

- Runtime Context
- Events

Produces:

- Subscription Records

---

## Revenue Generator

Depends on:

- Runtime Context
- Subscription Records

Produces:

- Revenue

---

## Retention Generator

Depends on:

- Runtime Context
- Events

Produces:

- Retention Tables

---

## Dirty Data Engine

Depends on:

- Runtime Context
- All Generated Datasets

Produces:

- Dirty Dataset

---

## Validation Engine

Depends on:

- Runtime Context
- Final Dataset

Produces:

- Validation Results

---

## Output Engine

Depends on:

- Runtime Context
- Validation Results
- Final Dataset

Produces:

- Exported Artifacts

---

# 6. Dependency Matrix

| Component | Config | Runtime | RNG | Dataset | Validation | Output |
|-----------|:------:|:-------:|:---:|:-------:|:----------:|:------:|
| Simulation Engine | ✓ | ✓ | - | - | - | - |
| User Generator | ✓ | ✓ | ✓ | - | - | - |
| Session Generator | ✓ | ✓ | ✓ | Users | - | - |
| Event Generator | ✓ | ✓ | ✓ | Users, Sessions | - | - |
| Subscription Generator | ✓ | ✓ | ✓ | Events | - | - |
| Revenue Generator | ✓ | ✓ | ✓ | Subscription | - | - |
| Retention Generator | ✓ | ✓ | ✓ | Events | - | - |
| Dirty Data Engine | ✓ | ✓ | ✓ | All | - | - |
| Validation Engine | ✓ | ✓ | - | Final Dataset | - | - |
| Output Engine | ✓ | ✓ | - | Final Dataset | Validation | - |

---

# 7. Allowed Dependency Rules

## Rule 1

Generators may depend on Runtime Context.

---

## Rule 2

Generators may consume datasets produced by earlier generators.

---

## Rule 3

Shared services may be accessed only through Runtime Context.

---

## Rule 4

The Simulation Engine invokes generators through the Engine Registry.

---

## Rule 5

The Output Engine executes only after successful validation.

---

## Rule 6

Configuration objects are read-only.

---

# 8. Forbidden Dependencies

The following dependency patterns are prohibited.

## Generator-to-Generator Calls

❌

```text
UserGenerator

↓

EventGenerator.run()
```

Generators must never invoke each other directly.

---

## Random Instantiation

❌

```python
random.Random()
```

Only the Random Manager may create random streams.

---

## Direct Configuration Access

❌

```python
config.yaml
```

Generators must consume only the Resolved Configuration via the Runtime Context.

---

## Circular Dependency

❌

```text
Revenue Generator

↓

Retention Generator

↓

Revenue Generator
```

Circular dependencies are strictly forbidden.

---

## Output Before Validation

❌

```text
Dataset

↓

Output

↓

Validation
```

Validation must always precede export.

---

# 9. Dependency Validation

The simulator validates dependency integrity during startup.

Validation checks include:

- Circular dependency detection
- Missing engine registrations
- Invalid execution order
- Missing contracts
- Runtime Context availability
- Configuration completeness

Simulation startup fails if dependency validation does not pass.

---

# References

- core_master_spec.md
- architecture.md
- simulation_pipeline.md
- engine_contract.md
- abstract_generator.md
- validation_contract.md
- config_relationship.md
