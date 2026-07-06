# Synthetic SaaS User Behavior Simulator v2.0

# Session Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Session Model
7. Generation Workflow
8. Session Attributes
9. Session Generation Strategy
10. Session Rules
11. Runtime Metrics
12. Engine Contract
13. References

---

# 1. Purpose

The Session Engine converts weekly user activity into realistic product sessions.

A session represents one continuous period of product usage by a user.

The Session Engine determines when users visit the product, how often they visit, and how long each visit lasts.

The generated sessions become the foundation for downstream event generation.

---

# 2. Responsibilities

The Session Engine is responsible for:

- generating user sessions
- assigning session timestamps
- generating session duration
- generating session sequence
- enriching User Blueprints
- publishing Session Dataset

The Session Engine is **not** responsible for:

- generating events
- subscriptions
- revenue
- retention
- churn

Those responsibilities belong to downstream engines.

---

# 3. Engine Position

```text
Weekly Activity Engine

↓

Session Engine

↓

Event Engine
```

The Session Engine executes after weekly activity generation.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- Lifecycle Profiles
- Weekly Activity Profiles
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

Session Dataset

Published to

Simulation Context

Each User Blueprint is enriched with generated sessions.

---

# 6. Session Model

A session represents one continuous interaction with the SaaS product.

Each session belongs to exactly one:

- user
- simulation week

Each session contains one or more downstream events.

Sessions are generated only during active weeks.

---

# 7. Generation Workflow

```text
Load Weekly Activity Profiles

↓

Determine Active Weeks

↓

Estimate Session Count

↓

Generate Session Dates

↓

Generate Session Start Time

↓

Generate Session Duration

↓

Generate Session ID

↓

Validate Timeline

↓

Publish Session Dataset
```

---

# 8. Session Attributes

Each session contains:

| Attribute | Description |
|------------|-------------|
| session_id | Unique session identifier |
| user_id | Session owner |
| session_number | Sequential session index |
| simulation_week | Simulation week |
| session_start | Session start timestamp |
| session_end | Session end timestamp |
| session_duration_minutes | Session duration |
| expected_event_count | Estimated downstream events |
| device_type | Device used |
| traffic_source | Session acquisition source |

These attributes are immutable once generated.

---

# 9. Session Generation Strategy

Session generation depends on:

- weekly activity
- engagement score
- lifecycle state
- persona
- scenario modifiers
- benchmark profile

Typical behavior

### Highly active users

- many sessions
- longer duration

### Trial users

- frequent sessions

### Paid users

- stable sessions

### Dormant users

- very few sessions

### Churned users

- no sessions

Session timestamps are distributed realistically throughout the week.

---

# 10. Session Rules

The Session Engine ensures:

- every session belongs to one user
- every session belongs to one active week
- session timestamps are chronological
- session duration is positive
- sessions occur after signup
- churned users generate no new sessions
- session generation is reproducible

The engine never:

- generates events
- changes lifecycle
- modifies hidden variables
- generates purchases

---

# 11. Runtime Metrics

Recorded metrics include:

- sessions generated
- sessions per user
- average session duration
- session distribution by weekday
- session distribution by hour
- sessions per lifecycle state
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 12. Engine Contract

Input

RuntimeContext

Consumes

- Weekly Activity Profiles
- Hidden Variable Profiles
- Random Manager

Produces

- Session Dataset

Publishes

Simulation Context

Returns

EngineResult

---

# 13. References

- simulation_master_spec.md
- weekly_activity_engine.md
- lifecycle_engine.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
