# Synthetic SaaS User Behavior Simulator v2.0

# Event Generator Specification

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
7. Event Generation Model
8. Generation Workflow
9. Event Sequencing
10. Session Integration
11. Lifecycle Integration
12. Event Attributes
13. Internal Validation
14. Runtime Metrics
15. Generator Contract
16. References

---

# 1. Purpose

The Event Generator produces behavioral telemetry representing how users interact with the SaaS product.

Unlike the Lifecycle Generator, which determines business progression, the Event Generator creates observable analytics events that describe user interactions within sessions.

The generated events become the primary dataset used for funnel analysis, product analytics, retention analysis, and feature adoption metrics.

---

# 2. Responsibilities

The Event Generator is responsible for:

- generating user interaction events
- assigning events to sessions
- preserving chronological order
- generating realistic event sequences
- attaching event metadata
- publishing the Events dataset

The Event Generator is **not** responsible for:

- lifecycle decisions
- subscription decisions
- revenue generation
- churn prediction

---

# 3. Generator Position

```text
Users

↓

Sessions

↓

Lifecycle

↓

Event Generator

↓

Events Dataset

↓

Subscription Generator
```

Events reflect business progression that has already been determined.

---

# 4. Inputs

Runtime Context

Contains

- ResolvedConfig
- RandomManager
- Logger
- Metrics

Required Datasets

- Users
- Sessions
- Lifecycle

Configuration

- probability_config
- benchmark_profiles
- scenario_config

---

# 5. Outputs

Primary Dataset

Events

Published to Dataset Registry.

---

# 6. Dataset Schema

| Column | Description |
|----------|-------------|
| event_id | Unique event identifier |
| user_id | User identifier |
| session_id | Session identifier |
| event_name | Analytics event |
| event_time | Event timestamp |
| lifecycle_state | Lifecycle state during event |
| event_order | Order within session |
| page | Current page |
| feature | Related feature |
| metadata | Optional event payload |

Primary Key

event_id

Foreign Keys

user_id → Users.user_id

session_id → Sessions.session_id

---

# 7. Event Generation Model

Events are generated from three dimensions.

## Session

Defines when events occur.

---

## Lifecycle

Defines which events are allowed.

---

## Behavior Model

Defines event frequency and ordering.

The generator never produces events that contradict lifecycle progression.

---

# 8. Generation Workflow

```text
Load Users

↓

Load Sessions

↓

Load Lifecycle

↓

Determine Allowed Events

↓

Generate Event Sequence

↓

Assign Event Attributes

↓

Validate Event Order

↓

Publish Dataset
```

---

# 9. Event Sequencing

Events are generated in chronological order within each session.

Example

```text
session_start

↓

page_view

↓

feature_clicked

↓

form_completed

↓

onboarding_completed

↓

session_end
```

Event order must always remain valid.

---

# 10. Session Integration

Every event belongs to exactly one session.

Rules

- event_time must fall inside session boundaries
- session_id must exist
- events inherit session metadata where applicable
- event order restarts for each session

---

# 11. Lifecycle Integration

Lifecycle determines which events may occur.

Example

| Lifecycle State | Allowed Events |
|-----------------|----------------|
| SIGNED_UP | signup |
| EMAIL_VERIFIED | email_verified |
| ONBOARDING_STARTED | onboarding_started |
| ONBOARDING_COMPLETED | onboarding_completed |
| ACTIVATED | feature_used |
| TRIAL | trial_started |
| PAID | subscription_purchased |

Events outside the current lifecycle state are prohibited.

---

# 12. Event Attributes

Each generated event may include:

- page
- feature
- button
- experiment_group
- country
- device
- platform
- source
- campaign
- custom metadata

Attribute generation is configurable.

---

# 13. Internal Validation

Before publication, the generator validates:

- unique event_id
- valid user_id
- valid session_id
- chronological timestamps
- valid event order
- allowed lifecycle mapping
- required event attributes
- no impossible event sequences

Publication occurs only after successful validation.

---

# 14. Runtime Metrics

Recorded metrics include:

- events generated
- average events per session
- average events per user
- event distribution
- event frequency
- execution time
- validation warnings

---

# 15. Generator Contract

Input

RuntimeContext

Consumes

- Users Dataset
- Sessions Dataset
- Lifecycle Dataset

Produces

Events Dataset

Publishes

Events Dataset

Returns

GeneratorResult

---

# References

- generator_master_spec.md
- lifecycle_generator.md
- event_dictionary.md
- session_definition.md
- abstract_generator.md
