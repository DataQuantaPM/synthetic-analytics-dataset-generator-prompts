# Synthetic SaaS User Behavior Simulator v2.0

# Core Engine Master Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Core Philosophy
3. Core Layer Overview
4. Core Components
5. Design Principles
6. Execution Lifecycle
7. Core Dependency Rules
8. Engine Communication
9. Extension Strategy
10. References

---

# 1. Purpose

The Core Layer contains the executable simulation engine responsible for transforming business rules, configurations, and probabilistic models into a complete synthetic SaaS dataset.

It is the operational heart of the simulator.

Unlike previous layers, which define *what* should happen, the Core Layer defines *how* it happens.

---

# 2. Core Philosophy

The simulator follows five architectural principles.

## Configuration-Driven

Core components never hardcode business logic.

All behavior originates from resolved configuration.

---

## Stateless Components

Generators should avoid shared mutable state whenever possible.

Each component receives explicit inputs and produces explicit outputs.

---

## Modular

Every engine performs exactly one responsibility.

No engine should implement multiple business domains.

---

## Deterministic

Given the same Resolved Configuration and Random Seed, the Core Layer should produce statistically equivalent datasets.

---

## Extensible

New generators and engines should be added without modifying existing implementations.

---

# 3. Core Layer Overview

```text
Resolved Configuration
          │
          ▼
Simulation Engine
          │
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

The Simulation Engine orchestrates execution but does not generate business entities itself.

---

# 4. Core Components

| Component | Responsibility |
|-----------|----------------|
| Simulation Engine | Coordinates execution |
| Config Resolver | Supplies resolved configuration |
| Random Manager | Provides random streams |
| Generator Modules | Generate business entities |
| Validation Engine | Validates generated datasets |
| Dirty Data Engine | Injects controlled imperfections |
| Output Engine | Writes artifacts |
| Runtime Context | Shares execution metadata |

Each component owns one primary responsibility.

---

# 5. Design Principles

## Single Responsibility

Each engine has one purpose.

---

## Dependency Injection

Core components receive dependencies through constructors or interfaces rather than creating them internally.

---

## Loose Coupling

Generators communicate through contracts, not direct references.

---

## Immutable Configuration

Resolved Configuration is read-only throughout execution.

---

## Observable Execution

Every major step should produce logs and execution metrics.

---

# 6. Execution Lifecycle

The Core Layer follows a deterministic execution sequence.

```text
Load Resolved Configuration
        │
        ▼
Initialize Runtime Context
        │
        ▼
Initialize Random Manager
        │
        ▼
Initialize Engines
        │
        ▼
Execute Generators
        │
        ▼
Inject Dirty Data
        │
        ▼
Run Validation
        │
        ▼
Generate Outputs
        │
        ▼
Complete Simulation
```

Each stage must complete successfully before the next begins.

---

# 7. Core Dependency Rules

The Core Layer follows strict dependency rules.

1. Engines depend on interfaces, not implementations.
2. Generators never instantiate other generators.
3. Randomness is supplied only by the Random Manager.
4. Configuration is supplied only by the Config Resolver.
5. Output is handled only by the Output Engine.
6. Validation occurs after generation and before export.

These rules ensure a Directed Acyclic Graph (DAG) across the Core Layer.

---

# 8. Engine Communication

Core components exchange information through contracts.

```text
ResolvedConfig
        │
        ▼
Simulation Engine
        │
        ▼
Runtime Context
        │
        ├── User Generator
        ├── Session Generator
        ├── Event Generator
        ├── Subscription Generator
        ├── Revenue Generator
        ├── Retention Generator
        └── Dirty Data Engine
```

Direct communication between generators is discouraged.

Instead, shared state is mediated through the Runtime Context.

---

# 9. Extension Strategy

The Core Layer is designed for future growth.

New capabilities should be added by introducing new components rather than modifying existing ones.

Examples include:

- Cohort Generator
- Feature Flag Engine
- Experiment Engine
- Notification Generator
- Recommendation Engine

Extensions must conform to existing engine contracts.

---

# References

- config_relationship.md
- architecture.md
- dependency_graph.md
- simulation_pipeline.md
- engine_contract.md
- abstract_generator.md
- validation_contract.md
