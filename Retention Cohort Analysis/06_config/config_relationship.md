# Synthetic SaaS User Behavior Simulator v2.0

# Configuration Relationship

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Configuration Overview
3. Configuration Dependency Graph
4. Configuration Responsibilities
5. Configuration Read Flow
6. Configuration Dependency Matrix
7. Configuration Ownership
8. Configuration Lifecycle
9. Configuration Rules
10. References

---

# 1. Purpose

This document describes how configuration modules interact within the simulator.

Rather than defining configuration values, it explains:

- configuration dependencies
- ownership
- execution order
- data flow
- responsibilities

It serves as the architectural reference for the Configuration Layer.

---

# 2. Configuration Overview

The Configuration Layer consists of seven independent modules.

```text
06_config/

├── simulator_config.md
├── benchmark_profiles.md
├── scenario_config.md
├── probability_config.md
├── dirty_data_config.md
├── output_config.md
├── random_seed.md
```

Each module has a single responsibility.

No configuration module should duplicate another.

---

# 3. Configuration Dependency Graph

```text
                   simulator_config
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
 benchmark_profiles   scenario_config   random_seed
        │                 │
        └────────────┬────┘
                     ▼
          probability_config
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
 dirty_data_config          output_config
                     │
                     ▼
              Resolved Config
                     │
                     ▼
             Simulation Engine
```

The Simulation Engine interacts only with the final **Resolved Configuration**.

---

# 4. Configuration Responsibilities

| Configuration | Primary Responsibility |
|--------------|------------------------|
| simulator_config | Selects simulation settings |
| benchmark_profiles | Defines business targets |
| scenario_config | Modifies business behavior |
| probability_config | Defines executable probabilities |
| dirty_data_config | Controls data quality injection |
| output_config | Controls exported artifacts |
| random_seed | Controls stochastic behavior |

Each configuration module owns exactly one concern.

---

# 5. Configuration Read Flow

Configuration files are loaded in a deterministic order.

```text
1. simulator_config

        ↓

2. benchmark_profiles

        ↓

3. scenario_config

        ↓

4. probability_config

        ↓

5. dirty_data_config

        ↓

6. output_config

        ↓

7. random_seed

        ↓

Resolved Configuration
```

No configuration should be loaded out of sequence.

---

# 6. Configuration Dependency Matrix

| Configuration | Reads | Used By |
|---------------|-------|---------|
| simulator_config | None | Config Resolver |
| benchmark_profiles | simulator_config | Probability Resolver |
| scenario_config | simulator_config | Scenario Engine |
| probability_config | benchmark_profiles, scenario_config | All Generators |
| dirty_data_config | simulator_config | Dirty Data Engine |
| output_config | simulator_config | Output Engine |
| random_seed | simulator_config | Random Manager |

This matrix documents direct configuration dependencies only.

---

# 7. Configuration Ownership

Each configuration module is owned by a single subsystem.

| Module | Owner |
|---------|-------|
| simulator_config | Config Manager |
| benchmark_profiles | Benchmark Manager |
| scenario_config | Scenario Engine |
| probability_config | Probability Resolver |
| dirty_data_config | Dirty Data Engine |
| output_config | Output Engine |
| random_seed | Random Manager |

Ownership prevents configuration conflicts.

---

# 8. Configuration Lifecycle

```text
Read Configuration

        │

        ▼

Validate

        │

        ▼

Resolve Dependencies

        │

        ▼

Construct Resolved Configuration

        │

        ▼

Freeze Configuration

        │

        ▼

Simulation Starts
```

Configuration becomes immutable after the simulation begins.

---

# 9. Configuration Rules

The Configuration Layer follows these architectural rules.

## Rule 1

Configuration modules may reference other modules but must not modify them.

---

## Rule 2

Only the Config Resolver may combine multiple configuration modules.

---

## Rule 3

Generators never read raw configuration files directly.

They consume only the Resolved Configuration.

---

## Rule 4

Configuration values must never be hardcoded inside generators.

---

## Rule 5

Every configuration module must pass validation before resolution.

---

## Rule 6

Configuration modules are immutable during simulation execution.

---

# References

- simulator_config.md
- benchmark_profiles.md
- scenario_config.md
- probability_config.md
- dirty_data_config.md
- output_config.md
- random_seed.md
- config_resolution.md
