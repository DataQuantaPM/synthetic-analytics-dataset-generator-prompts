# Synthetic SaaS User Behavior Simulator v2.0

# Probability Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Probability Architecture
4. Probability Categories
5. Configuration Structure
6. Resolution Pipeline
7. Probability Evaluation
8. Validation Rules
9. Example Configuration
10. References

---

# 1. Purpose

The Probability Configuration translates business targets into executable behavioral probabilities used by the simulation engine.

Unlike Benchmark Profiles, which define *desired business outcomes*, Probability Configuration defines the *decision probabilities* that drive user behavior during simulation.

Every generator uses this configuration when determining whether an event should occur.

---

# 2. Design Principles

## Data-Driven

All behavioral decisions are controlled through configuration.

No generator should contain hardcoded probabilities.

---

## Deterministic

Given the same resolved configuration and random seed, probability evaluation should produce statistically equivalent datasets.

---

## Hierarchical

Probabilities are resolved after:

- Global Defaults
- Benchmark Profile
- Scenario Modifiers
- Runtime Overrides

---

## Context-Aware

A probability may depend on:

- user state
- subscription plan
- acquisition source
- country
- device
- lifecycle stage
- previous events

---

## Extensible

New probabilities can be added without modifying existing generators.

---

# 3. Probability Architecture

```text
Business Targets
        │
        ▼
Probability Configuration
        │
        ▼
Probability Resolver
        │
        ▼
Resolved Probability
        │
        ▼
Generator Decision
```

Generators never calculate probabilities themselves.

They only consume resolved probabilities.

---

# 4. Probability Categories

The simulator groups probabilities into several domains.

| Category | Purpose |
|----------|---------|
| Acquisition | Traffic source behavior |
| Activation | Signup and onboarding |
| Engagement | Product usage |
| Session | Session generation |
| Conversion | Trial and purchase |
| Subscription | Renewal and cancellation |
| Revenue | Billing events |
| Retention | Returning users |
| Churn | Inactivity |
| Reactivation | Returning after churn |
| Feature Adoption | Feature usage |

---

# 5. Configuration Structure

Every probability definition follows a common schema.

```yaml
probability:

  id:

  category:

  description:

  depends_on:

  scope:

  condition:

  value:

  fallback:
```

---

## ID

Unique identifier.

Example

```yaml
id:

  onboarding_completion
```

---

## Category

Business domain.

```yaml
category:

  activation
```

---

## Depends On

Defines upstream conditions.

Example

```yaml
depends_on:

  - onboarding_started
```

---

## Scope

Defines where the probability applies.

```yaml
scope:

  benchmark:

    - balanced

    - growth

  plans:

    - free

    - pro
```

---

## Condition

Optional conditional logic.

Example

```yaml
condition:

  country == "United States"

  AND

  device == "Desktop"
```

---

## Value

Resolved probability.

```yaml
value:

  0.84
```

All probability values must be within the range [0,1].

---

## Fallback

Fallback probability if no condition matches.

```yaml
fallback:

  0.50
```

---

# 6. Resolution Pipeline

Probabilities are resolved dynamically.

```text
Global Default
        │
        ▼
Benchmark Profile
        │
        ▼
Scenario Modifiers
        │
        ▼
Conditional Rules
        │
        ▼
Fallback
        │
        ▼
Resolved Probability
```

Only resolved probabilities are visible to generators.

---

# 7. Probability Evaluation

The simulator evaluates probabilities in a consistent order.

```text
Read Probability

↓

Evaluate Scope

↓

Evaluate Conditions

↓

Apply Scenario Modifier

↓

Resolve Final Probability

↓

Generate Random Number

↓

Decision
```

Decision example

```text
Resolved Probability = 0.72

↓

Random = 0.61

↓

Decision = TRUE
```

---

# 8. Validation Rules

Every probability definition is validated before simulation.

| Rule | Expected |
|------|----------|
| ID unique | PASS |
| Category exists | PASS |
| Probability between 0–1 | PASS |
| Scope valid | PASS |
| Dependencies valid | PASS |
| Fallback defined | PASS |

Invalid probability configurations prevent simulation startup.

---

# 9. Example Configuration

## Onboarding Completion

```yaml
probability:

  id: onboarding_completion

  category: activation

  depends_on:

    - onboarding_started

  value: 0.83

  fallback: 0.70
```

---

## Trial Conversion

```yaml
probability:

  id: trial_conversion

  category: conversion

  depends_on:

    - onboarding_completed

  value: 0.38

  fallback: 0.30
```

---

## Subscription Renewal

```yaml
probability:

  id: renewal

  category: subscription

  depends_on:

    - active_subscription

  value: 0.82

  fallback: 0.75
```

---

# References

- simulator_config.md
- benchmark_profiles.md
- scenario_config.md
- config_resolution.md
- business_rules.md
