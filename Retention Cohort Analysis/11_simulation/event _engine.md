# Synthetic SaaS User Behavior Simulator v2.0

# Event Engine Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Responsibilities
3. Engine Position
4. Inputs
5. Outputs
6. Event Model
7. Generation Workflow
8. Event Attributes
9. Event Generation Strategy
10. Funnel & Event Rules
11. Runtime Metrics
12. Engine Contract
13. References

---

# 1. Purpose

The Event Engine generates realistic user interaction events based on previously generated sessions.

Unlike previous engines that simulate user state, the Event Engine simulates observable product behavior.

The generated Event Dataset becomes the primary analytical dataset consumed by BI tools, SQL queries, product analytics platforms, and downstream business analyses.

---

# 2. Responsibilities

The Event Engine is responsible for:

- generating product events
- generating event timestamps
- generating event sequences
- preserving funnel consistency
- generating feature usage
- publishing the Event Dataset

The Event Engine is **not** responsible for:

- subscription decisions
- revenue generation
- retention calculation
- churn determination

Those responsibilities belong to downstream engines.

---

# 3. Engine Position

```text
Session Engine

↓

Event Engine

↓

Subscription Engine
```

The Event Engine executes after all sessions have been generated.

---

# 4. Inputs

Runtime Context

Contains

- User Dataset
- Persona Profiles
- Hidden Variable Profiles
- Lifecycle Profiles
- Weekly Activity Profiles
- Session Dataset
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

Event Dataset

Published to

Simulation Context

Each session is enriched with a sequence of product events.

---

# 6. Event Model

An event represents a single user interaction within a session.

Each event belongs to exactly one:

- user
- session

Each session contains one or more ordered events.

Events are immutable once generated.

---

# 7. Generation Workflow

```text
Load Session Dataset

↓

Read Lifecycle State

↓

Read Session Blueprint

↓

Determine Navigation Path

↓

Generate Event Sequence

↓

Generate Event Timestamp

↓

Validate Funnel Order

↓

Publish Event Dataset
```

---

# 8. Event Attributes

Each generated event contains:

| Attribute | Description |
|------------|-------------|
| event_id | Unique event identifier |
| event_name | Standardized event name |
| user_id | Event owner |
| session_id | Parent session |
| event_timestamp | Timestamp |
| event_order | Order within session |
| lifecycle_state | User lifecycle at event time |
| feature_name | Related feature (optional) |
| event_category | Navigation / Funnel / Feature / System |

Event attributes are immutable after creation.

---

# 9. Event Generation Strategy

Event generation depends on:

- session blueprint
- lifecycle state
- engagement score
- feature curiosity
- product fit
- persona
- scenario modifiers

Typical examples

### Early Funnel

- signup
- email_verified
- onboarding_started
- onboarding_completed

### Product Usage

- dashboard_viewed
- workspace_created
- project_created
- report_generated

### Commercial

- trial_started
- subscription_upgraded
- payment_completed

### Exit

- cancellation_requested
- subscription_cancelled

Event probabilities are configuration-driven.

---

# 10. Funnel & Event Rules

The Event Engine ensures:

- every event belongs to exactly one session
- event timestamps remain chronological
- event order is preserved
- funnel progression follows lifecycle
- duplicate events are only created when explicitly configured
- impossible event sequences are prohibited

Examples

Allowed

```text
signup

↓

email_verified

↓

onboarding_started

↓

onboarding_completed
```

Forbidden

```text
purchase

↓

signup
```

or

```text
subscription_cancelled

↓

trial_started
```

The engine preserves logical event progression.

---

# 11. Runtime Metrics

Recorded metrics include:

- total events
- events per session
- events per user
- funnel event distribution
- feature usage distribution
- event category distribution
- execution time

Metrics are published to the Runtime Metrics Registry.

---

# 12. Engine Contract

Input

RuntimeContext

Consumes

- Session Dataset
- Hidden Variable Profiles
- Lifecycle Profiles
- Random Manager

Produces

- Event Dataset

Publishes

Simulation Context

Returns

EngineResult

---

# 13. References

- simulation_master_spec.md
- session_engine.md
- lifecycle_engine.md
- event_dictionary.md
- probability_config.md
- benchmark_profiles.md
- generator_master_spec.md
- engine_contract.md
