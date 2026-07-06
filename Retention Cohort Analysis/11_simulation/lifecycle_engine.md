# Synthetic SaaS User Behavior Simulator v2.0

# Lifecycle Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Lifecycle Model
7. Generation Workflow
8. Lifecycle States
9. State Transition Model
10. Decision Strategy
11. Lifecycle Rules
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Lifecycle Engine determines each user's business journey throughout the simulation.

Using personas, hidden variables, benchmark profiles, and scenario configurations, the engine generates a deterministic customer lifecycle representing how users progress through the SaaS funnel.

The generated lifecycle becomes the foundation for all downstream behavioral simulation.

---

# 2. Responsibilities

The Lifecycle Engine is responsible for:

- determining customer lifecycle progression
- generating lifecycle states
- assigning milestone timestamps
- enriching User Blueprints
- publishing Lifecycle Profiles

The Lifecycle Engine is **not** responsible for:

- generating weekly activity
- sessions
- events
- subscriptions
- revenue
- retention metrics
- churn events

Those responsibilities belong to downstream engines.

---

# 3. Engine Position

```text
Hidden Variable Engine

↓

Lifecycle Engine

↓

Weekly Activity Engine
```

The Lifecycle Engine executes after hidden variables have been generated.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration

- probability_config
- benchmark_profiles
- scenario_config

---

# 5. Outputs

Primary Output

Lifecycle Profiles

Published to

Simulation Context

Each User Blueprint is enriched with lifecycle information.

---

# 6. Lifecycle Model

The Lifecycle Engine models customer progression through predefined business states.

Lifecycle progression is influenced by:

- hidden variables
- persona
- acquisition source
- scenario modifiers
- benchmark probabilities

Lifecycle generation is deterministic under identical random seeds.

---

# 7. Generation Workflow

```text
Load User Blueprint

↓

Read Lifecycle Configuration

↓

Calculate Transition Probabilities

↓

Determine Lifecycle Path

↓

Generate Milestone Dates

↓

Validate State Sequence

↓

Enrich User Blueprint

↓

Publish Lifecycle Profiles
```

---

# 8. Lifecycle States

Typical lifecycle states include:

| State | Description |
|---------|-------------|
| Signup | User created account |
| Email Verified | Email successfully verified |
| Onboarding Started | User begins onboarding |
| Onboarding Completed | User finishes onboarding |
| Activated | User reaches activation milestone |
| Trial Started | User begins free trial |
| Trial Completed | Trial period ends |
| Paid | User becomes paying customer |
| Retained | User remains active customer |
| Churned | User exits the product |

Additional states may be introduced through configuration.

---

# 9. State Transition Model

Lifecycle states follow a directed state machine.

```text
Signup

↓

Email Verified

↓

Onboarding Started

↓

Onboarding Completed

↓

Activated

↓

Trial Started

↓

Paid

↓

Retained

↓

Churned
```

State transitions are forward-only unless explicitly defined by future simulation extensions.

Invalid transitions are prohibited.

---

# 10. Decision Strategy

Lifecycle decisions are based on multiple inputs.

Primary factors include:

- activation affinity
- engagement score
- purchase affinity
- product fit score
- churn risk score
- scenario modifiers
- benchmark probabilities

The engine combines these factors to determine state transitions.

No single variable determines lifecycle progression.

---

# 11. Lifecycle Rules

The Lifecycle Engine ensures:

- every user starts at Signup
- lifecycle progression follows the configured state machine
- milestone timestamps remain chronological
- lifecycle states are internally consistent
- lifecycle generation is reproducible

The engine never:

- creates events
- generates sessions
- modifies personas
- modifies hidden variables
- generates revenue

---

# 12. Runtime Metrics

Recorded metrics include:

- lifecycle profiles generated
- activation rate
- trial rate
- paid conversion rate
- retention distribution
- churn distribution
- state transition counts
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- Random Manager

Produces

- Lifecycle Profiles

Publishes

Simulation Context

Returns

EngineResult

---

# 14. References

- simulation_master_spec.md
- hidden_variable_engine.md
- state_machine.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
