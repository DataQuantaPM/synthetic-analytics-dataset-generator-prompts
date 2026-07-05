# Synthetic SaaS User Behavior Simulator v2.0

# QA Rules

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. QA Philosophy
3. QA Scope
4. QA Categories
5. Dataset QA Rules
6. Business QA Rules
7. Statistical QA Rules
8. Behavioral QA Rules
9. Scenario QA Rules
10. QA Severity Levels
11. QA Report
12. Acceptance Criteria
13. References

---

# 1. Purpose

This document defines the Quality Assurance (QA) rules used to evaluate whether a generated simulation is suitable for analytical use.

Unlike validation, QA focuses on realism, consistency, and business plausibility rather than structural correctness.

---

# 2. QA Philosophy

The simulator follows four QA principles.

## Realistic

Generated data should resemble production SaaS environments.

---

## Consistent

Different datasets should tell the same business story.

---

## Explainable

Every anomaly should have a logical business explanation.

---

## Repeatable

The same configuration and random seed should produce similar QA results.

---

# 3. QA Scope

QA evaluates the simulation at four levels.

| Level | Focus |
|---------|------|
| Dataset | File integrity and completeness |
| Business | SaaS business logic |
| Statistical | Distribution realism |
| Behavioral | User lifecycle realism |

---

# 4. QA Categories

| Category | Description |
|----------|-------------|
| Dataset QA | Dataset completeness |
| Business QA | SaaS rules |
| Statistical QA | Distribution targets |
| Behavioral QA | User behavior realism |
| Scenario QA | Scenario implementation |

Every simulation executes all QA categories.

---

# 5. Dataset QA Rules

The following conditions must be satisfied.

✓ Every expected CSV exists

✓ No empty dataset

✓ Required columns exist

✓ Record counts are reasonable

✓ Primary keys remain unique

✓ Foreign keys remain valid

---

# 6. Business QA Rules

Business metrics should remain realistic.

Examples

✓ Funnel conversion decreases gradually.

✓ Trial users cannot exceed signup users.

✓ Paid users cannot exceed trial users.

✓ Revenue only exists for paid users.

✓ One active subscription per user.

✓ Churn occurs after activity.

✓ Retention decreases over time.

---

# 7. Statistical QA Rules

Generated distributions should match configured targets.

Examples

| Metric | Expected |
|---------|---------|
| Ads Source | 35–45% |
| Organic | 25–35% |
| Referral | 10–20% |
| Direct | 10–20% |

---

Retention

Week 1

45–60%

Week 4

25–40%

Week 12

10–20%

---

Duplicate Events

2–5%

---

Missing Values

1–3%

---

Purchase Rate

5–10%

---

# 8. Behavioral QA Rules

Generated users should resemble realistic SaaS behavior.

Examples

✓ Most users perform multiple sessions.

✓ Power users exist.

✓ Some users churn early.

✓ Some users reactivate.

✓ Trial conversion differs by acquisition source.

✓ Feature adoption influences retention.

✓ Aha Moment precedes long-term retention.

---

# 9. Scenario QA Rules

Every enabled scenario should produce measurable effects.

Examples

If "High Ads Churn" is enabled:

Expected outcome

✓ Ads churn > Organic churn

---

If "Poor Onboarding" is enabled:

Expected outcome

✓ Activation decreases

✓ Week 1 retention decreases

---

If "Successful Referral Campaign" is enabled:

Expected outcome

✓ Referral conversion increases

---

If no measurable difference exists,

QA should issue a WARNING.

---

# 10. QA Severity Levels

| Severity | Meaning | Action |
|----------|---------|--------|
| PASS | Meets expectations | Continue |
| INFO | Minor observation | Continue |
| WARNING | Outside preferred range | Review |
| FAIL | Unrealistic simulation | Reject |

---

# 11. QA Report

Each simulation produces a QA summary.

Example

Simulation Summary

PASS

---

Datasets

PASS

Business Rules

PASS

Statistics

WARNING

Behavior

PASS

Scenario

PASS

Overall

PASS

---

# 12. Acceptance Criteria

A simulation is approved when:

✓ Validation passes

✓ Business rules pass

✓ No FAIL status exists

✓ Statistical deviations remain acceptable

✓ Dirty data stays within configured limits

✓ Scenario effects are observable

Only approved simulations should be published for portfolio analysis.

---

# References

- validation.md
- data_quality_rules.md
- benchmark.md
- scenario_library.md
- business_rules.md
