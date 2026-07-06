# Synthetic SaaS User Behavior Simulator v2.0

# Persona Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Persona Model
7. Generation Workflow
8. Persona Attributes
9. Persona Assignment Strategy
10. Distribution Strategy
11. Generation Rules
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Persona Engine enriches each generated user with a realistic customer persona.

A persona represents stable behavioral characteristics that influence customer decisions throughout the entire simulation.

Unlike demographic attributes, personas describe why users behave differently even when they share similar profiles.

Personas become the behavioral foundation for downstream simulation engines.

---

# 2. Responsibilities

The Persona Engine is responsible for:

- assigning customer personas
- generating stable behavioral profiles
- enriching User Blueprints
- publishing Persona Profiles

The Persona Engine is **not** responsible for:

- hidden variables
- lifecycle progression
- activity generation
- session generation
- event generation
- subscriptions
- revenue
- retention
- churn

---

# 3. Engine Position

```text
User Generator

↓

Persona Engine

↓

Hidden Variable Engine
```

The Persona Engine executes immediately after the User Generator.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration

- simulator_config
- scenario_config
- benchmark_profiles
- probability_config

---

# 5. Outputs

Primary Output

Persona Profiles

Published to

Simulation Context

Each User Blueprint is enriched with persona attributes.

---

# 6. Persona Model

A persona represents long-term customer characteristics.

Unlike lifecycle states, personas never change during a simulation.

Each persona influences future behavioral probabilities but does not directly generate behavior.

Behavior is generated later through Hidden Variables and downstream engines.

---

# 7. Generation Workflow

```text
Load User Dataset

↓

Read Persona Distribution

↓

Select Persona

↓

Assign Persona Attributes

↓

Enrich User Blueprint

↓

Publish Persona Profiles
```

---

# 8. Persona Attributes

Each persona contains stable behavioral characteristics.

| Attribute | Description |
|-----------|-------------|
| persona_name | Persona identifier |
| role | Customer role |
| company_type | Startup / SMB / Enterprise |
| company_size | Organization size |
| technical_level | Low / Medium / High |
| budget_level | Low / Medium / High |
| decision_speed | Slow / Medium / Fast |
| price_sensitivity | Low / Medium / High |
| feature_preference | Primary product interest |
| collaboration_style | Individual / Team |

These attributes remain constant throughout the simulation.

---

# 9. Persona Assignment Strategy

Personas are assigned probabilistically based on configured benchmark profiles.

Example personas include:

- Startup Founder
- Product Manager
- Marketing Manager
- Sales Representative
- Software Engineer
- Freelancer
- Student
- Enterprise Executive

The available persona catalog is configuration-driven.

---

# 10. Distribution Strategy

Persona distributions are configurable.

Distribution may depend on:

- acquisition source
- country
- company size
- subscription entry plan
- simulation scenario

Example

| Acquisition Source | Common Persona |
|--------------------|----------------|
| Organic | Product Manager |
| Referral | Startup Founder |
| Paid Ads | Marketing Manager |
| Direct | Enterprise Executive |

Conditional probabilities are defined in configuration files.

---

# 11. Generation Rules

The Persona Engine ensures:

- every user receives exactly one persona
- personas remain immutable
- configured distributions are respected
- persona assignment is reproducible using the configured random seed
- personas enrich existing User Blueprints

The Persona Engine never:

- changes user identities
- creates lifecycle states
- generates behavioral events
- modifies previous engine outputs

---

# 12. Runtime Metrics

Recorded metrics include:

- personas assigned
- persona distribution
- role distribution
- company size distribution
- budget distribution
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- User Dataset
- Random Manager

Produces

- Persona Profiles

Publishes

Simulation Context

Returns

EngineResult

---

# 14. References

- simulation_master_spec.md
- user_generator.md
- generator_master_spec.md
- benchmark_profiles.md
- probability_config.md
- engine_contract.md
