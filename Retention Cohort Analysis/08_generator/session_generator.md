# Synthetic SaaS User Behavior Simulator v2.0

# Session Generator Specification

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
8. Session Generation Logic
9. Session Scheduling
10. Session Characteristics
11. Device & Platform Consistency
12. Internal Validation
13. Runtime Metrics
14. Generator Contract
15. References

---

# 1. Purpose

The Session Generator creates user sessions that represent visits to the SaaS application.

Sessions define **when**, **how often**, and **from which device** users interact with the product.

They provide the temporal structure required for downstream event generation.

---

# 2. Responsibilities

The Session Generator is responsible for:

- determining whether a user returns
- generating session timestamps
- generating session identifiers
- assigning session duration
- assigning session device
- assigning session platform
- publishing the Sessions dataset

The Session Generator is **not** responsible for:

- lifecycle transitions
- generating events
- subscriptions
- revenue
- retention calculation
- churn analysis

---

# 3. Generator Position

```text
Users Dataset

↓

Session Generator

↓

Sessions Dataset

↓

Lifecycle Generator
```

Every downstream behavioral dataset depends on sessions.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Dataset

Users

Configuration

- benchmark_profiles
- probability_config
- simulator_config

---

# 5. Outputs

Primary Dataset

Sessions

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| session_id | Unique session identifier |
| user_id | Owner user |
| session_start | Session start timestamp |
| session_end | Session end timestamp |
| session_duration_minutes | Duration |
| device | Session device |
| platform | Web / Mobile |
| session_number | Sequential session number |

Primary Key

session_id

Foreign Key

user_id → Users.user_id

---

# 7. Generation Workflow

```text
Load Users

↓

Determine Returning Users

↓

Generate Session Count

↓

Generate Session Schedule

↓

Assign Device

↓

Assign Platform

↓

Calculate Duration

↓

Validate Sessions

↓

Publish Dataset
```

---

# 8. Session Generation Logic

## Step 1

Select active users.

Not every user receives sessions.

Activity probability depends on:

- persona
- acquisition source
- benchmark profile

---

## Step 2

Determine number of sessions.

Examples

Explorer

2 sessions

Power User

18 sessions

Casual User

5 sessions

Distribution is configurable.

---

## Step 3

Generate session timestamps.

Sessions follow:

- simulation window
- seasonality
- weekday effects
- business hour profile

Sessions are sorted chronologically.

---

## Step 4

Generate session IDs.

Example

```
S00000001
S00000002
```

IDs are globally unique.

---

## Step 5

Generate duration.

Duration follows configured distributions.

Examples

- 2 minutes
- 12 minutes
- 45 minutes

---

# 9. Session Scheduling

Session timing is influenced by:

- user persona
- weekday/weekend profile
- country timezone
- traffic seasonality
- campaign periods

The scheduling model supports configurable traffic curves.

---

# 10. Session Characteristics

Each session includes additional behavioral properties.

Examples

- session_number
- entry_device
- platform
- duration
- engagement_level

These attributes are later used by the Event Generator.

---

# 11. Device & Platform Consistency

The Session Generator maintains realistic device behavior.

Rules

- most users keep the same primary device
- occasional device switching is allowed
- platform depends on device type
- device switching probability is configurable

Example

Desktop → Web

Mobile → Mobile App

Tablet → Web

---

# 12. Internal Validation

Before publication, the generator validates:

- unique session_id
- valid user_id
- chronological timestamps
- positive duration
- valid device
- valid platform
- valid session number

Publication occurs only after successful validation.

---

# 13. Runtime Metrics

Recorded metrics include:

- sessions generated
- active users
- average sessions per user
- average duration
- average session length
- device distribution
- platform distribution
- execution time
- validation warnings

---

# 14. Generator Contract

Input

RuntimeContext

Consumes

Users Dataset

Produces

Sessions Dataset

Publishes

Sessions Dataset

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- abstract_generator.md
- engine_contract.md
- benchmark_profiles.md
- personas.md
