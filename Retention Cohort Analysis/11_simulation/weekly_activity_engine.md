# Synthetic SaaS User Behavior Simulator v2.0

# Weekly Activity Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Weekly Activity Model
7. Generation Workflow
8. Activity Profile
9. Activity Generation Strategy
10. Activity Rules
11. Runtime Metrics
12. Engine Contract
13. References

---

# 1. Purpose

The Weekly Activity Engine determines user engagement patterns across the simulation period.

Rather than generating sessions directly, the engine first decides whether users are active during each simulation week.

These activity decisions become the foundation for downstream Session and Event generation.

---

# 2. Responsibilities

The Weekly Activity Engine is responsible for:

- generating weekly activity states
- determining active and inactive weeks
- calculating engagement intensity
- enriching User Blueprints
- publishing Weekly Activity Profiles

The Weekly Activity Engine is **not** responsible for:

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
Lifecycle Engine

↓

Weekly Activity Engine

↓

Session Engine
```

The Weekly Activity Engine executes after lifecycle generation.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- Lifecycle Profiles
- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration

- simulator_config
- probability_config
- scenario_config
- benchmark_profiles

---

# 5. Outputs

Primary Output

Weekly Activity Profiles

Published to

Simulation Context

Each User Blueprint is enriched with weekly engagement information.

---

# 6. Weekly Activity Model

Weekly activity represents whether a user interacts with the product during a given simulation week.

Each simulation week contains an independent activity decision influenced by previous engagement history and user characteristics.

Weekly activity is generated before sessions and events.

---

# 7. Generation Workflow

```text
Load Lifecycle Profiles

↓

Determine Simulation Weeks

↓

Calculate Weekly Activity Probability

↓

Generate Weekly Activity Timeline

↓

Assign Engagement Intensity

↓

Validate Weekly Timeline

↓

Enrich User Blueprint

↓

Publish Weekly Activity Profiles
```

---

# 8. Activity Profile

Each user receives a weekly activity timeline.

Typical attributes include:

| Attribute | Description |
|------------|-------------|
| simulation_week | Week index |
| is_active | User active during the week |
| engagement_level | Low / Medium / High |
| expected_sessions | Estimated sessions for the week |
| expected_active_days | Estimated active days |
| activity_score | Weekly activity intensity |

These values are consumed by the Session Engine.

---

# 9. Activity Generation Strategy

Weekly activity depends on multiple factors.

Primary inputs include:

- lifecycle state
- engagement score
- product fit score
- churn risk
- purchase affinity
- scenario modifiers
- benchmark profiles

Typical examples

### Activated users

Higher weekly activity.

### Trial users

Highest activity.

### Paid users

Stable activity.

### Churned users

No future activity.

Weekly probabilities are configuration-driven.

---

# 10. Activity Rules

The Weekly Activity Engine ensures:

- activity begins after signup
- users cannot be active before account creation
- churned users generate no future activity
- activity follows lifecycle progression
- engagement intensity remains within configured limits
- weekly generation is reproducible

The engine never:

- generates sessions
- creates events
- changes lifecycle states
- modifies hidden variables

---

# 11. Runtime Metrics

Recorded metrics include:

- weekly activity profiles generated
- weekly active users
- average engagement level
- average active weeks
- expected sessions
- inactive week distribution
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 12. Engine Contract

Input

RuntimeContext

Consumes

- Lifecycle Profiles
- Hidden Variable Profiles
- Random Manager

Produces

- Weekly Activity Profiles

Publishes

Simulation Context

Returns

EngineResult

---

# 13. References

- simulation_master_spec.md
- lifecycle_engine.md
- hidden_variable_engine.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
