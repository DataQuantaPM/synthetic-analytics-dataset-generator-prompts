# Synthetic SaaS User Behavior Simulator v2.0

# Module Dependency

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Dependency Philosophy
3. High-Level Dependency Graph
4. Module Dependency Matrix
5. Module Responsibilities
6. Allowed Dependency Rules
7. Forbidden Dependencies
8. Dependency Injection Principles
9. Layering Rules
10. Future Extensions
11. References

---

# 1. Purpose

This document defines dependency relationships between all modules within the simulator.

Its objectives are:

- Prevent circular dependencies
- Simplify testing
- Improve maintainability
- Support modular development

---

# 2. Dependency Philosophy

The simulator follows a unidirectional dependency model.

Modules may only depend on lower-level modules.

Higher-level modules orchestrate lower-level modules but never the reverse.

Every dependency should be explicit.

---

# 3. High-Level Dependency Graph

                        Configuration
                              │
                              ▼
                          Core Engine
                              │
      ┌───────────────────────┼───────────────────────┐
      ▼                       ▼                       ▼
     Users                Scenarios              Lifecycle
      │                       │                       │
      └───────────────┬───────────────┬───────────────┘
                      ▼
                  Sessions
                      │
                      ▼
                    Events
                      │
          ┌───────────┴─────────────┐
          ▼                         ▼
   Subscription                 Revenue
          │                         │
          └───────────────┬─────────┘
                          ▼
                    Dirty Data Engine
                          ▼
                    Validation Engine
                          ▼
                      Export Engine

---

# 4. Module Dependency Matrix

| Module | Depends On | Used By |
|----------|------------|---------|
| Config | None | All |
| Core | Config | All Engines |
| Users | Config | Persona, Lifecycle |
| Personas | Users | Hidden Variables |
| Hidden Variables | Personas | Lifecycle |
| Scenarios | Hidden Variables | Lifecycle |
| Lifecycle | Users, Hidden Variables, Scenarios | Sessions, Subscription |
| Sessions | Lifecycle | Events |
| Events | Sessions, Lifecycle | Validation |
| Subscription | Lifecycle | Revenue |
| Revenue | Subscription | Validation |
| Dirty Data | Events, Revenue | Validation |
| Validation | All Output Tables | Export |
| Export | Validation | None |

---

# 5. Module Responsibilities

## Config

Responsible for

- Loading YAML
- Validation
- Global settings

---

## Users

Responsible for

- User generation
- Static attributes

---

## Personas

Responsible for

- Persona assignment
- Persona DNA

---

## Hidden Variables

Responsible for

- Behavioral variables

---

## Scenarios

Responsible for

- Business scenario assignment
- Probability modifiers

---

## Lifecycle

Responsible for

- State transitions
- Weekly progression

---

## Sessions

Responsible for

- Session generation

---

## Events

Responsible for

- Product events

---

## Subscription

Responsible for

- Trial
- Upgrade
- Renewal
- Cancellation

---

## Revenue

Responsible for

- Billing
- Revenue records

---

## Dirty Data

Responsible for

- Injecting configurable data issues

---

## Validation

Responsible for

- Structural validation
- Business validation
- Statistical validation

---

## Export

Responsible for

- CSV
- JSON
- Metadata

---

# 6. Allowed Dependency Rules

Every module may only import modules listed below.

| Module | Allowed Imports |
|----------|----------------|
| Users | Config, Utils |
| Personas | Users, Utils |
| Hidden Variables | Personas, Utils |
| Scenarios | Hidden Variables |
| Lifecycle | Users, Hidden Variables, Scenarios |
| Sessions | Lifecycle |
| Events | Sessions, Lifecycle |
| Subscription | Lifecycle |
| Revenue | Subscription |
| Dirty Data | Events, Revenue |
| Validation | All Output Objects |
| Export | Validation |

---

# 7. Forbidden Dependencies

The following dependencies are prohibited.

❌ Revenue → Lifecycle

❌ Events → Revenue

❌ Users → Revenue

❌ Sessions → Users

