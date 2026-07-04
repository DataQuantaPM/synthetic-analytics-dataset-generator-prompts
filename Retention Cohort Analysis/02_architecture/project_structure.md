# Synthetic SaaS User Behavior Simulator v2.0

# Project Structure

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Project Organization Principles
3. Repository Structure
4. Source Code Structure
5. Configuration Structure
6. Documentation Structure
7. Output Structure
8. Testing Structure
9. Naming Conventions
10. Design Rules
11. Future Extensions
12. References

---

# 1. Purpose

This document defines the directory layout and organization of the Synthetic SaaS User Behavior Simulator.

A consistent project structure improves maintainability, readability, testing, and future extensibility.

---

# 2. Project Organization Principles

The repository follows several design principles.

- Domain-driven organization
- One responsibility per module
- Configuration separated from implementation
- Documentation-first development
- Testable components
- Reproducible execution

---

# 3. Repository Structure

```text
synthetic-saas-simulator/

│
├── README.md
├── requirements.txt
├── pyproject.toml
├── LICENSE
├── .gitignore
│
├── docs/
│
├── configs/
│
├── src/
│
├── tests/
│
├── outputs/
│
├── notebooks/
│
└── scripts/
```

---

# 4. Source Code Structure

```text
src/

├── core/
│   ├── simulator.py
│   ├── pipeline.py
│   ├── random_manager.py
│   ├── logger.py
│   └── context.py
│
├── config/
│   ├── loader.py
│   ├── validator.py
│   └── models.py
│
├── users/
│   ├── generator.py
│   ├── personas.py
│   ├── hidden_variables.py
│   └── models.py
│
├── lifecycle/
│   ├── state_machine.py
│   ├── transition_engine.py
│   └── timeline.py
│
├── sessions/
│   ├── generator.py
│   ├── duration.py
│   └── timestamp.py
│
├── events/
│   ├── generator.py
│   ├── event_catalog.py
│   └── validator.py
│
├── subscriptions/
│   ├── engine.py
│   ├── billing.py
│   ├── renewal.py
│   └── pricing.py
│
├── revenue/
│   ├── engine.py
│   ├── mrr.py
│   └── metrics.py
│
├── scenarios/
│   ├── engine.py
│   ├── modifiers.py
│   └── assignment.py
│
├── dirty_data/
│   ├── injector.py
│   ├── duplicates.py
│   ├── missing_values.py
│   ├── timestamp_drift.py
│   └── inconsistent_labels.py
│
├── validation/
│   ├── structural.py
│   ├── business.py
│   ├── statistical.py
│   ├── quality.py
│   └── report.py
│
├── export/
│   ├── csv_exporter.py
│   ├── json_exporter.py
│   └── metadata.py
│
└── utils/
    ├── dates.py
    ├── probability.py
    ├── random.py
    └── helpers.py
```

---

# 5. Configuration Structure

```text
configs/

├── simulation.yaml
├── personas.yaml
├── pricing.yaml
├── scenarios.yaml
├── dirty_data.yaml
└── validation.yaml
```

All business behavior should be configurable without modifying source code.

---

# 6. Documentation Structure

```text
docs/

├── 01_simulation/
├── 02_architecture/
├── 03_business/
├── 04_api/
├── 05_examples/
└── diagrams/
```

Documentation is treated as a first-class component of the project.

---

# 7. Output Structure

```text
outputs/

├── clean/
│   ├── users.csv
│   ├── sessions.csv
│   ├── events.csv
│   ├── subscriptions.csv
│   └── revenue.csv
│
├── dirty/
│   ├── events_dirty.csv
│   └── users_dirty.csv
│
├── metadata/
│   ├── simulation.json
│   └── qa_report.json
│
└── logs/
    └── execution.log
```

---

# 8. Testing Structure

```text
tests/

├── unit/
├── integration/
├── validation/
├── performance/
└── fixtures/
```

Every major engine should include corresponding unit tests.

---

# 9. Naming Conventions

## Files

snake_case

Example

user_generator.py

---

## Classes

PascalCase

Example

UserGenerator

---

## Functions

snake_case

Example

generate_users()

---

## Variables

snake_case

Example

engagement_score

---

## Constants

UPPER_CASE

Example

MAX_TRIAL_DAYS

---

# 10. Design Rules

The project follows these rules.

- No circular imports.
- One public class per module where practical.
- Business logic must not appear in utility modules.
- Engines communicate only through defined data contracts.
- Configuration values must never be hardcoded.
- Random number generation must be centralized.

---

# 11. Future Extensions

The architecture is designed to support future modules such as:

- Organization Engine
- Experiment Engine
- Recommendation Engine
- AI Agent Simulation
- Multi-product Workspaces
- API Export
- DuckDB Export
- Real-time Event Streaming

These additions should not require restructuring the repository.

---

# 12. References

- architecture.md
- execution_pipeline.md
- module_dependency.md
