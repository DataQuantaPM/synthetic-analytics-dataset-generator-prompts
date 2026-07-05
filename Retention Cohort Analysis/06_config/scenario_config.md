# Synthetic SaaS User Behavior Simulator v2.0

# Scenario Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Scenario Architecture
4. Scenario Categories
5. Scenario Configuration Structure
6. Scenario Resolution Pipeline
7. Scenario Composition
8. Scenario Validation
9. Example Configurations
10. References

---

# 1. Purpose

Business scenarios introduce controlled behavioral changes into the simulation without modifying the underlying benchmark profile.

A scenario represents a temporary or permanent business condition that affects user behavior, conversion, engagement, retention, monetization, or data quality.

Scenarios are applied after the benchmark profile has been loaded but before probabilities are resolved.

---

# 2. Design Principles

Scenario configuration follows five principles.

## Additive

Scenarios modify existing benchmark targets rather than replacing them.

---

## Independent

Each scenario should affect only the intended business metrics.

Example:

A pricing increase should influence trial-to-paid conversion without changing signup volume.

---

## Composable

Multiple compatible scenarios may be enabled simultaneously.

Example

- poor_onboarding
- referral_campaign
- feature_rollout

---

## Predictable

Each scenario has a documented expected business impact.

---

## Reversible

Disabling a scenario restores the original benchmark behavior.

---

# 3. Scenario Architecture

```text
Benchmark Profile
        │
        ▼
Scenario Configuration
        │
        ▼
Scenario Engine
        │
        ▼
Resolved Business Targets
        │
        ▼
Probability Manager
```

Scenarios never interact directly with the Simulation Engine.

---

# 4. Scenario Categories

The simulator supports multiple categories of business scenarios.

| Category | Purpose |
|----------|---------|
| Acquisition | Traffic quality and volume |
| Activation | Onboarding experience |
| Engagement | Product usage |
| Monetization | Pricing and subscription |
| Retention | Long-term user behavior |
| Churn | User inactivity |
| Product | Feature releases and experiments |
| Marketing | Campaign effects |
| Data Quality | Optional dirty-data modifiers |

Each category may contain multiple scenarios.

---

# 5. Scenario Configuration Structure

Every scenario follows the same logical structure.

```yaml
scenario:

  metadata:

  category:

  priority:

  enabled:

  compatible_with:

  conflicts_with:

  modifiers:

  expected_impact:
```

---

## Metadata

General information.

```yaml
metadata:

  id: poor_onboarding

  display_name: Poor Onboarding

  version: 1.0
```

---

## Category

Defines the business domain affected.

Example

```yaml
category:

  activation
```

---

## Enabled

Whether the scenario is active.

```yaml
enabled:

  true
```

---

## Compatibility

Defines which scenarios may coexist.

Example

```yaml
compatible_with:

  - referral_campaign

  - feature_rollout
```

---

## Conflicts

Defines incompatible scenarios.

Example

```yaml
conflicts_with:

  - optimized_onboarding
```

The simulator rejects conflicting scenario combinations.

---

## Modifiers

Defines which business targets are adjusted.

Example

```yaml
modifiers:

  onboarding_completion:

    delta: -0.18

  week_1_retention:

    delta: -0.09

  trial_conversion:

    delta: -0.06
```

Scenario modifiers are interpreted relative to the benchmark profile.

---

## Expected Impact

Documents the intended business outcome.

Example

```yaml
expected_impact:

  activation:

    lower

  retention:

    lower

  churn:

    higher
```

---

# 6. Scenario Resolution Pipeline

```text
Benchmark Profile
        │
        ▼
Load Enabled Scenarios
        │
        ▼
Validate Compatibility
        │
        ▼
Apply Scenario Modifiers
        │
        ▼
Resolved Business Targets
        │
        ▼
Probability Manager
```

Scenario effects are cumulative unless otherwise specified.

---

# 7. Scenario Composition

Multiple scenarios are applied according to priority.

```text
Global Defaults
        │
        ▼
Benchmark Profile
        │
        ▼
Scenario Priority
        │
        ▼
Resolved Scenario Effects
```

Priority determines the order in which modifiers are applied.

| Priority | Description |
|----------|-------------|
| Critical | Applied first |
| High | Major business events |
| Medium | Standard business scenarios |
| Low | Minor behavioral adjustments |

If two scenarios modify the same metric, higher-priority scenarios are applied first.

---

# 8. Scenario Validation

Before simulation begins, the Scenario Engine validates all enabled scenarios.

## Required Checks

- Scenario exists.
- Category is valid.
- No duplicate scenario IDs.
- No incompatible combinations.
- Modifiers are within supported ranges.
- Priority is valid.

---

## Validation Rules

| Rule | Expected |
|------|----------|
| Scenario exists | PASS |
| Enabled flag valid | PASS |
| Priority valid | PASS |
| Compatible scenarios | PASS |
| No conflicts | PASS |
| Modifier ranges valid | PASS |

Any failed validation prevents scenario activation.

---

# 9. Example Configurations

## Poor Onboarding

```yaml
scenario:

  id: poor_onboarding

  enabled: true
```

---

## Referral Campaign

```yaml
scenario:

  id: referral_campaign

  enabled: true
```

---

## Feature Rollout

```yaml
scenario:

  id: feature_rollout

  enabled: true
```

---

## Pricing Increase

```yaml
scenario:

  id: pricing_increase

  enabled: true
```

Multiple scenarios may be enabled simultaneously if they pass compatibility validation.

---

# References

- simulator_config.md
- benchmark_profiles.md
- probability_config.md
- business_rules.md
- scenario_library.md
- config_resolution.md
