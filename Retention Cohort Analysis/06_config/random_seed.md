# Synthetic SaaS User Behavior Simulator v2.0

# Random Seed Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Random Engine Architecture
4. Randomness Scope
5. Configuration Structure
6. Random Stream Management
7. Reproducibility
8. Validation Rules
9. Example Configuration
10. References

---

# 1. Purpose

Random Seed Configuration controls all stochastic behavior throughout the simulation.

Its primary goals are to:

- ensure reproducibility
- isolate independent random processes
- guarantee statistically equivalent simulations
- support deterministic testing

Rather than relying on uncontrolled randomness, every random decision is derived from managed random streams.

---

# 2. Design Principles

## Reproducible

The same configuration and random seed should produce statistically equivalent datasets.

---

## Independent

Different simulation modules should not share the same random sequence.

---

## Deterministic

When deterministic mode is enabled, repeated executions generate identical outputs.

---

## Isolated

Each generator owns its own random stream.

---

## Auditable

The simulator records the seed and random configuration used for every simulation.

---

# 3. Random Engine Architecture

```text
Master Seed
      │
      ▼
Random Manager
      │
      ├── User Generator
      ├── Session Generator
      ├── Event Generator
      ├── Revenue Generator
      ├── Retention Generator
      ├── Dirty Data Engine
      └── Validation Engine
```

Every module receives its own independent random stream.

The master seed is never used directly by generators.

---

# 4. Randomness Scope

Randomness affects multiple parts of the simulator.

| Module | Examples |
|----------|----------|
| User Generator | Persona assignment, acquisition source |
| Session Generator | Session count, session timing |
| Event Generator | Event occurrence, event timing |
| Subscription Generator | Trial, upgrade, cancellation |
| Revenue Generator | Payment success, renewal |
| Retention Generator | Weekly return behavior |
| Dirty Data Engine | Duplicate rows, missing values |
| Scenario Engine | Scenario-specific randomness |

Each module consumes only its own random stream.

---

# 5. Configuration Structure

The Random Configuration follows a common schema.

```yaml
random:

  seed:

  deterministic:

  stream_strategy:

  save_seed:

  save_stream_metadata:
```

---

## Seed

Master seed used to initialize the Random Manager.

```yaml
seed:

  42
```

---

## Deterministic Mode

Controls reproducibility.

```yaml
deterministic:

  true
```

When enabled, identical configurations produce identical datasets.

---

## Stream Strategy

Defines how module-specific streams are created.

```yaml
stream_strategy:

  independent
```

Supported strategies

- independent
- shared

Independent streams are recommended.

---

## Save Seed

Stores the seed in simulation metadata.

```yaml
save_seed:

  true
```

---

## Save Stream Metadata

Stores information about generated random streams.

```yaml
save_stream_metadata:

  true
```

---

# 6. Random Stream Management

The Random Manager derives independent streams from the master seed.

```text
Master Seed
      │
      ├── User RNG
      ├── Session RNG
      ├── Event RNG
      ├── Subscription RNG
      ├── Revenue RNG
      ├── Dirty Data RNG
      └── Validation RNG
```

This prevents unrelated modules from influencing one another.

For example, changing duplicate-event generation should not affect subscription behavior.

---

# 7. Reproducibility

The simulator supports two execution modes.

## Deterministic Mode

Characteristics

- Fixed seed
- Independent streams
- Repeatable datasets
- Recommended for testing

---

## Stochastic Mode

Characteristics

- Automatically generated seed
- Independent streams
- Different dataset every execution
- Recommended for experimentation

---

Example

```yaml
random:

  seed: auto

  deterministic: false
```

---

# 8. Validation Rules

Before simulation starts, the Random Manager validates the configuration.

| Rule | Expected |
|--------|----------|
| Seed is integer or auto | PASS |
| Deterministic flag valid | PASS |
| Stream strategy supported | PASS |
| Metadata flags valid | PASS |

Any failed validation prevents simulation startup.

---

# 9. Example Configuration

## Deterministic Simulation

```yaml
random:

  seed: 42

  deterministic: true

  stream_strategy: independent

  save_seed: true

  save_stream_metadata: true
```

---

## Randomized Simulation

```yaml
random:

  seed: auto

  deterministic: false

  stream_strategy: independent

  save_seed: true

  save_stream_metadata: false
```

---

# References

- simulator_config.md
- output_config.md
- config_resolution.md
- validation.md
