# Synthetic SaaS User Behavior Simulator v2.0

# User Generator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. User Generation Model
7. Generation Workflow
8. User Attributes
9. Identifier Strategy
10. Distribution Strategy
11. Generation Rules
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The User Generator is the first simulation engine responsible for creating the base user population.

It establishes immutable user identities and assigns static profile attributes that remain constant throughout the simulation.

The generated users become the foundation for all subsequent simulation engines.

---

# 2. Responsibilities

The User Generator is responsible for:

- generating unique users
- assigning immutable user identifiers
- generating signup dates
- assigning demographic attributes
- assigning acquisition sources
- assigning initial subscription plans
- publishing the User Dataset

The User Generator is **not** responsible for:

- personas
- behavioral traits
- lifecycle states
- sessions
- events
- subscriptions
- revenue
- retention
- churn

Those responsibilities belong to downstream engines.

---

# 3. Engine Position

```text
Simulation Context

↓

User Generator

↓

User Dataset

↓

Persona Engine
```

The User Generator is always executed first.

---

# 4. Inputs

Runtime Context

Contains

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

User Dataset

Published to

Simulation Context

The User Dataset becomes the source of truth for all downstream engines.

---

# 6. User Generation Model

Users are generated independently before any behavioral simulation begins.

Each user represents a unique SaaS customer.

Only immutable attributes are assigned during this stage.

Behavioral characteristics are introduced later by the Persona Engine and Hidden Variable Engine.

---

# 7. Generation Workflow

```text
Read Configuration

↓

Determine Target User Count

↓

Generate User IDs

↓

Assign Signup Dates

↓

Assign Country

↓

Assign Device

↓

Assign Acquisition Source

↓

Assign Initial Plan

↓

Publish User Dataset
```

---

# 8. User Attributes

Each generated user contains the following baseline attributes.

| Attribute | Description |
|----------|-------------|
| user_id | Globally unique identifier |
| signup_date | Account creation date |
| acquisition_source | Initial traffic source |
| country | User country |
| device_type | Desktop / Mobile / Tablet |
| initial_plan | Free or Paid entry plan |
| company_size | Optional B2B segmentation |
| created_at | Simulation timestamp |

These attributes are immutable after generation.

---

# 9. Identifier Strategy

User identifiers follow a deterministic format.

Example

```
U000001
U000002
U000003
```

Requirements

- globally unique
- deterministic
- reproducible
- human-readable

Identifiers are never reused.

---

# 10. Distribution Strategy

User attributes are sampled according to configured benchmark profiles.

Examples include:

### Acquisition Source

- Organic
- Paid Ads
- Referral
- Direct
- Social

### Country

Distribution follows the configured geographic profile.

### Device

Typical distribution

- Mobile
- Desktop
- Tablet

### Initial Plan

Typical plans

- Free
- Starter
- Pro
- Enterprise

All distributions are configuration-driven.

---

# 11. Generation Rules

The User Generator ensures:

- every user has a unique identifier
- required attributes are populated
- signup dates fall within the simulation period
- configured distributions are respected
- no behavioral information is generated
- users are reproducible using the configured random seed

The generator never creates:

- sessions
- events
- purchases
- subscriptions
- lifecycle states

---

# 12. Runtime Metrics

Recorded metrics include:

- users generated
- signup date distribution
- acquisition source distribution
- country distribution
- device distribution
- plan distribution
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- Simulator Configuration
- Random Manager

Produces

- User Dataset

Publishes

Simulation Context

Returns

EngineResult

---

# 14. References

- simulation_master_spec.md
- generator_master_spec.md
- config_master_spec.md
- benchmark_profiles.md
- scenario_config.md
- probability_config.md
- engine_contract.md
