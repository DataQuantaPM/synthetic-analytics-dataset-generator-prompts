# Synthetic SaaS User Behavior Simulator v2.0

# Simulator Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Configuration Philosophy
3. Configuration Hierarchy
4. Simulator Configuration Structure
5. Configuration Sections
6. Runtime Configuration Flow
7. Configuration Validation
8. Configuration Lifecycle
9. Example Configurations
10. References

---

# 1. Purpose

The Simulator Configuration serves as the primary entry point for every simulation.

It defines **what** simulation should be executed, while individual configuration modules define **how** the simulation behaves.

The simulator reads this configuration once at startup before constructing the complete runtime configuration.

---

# 2. Configuration Philosophy

The simulator follows four guiding principles.

## Single Entry Point

All simulations start from a single configuration file.

---

## Separation of Concerns

The simulator configuration does not contain:

- benchmark values
- event probabilities
- dirty data rates
- business rules

Instead, it references dedicated configuration modules.

---

## Reproducibility

Given the same configuration and random seed, the simulator should produce statistically equivalent datasets.

---

## Modularity

Each configuration section can evolve independently without affecting the overall architecture.

---

# 3. Configuration Hierarchy

```text
simulator_config
        │
        ▼
Benchmark Profile
        │
        ▼
Scenario Configuration
        │
        ▼
Probability Configuration
        │
        ▼
Dirty Data Configuration
        │
        ▼
Output Configuration
        │
        ▼
Resolved Configuration
        │
        ▼
Simulation Engine
```

The Simulation Engine always consumes the **Resolved Configuration**, never the raw configuration files.

---

# 4. Simulator Configuration Structure

The simulator configuration is logically divided into the following sections.

| Section | Purpose |
|----------|---------|
| Metadata | Simulation metadata |
| Simulation | Global simulation settings |
| Benchmark | Benchmark profile selection |
| Scenario | Enabled business scenarios |
| Output | Export configuration |
| Randomness | Random seed configuration |

---

# 5. Configuration Sections

## 5.1 Metadata

Describes the simulation itself.

Example:

```yaml
metadata:

  simulation_name: "Balanced SaaS Demo"

  description: "Synthetic Product Analytics Dataset"

  version: "2.0"

  author: "Simulator"

  created_at: auto
```

---

## 5.2 Simulation

Defines global execution parameters.

Example

```yaml
simulation:

  total_users: 12000

  observation_weeks: 12

  benchmark_profile: balanced

  timezone: UTC

  locale: en_US
```

### Parameters

| Parameter | Description |
|------------|-------------|
| total_users | Number of simulated users |
| observation_weeks | Simulation duration |
| benchmark_profile | Active benchmark |
| timezone | Timestamp timezone |
| locale | Localization |

---

## 5.3 Scenario

Enables business scenarios.

Example

```yaml
scenarios:

  enabled:

    - poor_onboarding

    - referral_campaign

    - pricing_increase
```

Multiple scenarios may be enabled simultaneously provided they are compatible.

---

## 5.4 Output

Defines exported artifacts.

```yaml
output:

  csv: true

  parquet: false

  validation_report: true

  qa_report: true

  overwrite_existing: false
```

---

## 5.5 Randomness

Controls reproducibility.

```yaml
random:

  seed: 42

  deterministic: true
```

When deterministic mode is enabled, statistically equivalent datasets can be reproduced.

---

# 6. Runtime Configuration Flow

Simulation configuration is resolved through multiple stages.

```text
simulator_config.yaml
          │
          ▼
Load Benchmark Profile
          │
          ▼
Load Scenario Configuration
          │
          ▼
Load Probability Configuration
          │
          ▼
Load Dirty Data Configuration
          │
          ▼
Apply Runtime Overrides
          │
          ▼
Resolved Configuration
```

Only the final resolved configuration is accessible by generators.

---

# 7. Configuration Validation

Before the simulation starts, the configuration is validated.

## Required Fields

- simulation_name
- benchmark_profile
- total_users
- observation_weeks
- output configuration
- random seed

---

## Validation Rules

| Rule | Expected |
|------|----------|
| total_users > 0 | PASS |
| observation_weeks > 0 | PASS |
| benchmark profile exists | PASS |
| output format supported | PASS |
| seed is integer | PASS |
| scenario names valid | PASS |

Any validation failure prevents the simulation from starting.

---

# 8. Configuration Lifecycle

```text
Read simulator_config
        │
        ▼
Validate Configuration
        │
        ▼
Resolve Dependencies
        │
        ▼
Construct Runtime Config
        │
        ▼
Launch Simulation
```

Configuration is immutable once the simulation begins.

---

# 9. Example Configurations

## Balanced Portfolio Dataset

```yaml
simulation:

  total_users: 12000

  observation_weeks: 12

  benchmark_profile: balanced

scenarios:

  enabled:

    - poor_onboarding

output:

  csv: true

random:

  seed: 42
```

---

## Enterprise SaaS

```yaml
simulation:

  total_users: 8000

  observation_weeks: 26

  benchmark_profile: enterprise

scenarios:

  enabled:

    - long_sales_cycle

output:

  csv: true

random:

  seed: 123
```

---

## Growth SaaS

```yaml
simulation:

  total_users: 20000

  observation_weeks: 16

  benchmark_profile: growth

scenarios:

  enabled:

    - referral_campaign

    - feature_rollout

output:

  csv: true

random:

  seed: 2026
```

---

# References

- benchmark_profiles.md
- scenario_config.md
- probability_config.md
- dirty_data_config.md
- output_config.md
- config_resolution.md
