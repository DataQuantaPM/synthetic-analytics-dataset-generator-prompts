# Synthetic SaaS User Behavior Simulator v2.0

# Business Rules

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Business Philosophy
3. User Lifecycle Rules
4. Persona Rules
5. Hidden Variable Rules
6. Activity Rules
7. Session Rules
8. Event Rules
9. Subscription Rules
10. Revenue Rules
11. Retention Rules
12. Churn Rules
13. Aha Moment Rules
14. Dirty Data Rules
15. Business Scenario Rules
16. Validation Rules

---

# 1. Purpose

This document defines the business rules governing the Synthetic SaaS User Behavior Simulator.

These rules represent business behavior rather than implementation logic.

The implementation must always follow these rules.

---

# 2. Business Philosophy

The simulator is based on five core principles.

## 2.1 Business Before Events

Events are never generated randomly.

Events occur because a user makes a business decision.

Example

```
High engagement

↓

More sessions

↓

More feature usage

↓

Higher conversion probability
```

---

## 2.2 Users Behave Differently

Every user is unique.

Behavior depends on:

- Persona
- Hidden variables
- Lifecycle state
- Current subscription
- Business scenario

---

## 2.3 Time Matters

Behavior changes over time.

Examples:

- New users explore.
- Existing users adopt.
- Dormant users become inactive.
- Power users collaborate more.

---

## 2.4 State Determines Behavior

The same user may behave differently after changing lifecycle state.

Example

```
Exploring

↓

few events

↓

Learning

↓

more core features

↓

Pro

↓

heavy collaboration
```

---

## 2.5 Business Scenarios Influence Users

Business scenarios modify probabilities.

They never directly force events.

---

# 3. User Lifecycle Rules

Every user starts with:

```
Signup
```

Every user must enter one of the following paths.

Typical path

```
Signup

↓

Exploring

↓

Learning

↓

Adopting

↓

Trial

↓

Basic

↓

Pro
```

Possible alternative paths

```
Signup

↓

Exploring

↓

Dormant
```

or

```
Signup

↓

Exploring

↓

Learning

↓

Churn
```

Lifecycle progression depends on user behavior rather than fixed dates.

---

# 4. Persona Rules

Each user receives exactly one persona.

Example personas

- Explorer
- Collaborator
- Analyst
- Executive
- Casual User

A persona remains constant throughout the simulation.

Personas influence:

- activity frequency
- session length
- feature preference
- conversion probability
- collaboration behavior

---

# 5. Hidden Variable Rules

Each user contains hidden behavioral variables.

Examples

- Engagement Score
- Adoption Score
- Intent Score
- Health Score
- Collaboration Score
- Price Sensitivity

Rules

- Generated once.
- May evolve over time.
- Never exported.
- Influence future decisions.
- Cannot directly create events.

---

# 6. Activity Rules

Users generate activity only while active.

Inactive users produce no activity.

Activity intensity depends on

- persona
- lifecycle
- engagement
- business scenario

Core activities include

- login
- dashboard_view
- feature_used
- report_created
- invite_team_member

---

# 7. Session Rules

Every activity belongs to a session.

Rules

- Sessions belong to one user.
- Sessions contain one or more events.
- Events inside a session are chronological.
- Session duration must be positive.
- Session identifiers are unique.

---

# 8. Event Rules

Events are consequences of user activity.

Rules

- Every event belongs to one session.
- Every event has exactly one timestamp.
- Event order must be chronological.
- Events cannot occur before signup.
- Events cannot occur after the observation window.

Duplicate events are prohibited before dirty data injection.

---

# 9. Subscription Rules

Subscription changes follow valid transitions.

Allowed transitions

```
Free

↓

Trial

↓

Basic

↓

Pro
```

Downgrades may occur only when enabled by scenario configuration.

Free users cannot directly become Pro without intermediate transitions unless explicitly configured.

---

# 10. Revenue Rules

Revenue is generated only after successful billing.

Rules

- Free users generate no revenue.
- Trial users generate no recurring revenue.
- Revenue occurs after subscription activation.
- Revenue timestamps must follow subscription events.

Revenue must always be reproducible.

---

# 11. Business KPIs & Target Benchmarks

| KPI                   | Expected Range |
| --------------------- | -------------- |
| Signup → Trial        | 20–35%         |
| Trial → Paid          | 10–20%         |
| Week 1 Retention      | 45–60%         |
| Week 4 Retention      | 20–35%         |
| Aha Moment Rate       | 35–55%         |
| Churn Rate (6 months) | 30–50%         |
| Paid Conversion       | 5–10%          |


---

# 12. Retention Rules

A retained user performs at least one qualifying activity during a cohort week.

Qualifying activities exclude passive system events.

Retention is calculated using Monday-based cohort weeks.

A user may skip one week and return in a later week.

Retention does not require continuous weekly activity.

---

# 13. Churn Rules

Churn is inferred from inactivity.

Rules

- Churn is never assigned randomly.
- Churn probability depends on lifecycle and hidden variables.
- Churned users generate no future activity unless reactivation is enabled.
- Users near the end of the observation window may be right-censored.

---

# 14. Aha Moment Rules

A user reaches the Aha Moment after completing at least two core feature events within the first seven days after signup.

Core feature events

- feature_used
- report_created
- invite_team_member

Segments

| Core Events | Segment |
|-------------|---------|
| 0 | No Core Usage |
| 1 | Light Usage |
| 2–4 | Reached Aha |
| ≥5 | Power User |

A user may transition from one segment to another only within the seven-day evaluation window.

---

# 15. Dirty Data Rules

Dirty data is injected only after the clean dataset has been generated.

Possible issues

- Missing values
- Duplicate events
- Timestamp drift
- Inconsistent labels
- Tracking failures
- Device changes
- Country changes

Dirty data percentages are configurable.

Business relationships must remain analyzable despite injected imperfections.

---

# 16. Business Scenario Rules

A simulation contains one or more business scenarios.

Examples

- Weak Onboarding
- Low-Quality Ads
- Poor Trial Conversion
- High Churn
- Mobile UX Issues
- Strong Organic Growth

Scenarios influence user probabilities but never violate lifecycle rules.

Multiple scenarios may be active simultaneously.

---

# 17. Validation Rules

Before export, the simulator validates:

- lifecycle consistency
- event chronology
- session integrity
- subscription integrity
- revenue consistency
- retention sanity
- churn sanity
- duplicate rate
- missing value rate

Datasets failing validation are rejected.

---

# Rule Hierarchy

If two rules conflict, priority is determined as follows:

1. Simulation Configuration (`config.yaml`)
2. Business Rules (this document)
3. Scenario Configuration
4. Persona Rules
5. Hidden Variable Logic
6. Generator Implementation

The generator implementation must never override business rules.

---

# References

- simulation_spec.md
- architecture.md
- state_machine.md
- scenario_library.md
- data_dictionary.md
