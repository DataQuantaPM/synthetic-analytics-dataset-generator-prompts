# Synthetic SaaS User Behavior Simulator v2.0

# Core Architecture

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Architectural Goals
3. High-Level Architecture
4. Core Layers
5. Core Components
6. Runtime Context
7. Engine Registry
8. Execution States
9. Data Flow
10. Design Principles
11. References

---

# 1. Purpose

The Core Architecture defines the structural organization of the Synthetic SaaS User Behavior Simulator.

It explains how the major runtime components collaborate to transform configuration into synthetic datasets.

This document focuses on component responsibilities and system interactions rather than implementation details.

---

# 2. Architectural Goals

The architecture is designed to achieve the following goals.

## Modular

Each component performs one clearly defined responsibility.

---

## Config-Driven

Business behavior originates from configuration rather than hardcoded logic.

---

## Deterministic

The same configuration and random seed should generate statistically equivalent datasets.

---

## Extensible

New engines and generators can be added without modifying existing components.

---

## Observable

Every execution stage exposes runtime metrics and logs.

---

# 3. High-Level Architecture

```text
                    Configuration Layer
                           │
                           ▼
                  Config Resolver
                           │
                           ▼
                  Resolved Configuration
                           │
                           ▼
                   Runtime Context
                           │
                           ▼
                 Simulation Engine
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
 Engine Registry      Random Manager     Runtime Metrics
        │
        ▼
 ┌─────────────────────────────────────────────────────────┐
 │                     Generator Layer                     │
 │                                                         │
 │  User Generator                                         │
 │  Session Generator                                      │
 │  Event Generator                                        │
 │  Subscription Generator                                 │
 │  Revenue Generator                                      │
 │  Retention Generator                                    │
 └─────────────────────────────────────────────────────────┘
                           │
                           ▼
                 Dirty Data Engine
                           │
                           ▼
                 Validation Engine
                           │
                           ▼
                   Output Engine
                           │
                           ▼
                    Generated Artifacts
```

The Simulation Engine coordinates execution but delegates business logic to specialized engines.

---

# 4. Core Layers

The Core is organized into logical layers.

| Layer | Responsibility |
|--------|----------------|
| Configuration | Load and resolve simulator configuration |
| Runtime | Maintain execution context and shared services |
| Orchestration | Coordinate execution order |
| Generation | Produce synthetic business entities |
| Quality | Inject dirty data and validate outputs |
| Export | Persist datasets and reports |

Each layer communicates only with adjacent layers.

---

# 5. Core Components

## Config Resolver

Builds the immutable `ResolvedConfig` object.

Input:

- Raw configuration

Output:

- Resolved Configuration

---

## Runtime Context

Central runtime object shared across all engines.

Contains:

- resolved configuration
- random manager
- runtime metrics
- logger
- datasets
- execution state

---

## Simulation Engine

Coordinates the entire simulation lifecycle.

Responsibilities:

- initialize runtime
- execute engines
- monitor execution
- terminate simulation

---

## Engine Registry

Stores all executable engines.

Responsibilities:

- registration
- execution order
- dependency validation

---

## Random Manager

Provides isolated random streams.

Responsibilities:

- initialize master seed
- generate independent streams
- ensure reproducibility

---

## Generator Layer

Responsible for creating business entities.

Generators include:

- User Generator
- Session Generator
- Event Generator
- Subscription Generator
- Revenue Generator
- Retention Generator

Generators never communicate directly with each other.

---

## Dirty Data Engine

Applies configurable data quality issues after generation.

---

## Validation Engine

Ensures generated datasets satisfy business rules and quality requirements.

---

## Output Engine

Exports datasets, reports, metadata, and logs.

---

# 6. Runtime Context

The Runtime Context is the central execution object.

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

Every engine receives the same Runtime Context instance.

Engines must not maintain independent copies of shared runtime state.

---

# 7. Engine Registry

The Engine Registry manages executable components.

```text
Engine Registry

├── User Generator
├── Session Generator
├── Event Generator
├── Subscription Generator
├── Revenue Generator
├── Retention Generator
├── Dirty Data Engine
├── Validation Engine
└── Output Engine
```

Responsibilities:

- engine registration
- dependency ordering
- lifecycle management

The Simulation Engine executes engines through the registry rather than invoking them directly.

---

# 8. Execution States

The simulator transitions through a finite execution lifecycle.

```text
CREATED
    │
    ▼
INITIALIZED
    │
    ▼
RUNNING
    │
    ▼
VALIDATING
    │
    ▼
EXPORTING
    │
    ▼
COMPLETED
```

If an unrecoverable error occurs:

```text
RUNNING

↓

FAILED
```

Each state transition is recorded in runtime metadata.

---

# 9. Data Flow

The simulator processes information through a fixed pipeline.

```text
Configuration

↓

Resolved Configuration

↓

Runtime Context

↓

Generators

↓

Generated Dataset

↓

Dirty Data Injection

↓

Validation

↓

Output Engine

↓

CSV / Reports / Metadata
```

Every transformation stage produces deterministic outputs.

---

# 10. Design Principles

The Core Layer follows these architectural rules.

## Rule 1

Business logic belongs inside generators.

---

## Rule 2

Configuration is immutable during execution.

---

## Rule 3

Randomness is provided only by the Random Manager.

---

## Rule 4

Generators never instantiate other generators.

---

## Rule 5

Engines communicate only through Runtime Context.

---

## Rule 6

The Simulation Engine orchestrates but never generates business entities.

---

## Rule 7

Validation occurs before export.

---

## Rule 8

All runtime events should be logged.

---

# References

- core_master_spec.md
- dependency_graph.md
- simulation_pipeline.md
- engine_contract.md
- abstract_generator.md
- validation_contract.md
