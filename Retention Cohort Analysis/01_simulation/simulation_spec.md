# Synthetic SaaS User Behavior Simulator v2.0

# Simulation Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Project Overview
2. Objectives
3. Design Principles
4. Simulation Scope
5. Simulation Pipeline
6. User Lifecycle
7. Hidden Variables
8. Business Scenarios
9. Dataset Generation Rules
10. Dirty Data Injection
11. Quality Assurance
12. Expected Outputs
13. Out of Scope
14. Future Improvements

---

# 1. Project Overview

The Synthetic SaaS User Behavior Simulator is a configurable simulation engine that generates realistic event-level telemetry for a Business-to-Business (B2B) Software-as-a-Service (SaaS) product.

Unlike traditional random data generators, this simulator models user behavior through lifecycle progression, behavioral states, personas, and configurable business scenarios.

The generated dataset is intended for analytics practice rather than operational system testing.

---

# 2. Objectives

The simulator has four primary objectives.

## 2.1 Generate realistic user behavior

User behavior should resemble real SaaS product usage instead of randomly generated events.

---

## 2.2 Support Product Analytics

The generated dataset must support analyses including:

- Funnel Analysis
- Cohort Retention
- Churn Analysis
- Aha Moment Analysis
- Feature Adoption
- Revenue Analysis
- Segmentation

---

## 2.3 Support Data Cleaning

The simulator intentionally injects controlled data quality issues to replicate production environments.

---

## 2.4 Ensure Reproducibility

Running the simulator with the same random seed must produce identical datasets.

---

# 3. Assumptions & Constraints

This section defines the assumptions and constraints under which the simulator operates. 
These rules establish the boundaries of the simulation and ensure consistent implementation across all modules.

## 3.1 General Assumptions
- Each user_id represents one unique individual.
- A user can own multiple sessions but only one active subscription plan at any point in time.
- Every user must begin with a signup event.
- No event may occur before the signup timestamp.
- Every event belongs to exactly one session.
- Every session belongs to exactly one user.
- All timestamps are generated in chronological order.

## 3.2 Time Constraints
- The simulation runs within a fixed observation window.
- Weeks are calculated using Monday as the first day of the week.
- Session duration cannot be negative.
- Event timestamps inside a session must always be increasing.
- Revenue events cannot occur before a successful subscription upgrade.

## 3.3 Business Constraints
- Free users generate no revenue.
- Trial users generate no recurring revenue.
- Subscription upgrades must follow valid transitions (e.g., Free → Trial → Basic → Pro).
- Churn cannot occur before signup.
- A user marked as churned cannot generate future activity unless reactivation is explicitly enabled.

## 3.4 Data Constraints
Before dirty data injection:
- Every event must contain a valid event_id.
- Every event must contain a valid user_id.
- Every event must contain an event_name.
- Every event must contain an event_time.
- Duplicate events are not allowed.
- Foreign key relationships must remain valid.

## 3.5 Simulation Constraints
- Business rules are configuration-driven and should not require source code modification.
- Running the simulator with the same random seed must produce identical results.
- The simulator should support different dataset sizes (e.g., 1K, 10K, 100K users) without changing business logic.
- Dirty data is injected only after the clean dataset has been fully generated.

## 3.6 Implementation Constraints
- Each engine is responsible for a single domain.
- Engines may read outputs from previous stages but must not modify them directly.
- Entity models are immutable after creation unless explicitly managed by the corresponding engine.
- Validation must complete successfully before any dataset is exported.

---

# 4. Design Principles

The simulator follows the principles below.

## Business Driven

Business behavior determines user behavior.

Events are generated as consequences of user decisions.

---

## State Machine

Users progress through lifecycle states.

No event is generated without an underlying state transition.

---

## Config Driven

Simulation parameters are configurable through external configuration files.

Business logic should never require source-code modification.

---

## Modular

Every engine has one responsibility.

No engine directly modifies another engine's internal state.

---

## Reproducible

The same configuration and random seed produce identical outputs.

---

# 5. Simulation Scope

The simulator models:

- Individual users
- User sessions
- Product events
- Subscription changes
- Revenue generation
- Churn
- Retention
- Feature adoption
- Controlled dirty data

The simulator does not model:

- Backend systems
- Payment gateways
- CRM
- Customer support
- Marketing automation

---

# 6. Simulation Pipeline

Simulation always follows this order.

```
Configuration

↓

User Generation

↓

Persona Assignment

↓

Hidden Variable Initialization

↓

Lifecycle Simulation

↓

Weekly Activity Simulation

↓

Session Generation

↓

Event Generation

↓

Subscription Simulation

↓

Revenue Simulation

↓

Dirty Data Injection

↓

Validation

↓

Export
```

Each stage depends only on outputs from previous stages.

---

# 7. User Lifecycle

Every user progresses through a lifecycle.

Possible states include:

- Visitor
- Signup
- Exploring
- Learning
- Adopting
- Trial
- Basic
- Pro
- Dormant
- Churned

State transitions follow rules documented in:

state_machine.md

---

# 8. Hidden Variables

Each user contains internal behavioral variables.

Examples:

- Engagement Score
- Adoption Score
- Intent Score
- Health Score
- Collaboration Score
- Price Sensitivity

These variables influence future behavior.

They are not exported.

---

# 9. Business Scenarios

Every generated dataset includes predefined business scenarios.

Examples:

- Weak Onboarding
- Low Quality Ads
- Pricing Resistance
- Mobile UX Issues
- Strong Organic Growth
- Collaboration Adoption
- High Churn

Scenarios influence user behavior while preserving statistical realism.

---

# 10. Dataset Generation Rules

The simulator generates data according to these rules.

## Users

Generated once.

Never duplicated.

---

## Sessions

Generated only for active users.

Inactive users generate no sessions.

---

## Events

Generated only inside sessions.

Every event must belong to exactly one session.

---

## Revenue

Generated only after successful subscription billing.

Free users generate no revenue.

---

## Churn

Generated from inactivity rather than random assignment.

---

# 11. Dirty Data Injection

Dirty data is applied after clean data generation.

Possible injected issues include:

- Missing values
- Duplicate rows
- Timestamp inconsistencies
- Event naming inconsistencies
- Tracking failures

Dirty data percentages are configurable.

---

# 12. Quality Assurance

Before export, the simulator validates:

- User counts
- Event counts
- Retention consistency
- Funnel consistency
- Revenue consistency
- Duplicate rates
- Missing value rates
- Lifecycle validity

Datasets failing validation must not be exported.

---

# 13. Expected Outputs

The simulator exports:

```
raw_events.csv
users.csv
sessions.csv
metadata.json
qa_report.json
```

Only raw_events.csv is required for analytics.

Other outputs are intended for debugging and validation.

---

# 14. Out of Scope

The simulator intentionally excludes:

- Enterprise organizations
- Seat licensing
- Refund workflows
- Billing retries
- Support tickets
- CRM integrations
- Multi-product ecosystems

These may be added in future versions.

---

# 15. Future Improvements

Potential enhancements include:

- Multi-tenant organizations
- AI-generated personas
- Dynamic pricing experiments
- Feature flag simulations
- A/B testing support
- Marketing campaign simulations
- LTV forecasting
- Survival analysis support

---

# References

Related documentation:

- business_rules.md
- architecture.md
- state_machine.md
- scenario_library.md
- data_dictionary.md
