# Synthetic SaaS User Behavior Simulator v2.0

# Hidden Variable Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Hidden Variable Model
7. Generation Workflow
8. Hidden Variables
9. Generation Strategy
10. Influence Model
11. Generation Rules
12. Runtime Metrics
13. Engine Contract
14. References

---

# 1. Purpose

The Hidden Variable Engine generates latent behavioral characteristics that cannot be directly observed but influence customer decisions throughout the simulation.

These variables represent internal customer tendencies such as motivation, engagement, product fit, and purchase readiness.

Hidden variables are immutable during a simulation and become the primary inputs for downstream behavioral engines.

---

# 2. Responsibilities

The Hidden Variable Engine is responsible for:

- generating latent behavioral variables
- enriching User Blueprints
- publishing Hidden Variable Profiles

The Hidden Variable Engine is **not** responsible for:

- lifecycle progression
- weekly activity
- sessions
- events
- subscriptions
- revenue
- retention
- churn

Behavior is generated later using these latent variables.

---

# 3. Engine Position

```text
Persona Engine

↓

Hidden Variable Engine

↓

Lifecycle Engine
```

The Hidden Variable Engine executes immediately after persona assignment.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
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

Hidden Variable Profiles

Published to

Simulation Context

Each User Blueprint is enriched with hidden behavioral variables.

---

# 6. Hidden Variable Model

Hidden variables represent intrinsic customer characteristics.

Unlike events or lifecycle states, hidden variables are never directly exposed in the generated datasets.

Instead, they influence downstream probability calculations.

They remain constant throughout a simulation unless explicitly overridden by future simulator versions.

---

# 7. Generation Workflow

```text
Load Persona Profiles

↓

Read Hidden Variable Configuration

↓

Sample Latent Variables

↓

Apply Persona Bias

↓

Validate Variable Ranges

↓

Enrich User Blueprint

↓

Publish Hidden Variable Profiles
```

---

# 8. Hidden Variables

Typical hidden variables include:

| Variable | Description |
|----------|-------------|
| engagement_score | Overall engagement tendency |
| activation_affinity | Likelihood of completing onboarding |
| product_fit_score | Product-market fit for the user |
| purchase_affinity | Natural tendency to purchase |
| churn_risk_score | Intrinsic churn tendency |
| feature_curiosity | Interest in exploring product features |
| learning_speed | Speed of product adoption |
| budget_readiness | Financial readiness to upgrade |
| switching_resistance | Resistance to changing products |
| referral_propensity | Likelihood of referring others |

All variables are normalized.

Recommended range:

0.0 – 1.0

---

# 9. Generation Strategy

Hidden variables are generated using multiple inputs.

Sources include:

- persona
- acquisition source
- company size
- benchmark profile
- scenario configuration
- controlled randomness

Each variable may use different probability distributions.

Examples:

- Normal Distribution
- Beta Distribution
- Triangular Distribution
- Weighted Sampling

Distribution selection is configuration-driven.

---

# 10. Influence Model

Hidden variables are not consumed directly by business outputs.

Instead, they influence downstream engines.

```text
Hidden Variables

↓

Lifecycle Decisions

↓

Weekly Activity

↓

Session Frequency

↓

Event Probability

↓

Subscription Decision

↓

Revenue

↓

Retention

↓

Churn
```

The Hidden Variable Engine never generates business outcomes directly.

---

# 11. Generation Rules

The Hidden Variable Engine ensures:

- every user receives a complete hidden variable profile
- variables remain within configured ranges
- persona bias is applied consistently
- generation is reproducible using the configured random seed
- hidden variables remain immutable during simulation

The engine never:

- modifies personas
- creates events
- changes lifecycle states
- generates revenue

---

# 12. Runtime Metrics

Recorded metrics include:

- hidden profiles generated
- average engagement score
- average purchase affinity
- average churn risk
- variable distributions
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 13. Engine Contract

Input

RuntimeContext

Consumes

- User Dataset
- Persona Profiles
- Random Manager

Produces

- Hidden Variable Profiles

Publishes

Simulation Context

Returns

EngineResult

---

# 14. References

- simulation_master_spec.md
- persona_engine.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
