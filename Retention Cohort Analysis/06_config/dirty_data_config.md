# Synthetic SaaS User Behavior Simulator v2.0

# Dirty Data Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Dirty Data Architecture
4. Dirty Data Categories
5. Configuration Structure
6. Injection Pipeline
7. Severity Levels
8. Validation Rules
9. Example Configuration
10. References

---

# 1. Purpose

Dirty Data Configuration controls the intentional introduction of realistic data quality issues into generated datasets.

The goal is to simulate real-world analytical environments where data is often incomplete, inconsistent, duplicated, delayed, or incorrectly formatted.

Dirty data is a feature of the simulator and is generated in a controlled and measurable way.

---

# 2. Design Principles

## Realistic

Injected issues should resemble common production data problems.

---

## Controlled

All dirty data behavior must be configurable.

---

## Measurable

The simulator must report how much dirty data was injected.

---

## Reversible

Raw clean datasets should always be reproducible.

---

## Isolated

Dirty data should be injected after core dataset generation.

---

# 3. Dirty Data Architecture

```text
Clean Dataset
        │
        ▼
Dirty Data Engine
        │
        ├── Duplicate Engine
        │
        ├── Missing Value Engine
        │
        ├── Timestamp Engine
        │
        ├── Label Noise Engine
        │
        ├── Event Order Engine
        │
        ▼
Dirty Dataset
```

Dirty data is never generated directly by the core generators.

---

# 4. Dirty Data Categories

The simulator supports the following dirty data categories.

| Category | Description |
|-----------|-------------|
| duplicate_records | Duplicate rows |
| missing_values | Null values |
| label_variants | Inconsistent labels |
| timestamp_shift | Incorrect timestamps |
| event_order_violation | Events appear in wrong sequence |
| orphan_records | Broken relationships |
| invalid_values | Invalid field values |
| inconsistent_identifiers | Entity mismatch |
| delayed_events | Late-arriving events |
| outlier_values | Extreme values |

---

# 5. Configuration Structure

Each dirty data type follows a common schema.

```yaml
dirty_data:

  id:

  enabled:

  severity:

  injection_rate:

  scope:

  rules:

  validation:
```

---

## ID

Unique dirty-data identifier.

Example

```yaml
id:

  duplicate_records
```

---

## Enabled

Whether the injection is active.

```yaml
enabled:

  true
```

---

## Severity

Controls intensity.

```yaml
severity:

  medium
```

Supported values:

- low
- medium
- high
- extreme

---

## Injection Rate

Percentage of affected records.

```yaml
injection_rate:

  0.03
```

Example:

3% of records affected.

---

## Scope

Determines where the issue may occur.

```yaml
scope:

  tables:

    - events

    - sessions
```

---

## Rules

Defines how the issue is generated.

```yaml
rules:

  duplicate_strategy:

    exact_copy
```

---

## Validation

Determines whether the issue is allowed to break validation.

```yaml
validation:

  expected: true
```

---

# 6. Injection Pipeline

Dirty data is injected after the clean dataset has been generated.

```text
Clean Dataset
        │
        ▼
Duplicate Injection
        │
        ▼
Missing Value Injection
        │
        ▼
Label Noise Injection
        │
        ▼
Timestamp Injection
        │
        ▼
Relationship Injection
        │
        ▼
Dirty Dataset
```

The order of injection is deterministic.

---

# 7. Severity Levels

Severity defines expected impact.

| Severity | Typical Rate |
|----------|-------------:|
| Low | 0–2% |
| Medium | 2–5% |
| High | 5–10% |
| Extreme | 10–20% |

Actual values are configurable.

---

# 8. Validation Rules

Before execution, the Dirty Data Engine validates configuration.

| Rule | Expected |
|--------|---------|
| ID unique | PASS |
| Severity valid | PASS |
| Injection rate within range | PASS |
| Scope exists | PASS |
| Rules valid | PASS |
| Validation flag defined | PASS |

Any failed validation prevents simulation startup.

---

# 9. Example Configuration

## Duplicate Records

```yaml
dirty_data:

  id: duplicate_records

  enabled: true

  severity: medium

  injection_rate: 0.03
```

---

## Missing Values

```yaml
dirty_data:

  id: missing_values

  enabled: true

  severity: low

  injection_rate: 0.02
```

---

## Timestamp Shift

```yaml
dirty_data:

  id: timestamp_shift

  enabled: true

  severity: medium

  injection_rate: 0.01
```

---

## Label Variants

```yaml
dirty_data:

  id: label_variants

  enabled: true

  severity: low

  injection_rate: 0.015
```

---

# References

- dirty_data_definition.md
- validation.md
- qa_rules.md
- simulator_config.md
- config_resolution.md