❌ Config → Validation

❌ Validation → Users

❌ Dirty Data → UserGenerator

Modules must never depend on downstream components.

---

# 8. Dependency Injection Principles

The simulator follows constructor dependency injection.

Example

UserGenerator receives

- Config
- RandomManager

rather than creating them internally.

Benefits

- Easier testing
- Reproducibility
- Loose coupling

---

# 9. Layering Rules

The simulator is divided into logical layers.

Layer 1

Configuration

↓

Layer 2

Core Infrastructure

↓

Layer 3

Business Simulation

↓

Layer 4

Data Quality

↓

Layer 5

Validation

↓

Layer 6

Export

Dependencies must always point downward.

---

# 10. Dependency Levels

To maintain a clean, scalable, and testable architecture, every module belongs to a predefined dependency level.

Lower levels provide foundational services, while higher levels orchestrate business workflows.

Dependencies should generally flow from higher levels to lower levels only.

---

## Dependency Hierarchy

Level 0
│
├── Config
└── Utils

↓

Level 1
│
├── Users
└── Personas

↓

Level 2
│
├── Hidden Variables
└── Scenarios

↓

Level 3
│
└── Lifecycle

↓

Level 4
│
├── Sessions
└── Subscription

↓

Level 5
│
├── Events
└── Revenue

↓

Level 6
│
└── Dirty Data

↓

Level 7
│
└── Validation

↓

Level 8
│
└── Export

---

## Dependency Level Matrix

| Level | Modules | Primary Responsibility |
|--------|---------|------------------------|
| Level 0 | Config, Utils | Shared configuration and helper utilities |
| Level 1 | Users, Personas | User initialization and behavioral identity |
| Level 2 | Hidden Variables, Scenarios | Behavioral modeling and business modifiers |
| Level 3 | Lifecycle | Weekly lifecycle simulation and state transitions |
| Level 4 | Sessions, Subscription | Session generation and subscription lifecycle |
| Level 5 | Events, Revenue | Product events and revenue generation |
| Level 6 | Dirty Data | Controlled injection of data quality issues |
| Level 7 | Validation | Business and structural validation |
| Level 8 | Export | Final dataset serialization and reporting |

---

## Dependency Rules

The following architectural rules apply:

- Dependencies should always point from higher layers toward lower layers.
- Lower-level modules must never import higher-level modules.
- Modules should communicate through well-defined interfaces or data contracts.
- Shared functionality should reside in `Utils` rather than creating cross-module dependencies.
- Configuration must be loaded exclusively through the `Config` module.
- Business rules must never be implemented inside utility modules.

---

## Valid Dependency Examples

✓ Lifecycle → Hidden Variables

✓ Lifecycle → Scenarios

✓ SessionEngine → Lifecycle

✓ EventEngine → SessionEngine

✓ RevenueEngine → SubscriptionEngine

✓ ValidationEngine → Events

✓ ExportEngine → ValidationEngine

---

## Invalid Dependency Examples

✗ Users → Revenue

✗ Revenue → Users

✗ Revenue → Lifecycle

✗ EventEngine → UserGenerator

✗ Validation → SessionGenerator

✗ Export → Hidden Variables

✗ DirtyData → UserGenerator

These dependencies violate the architectural hierarchy and may introduce circular dependencies or tight coupling.

---

## Architectural Rationale

The dependency hierarchy is designed to achieve the following objectives:

- Maintain loose coupling between business domains.
- Prevent circular imports.
- Enable independent unit testing.
- Improve code readability and maintainability.
- Simplify future feature development.
- Support replacement or extension of individual modules without affecting unrelated components.

Every new module introduced in future versions should be assigned to an appropriate dependency level before implementation.

---

# 11. Future Extensions

Future modules should follow the same dependency rules.

Possible additions

- Organization Engine
- Recommendation Engine
- Marketing Engine
- Experiment Engine
- AI Agent Engine

These modules should integrate without modifying existing dependencies.

---

# 12. References

- architecture.md
- execution_pipeline.md
- project_structure.md
- state_machine.md
