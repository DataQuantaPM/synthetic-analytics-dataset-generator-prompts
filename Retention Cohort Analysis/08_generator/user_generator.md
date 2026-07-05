# Synthetic SaaS User Behavior Simulator v2.0

# User Generator Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Generator Position
4. Inputs
5. Outputs
6. Dataset Schema
7. Generation Workflow
8. User Generation Logic
9. Persona Assignment
10. Acquisition Assignment
11. Geography Assignment
12. Device Assignment
13. Plan Assignment
14. Initial State Assignment
15. Internal Validation
16. Runtime Metrics
17. Generator Contract
18. References

---

# 1. Purpose

The User Generator creates the base user population for the simulation.

Every simulated entity originates from this generator.

The generated users become the foundation for every downstream dataset including sessions, lifecycle states, events, subscriptions, retention, churn, and revenue.

---

# 2. Responsibilities

The User Generator is responsible for:

- generating unique users
- assigning personas
- assigning acquisition sources
- assigning countries
- assigning devices
- assigning initial plans
- assigning signup timestamps
- publishing the Users dataset

The User Generator is **not** responsible for:

- creating sessions
- generating events
- creating subscriptions
- calculating revenue
- retention analysis
- churn prediction

---

# 3. Generator Position

```text
User Generator

↓

Users Dataset

↓

Session Generator
```

This is the first business generator executed by the Simulation Engine.

---

# 4. Inputs

Runtime Context

Contains:

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Configuration Sections

- simulator_config
- benchmark_profiles
- probability_config

Required Dataset

None

The User Generator has no upstream dataset dependency.

---

# 5. Outputs

Primary Dataset

Users

Dataset Descriptor

Generated automatically during publication.

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| user_id | Unique user identifier |
| signup_time | Signup timestamp |
| country | User country |
| acquisition_source | Marketing source |
| device_type | Device category |
| initial_plan | Free / Trial / Paid |
| persona | Assigned business persona |
| experiment_group | Optional A/B group |

Primary Key

user_id

---

# 7. Generation Workflow

```text
Read Configuration

↓

Initialize Random Stream

↓

Generate User IDs

↓

Assign Signup Time

↓

Assign Persona

↓

Assign Acquisition Source

↓

Assign Country

↓

Assign Device

↓

Assign Initial Plan

↓

Validate Dataset

↓

Publish Dataset
```

---

# 8. User Generation Logic

## Step 1

Generate unique user identifiers.

Rules

- globally unique
- deterministic
- sequential or configurable

Example

```
U0000001
U0000002
U0000003
```

---

## Step 2

Generate signup timestamps.

Distribution

Configured through:

- simulation period
- seasonality
- traffic profile

---

## Step 3

Assign personas.

Personas are sampled according to configured business distributions.

Example

- Explorer
- Power User
- Team Buyer
- Casual User

---

## Step 4

Assign acquisition source.

Examples

- Organic
- Paid Ads
- Referral
- Direct
- Social

Distribution controlled by:

benchmark_profiles

---

## Step 5

Assign geography.

Examples

- Indonesia
- United States
- Germany
- Japan

Country distributions are configurable.

---

## Step 6

Assign device.

Examples

- Desktop
- Mobile
- Tablet

Distribution depends on:

- country
- acquisition source
- benchmark profile

---

## Step 7

Assign initial subscription plan.

Examples

- Free
- Trial
- Paid

The assignment follows benchmark configuration.

---

# 9. Persona Assignment

Persona assignment controls downstream behavior.

Each persona influences:

- session frequency
- activity level
- trial probability
- purchase probability
- churn probability

The User Generator assigns personas but does not simulate their behavior.

---

# 10. Acquisition Assignment

Acquisition source affects downstream conversion.

Examples

```text
Organic

↓

Higher retention

Paid Ads

↓

Lower conversion

Referral

↓

Higher purchase intent
```

The User Generator stores acquisition metadata for downstream generators.

---

# 11. Geography Assignment

Countries determine:

- timezone
- pricing region
- usage profile
- language
- regional seasonality

Country distributions are configurable.

---

# 12. Device Assignment

Each user receives a primary device.

Examples

- Desktop
- Mobile
- Tablet

Device assignment influences future session behavior.

---

# 13. Plan Assignment

Each user starts with one initial plan.

Possible values

- Free
- Trial
- Paid

Future upgrades are handled by the Subscription Generator.

---

# 14. Initial State Assignment

Every generated user starts in the same lifecycle state.

```text
SIGNED_UP
```

Future lifecycle transitions are handled by the Lifecycle Generator.

---

# 15. Internal Validation

Before publication, the generator validates:

- unique user_id
- valid signup timestamps
- required columns
- valid persona
- valid country
- valid acquisition source
- valid device
- valid plan

Publication occurs only after successful validation.

---

# 16. Runtime Metrics

The User Generator records:

- users generated
- execution time
- generation rate
- country distribution
- acquisition distribution
- persona distribution
- device distribution
- plan distribution
- validation warnings

Metrics are published to Runtime Metrics.

---

# 17. Generator Contract

Input

RuntimeContext

Output

Users Dataset

Dependencies

None

Publishes

Users Dataset

Consumes

No datasets

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- abstract_generator.md
- engine_contract.md
- benchmark_profiles.md
- personas.md
- pricing.md
