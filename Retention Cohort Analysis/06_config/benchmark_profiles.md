# Synthetic SaaS User Behavior Simulator v2.0

# Benchmark Profiles Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Benchmark Profile Architecture
4. Available Profiles
5. Profile Structure
6. Configuration Resolution
7. Profile Inheritance
8. Profile Validation
9. Example Configurations
10. References

---

# 1. Purpose

Benchmark Profiles define the overall business characteristics of the simulated SaaS product.

A benchmark profile does **not** directly control event generation.

Instead, it provides high-level business targets that are later translated into executable probabilities through the Probability Configuration.

Each simulation activates exactly one benchmark profile.

---

# 2. Design Principles

Benchmark Profiles follow five core principles.

## Business-Oriented

Profiles describe business behavior rather than implementation details.

Examples include:

- retention targets
- conversion targets
- churn expectations
- engagement characteristics

---

## Modular

Profiles can be added without modifying the Simulation Engine.

---

## Reusable

The same benchmark profile can be combined with different scenarios.

Examples

- Balanced + Poor Onboarding

- Balanced + Pricing Increase

- Enterprise + Feature Rollout

---

## Extensible

Future SaaS models can be introduced without affecting existing profiles.

---

## Deterministic

Given the same profile and random seed, statistically similar datasets should be generated.

---

# 3. Benchmark Profile Architecture

```text
Benchmark Profile
        │
        ▼
Business Targets
        │
        ▼
Probability Manager
        │
        ▼
Resolved Probabilities
        │
        ▼
Simulation Engine
```

Benchmark profiles never contain implementation logic.

They only define target business behavior.

---

# 4. Available Profiles

The simulator currently supports the following benchmark profiles.

| Profile | Description |
|----------|-------------|
| balanced | Default realistic B2B SaaS simulation |
| growth | High-performing SaaS product |
| struggling | Product with onboarding and retention problems |
| enterprise | Enterprise-focused SaaS |
| plg | Product-Led Growth SaaS |

Only one profile may be active during a simulation.

---

# 5. Profile Structure

Each profile consists of multiple logical sections.

```yaml
benchmark_profile:

    metadata

    acquisition

    activation

    engagement

    conversion

    retention

    churn

    monetization

    feature_adoption
```

The profile does not define probabilities.

Instead, it defines target business outcomes.

---

## Metadata

General profile information.

```yaml
metadata:

    id: balanced

    display_name: Balanced SaaS

    description: Default realistic SaaS

    version: 1.0
```

---

## Business Targets

Each profile specifies target ranges for major business metrics.

Example categories include:

- acquisition quality
- activation performance
- funnel conversion
- retention
- churn
- monetization
- engagement

Exact values are documented in:

```
04_quality/benchmark.md
```

---

# 6. Configuration Resolution

Benchmark Profiles are resolved before simulation begins.

```text
Load Profile
      │
      ▼
Validate Profile
      │
      ▼
Merge Global Defaults
      │
      ▼
Apply Scenario Overrides
      │
      ▼
Generate Resolved Targets
```

Resolved targets are forwarded to the Probability Manager.

---

# 7. Profile Inheritance

Every profile inherits the Global Business Rules.

```text
Global Business Rules
          │
          ▼
Benchmark Profile
          │
          ▼
Scenario Modifier
          │
          ▼
Resolved Configuration
```

A profile may change target values but must never violate fundamental business rules.

Examples

✓ Purchase requires trial.

✓ Trial requires activation.

✓ Revenue requires subscription.

✓ Retention cannot exceed 100%.

---

# 8. Profile Validation

Before activation, each profile is validated.

## Required Sections

- metadata
- acquisition
- activation
- engagement
- conversion
- retention
- churn
- monetization
- feature_adoption

---

## Validation Rules

| Rule | Expected |
|------|----------|
| Profile ID unique | PASS |
| Required sections present | PASS |
| Target ranges valid | PASS |
| Compatible with simulator version | PASS |
| Business rules satisfied | PASS |

Any validation failure prevents the profile from being loaded.

---

# 9. Example Configurations

## Balanced

```yaml
benchmark_profile:

    id: balanced
```

---

## Growth

```yaml
benchmark_profile:

    id: growth
```

---

## Enterprise

```yaml
benchmark_profile:

    id: enterprise
```

---

## PLG

```yaml
benchmark_profile:

    id: plg
```

---

## Struggling

```yaml
benchmark_profile:

    id: struggling
```

The simulator loads the complete profile definition based on the selected identifier.

---

# References

- simulator_config.md
- benchmark.md
- probability_config.md
- scenario_config.md
- business_rules.md
