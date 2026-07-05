# Synthetic SaaS User Behavior Simulator v2.0

# Benchmark Specification

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Benchmark Philosophy
3. Benchmark Scope
4. Funnel Benchmarks
5. Retention Benchmarks
6. Churn Benchmarks
7. Revenue Benchmarks
8. Engagement Benchmarks
9. Data Quality Benchmarks
10. Scenario Benchmarks
11. Benchmark Tolerance
12. References

---

# 1. Purpose

This document defines the target behavioral and business benchmarks used by the simulator.

These benchmarks are **simulation targets**, not industry standards.

Their purpose is to produce realistic datasets suitable for Product Analytics portfolios, SQL practice, dashboard development, and business analysis.

---

# 2. Benchmark Philosophy

The simulator is designed around realistic B2B SaaS behavior.

Benchmark values should:

- produce believable user journeys,
- generate actionable business insights,
- preserve realistic variation,
- avoid perfectly clean or perfectly optimized data.

Every benchmark represents an expected operating range rather than a fixed value.

---

# 3. Benchmark Scope

Benchmarks are defined for the following domains.

| Domain | Description |
|---------|-------------|
| Funnel | Conversion across lifecycle stages |
| Retention | Weekly cohort retention |
| Churn | User inactivity |
| Revenue | Subscription performance |
| Engagement | Product usage |
| Data Quality | Dirty data rates |
| Scenario | Expected scenario impact |

---

# 4. Funnel Benchmarks

| Stage | Expected Range |
|--------|---------------:|
| Signup → Email Verified | 90–98% |
| Email Verified → Onboarding Started | 90–96% |
| Onboarding Started → Onboarding Completed | 65–85% |
| Onboarding Completed → Trial Started | 30–45% |
| Trial Started → Paid Subscription | 15–30% |
| Paid Subscription → Renewal | 70–90% |

General expectations:

- Conversion decreases as users progress through the funnel.
- Paid acquisition typically converts worse than organic or referral traffic.
- Funnel performance should vary by acquisition source.

---

# 5. Retention Benchmarks

| Cohort Week | Expected Range |
|-------------|---------------:|
| Week 0 | 100% |
| Week 1 | 45–60% |
| Week 2 | 35–50% |
| Week 4 | 25–40% |
| Week 8 | 15–30% |
| Week 12+ | 10–20% |

Retention should decline gradually rather than collapse abruptly unless a specific scenario is enabled.

---

# 6. Churn Benchmarks

| Metric | Expected Range |
|---------|---------------:|
| Early Churn | 20–30% |
| Long-Term Churn | 40–60% |
| Reactivation Rate | 5–15% |
| High-Risk Users | 10–20% |

Churn should vary by:

- acquisition source,
- plan,
- country,
- device.

---

# 7. Revenue Benchmarks

| Metric | Expected Range |
|---------|---------------:|
| Trial → Paid | 15–30% |
| Monthly Renewal | 70–90% |
| Upgrade Rate | 5–15% |
| Downgrade Rate | 2–8% |
| Refund Rate *(optional)* | <2% |

Revenue growth should primarily originate from recurring subscriptions rather than upgrades.

---

# 8. Engagement Benchmarks

| Metric | Expected Range |
|---------|---------------:|
| Sessions per User | 4–12 |
| Events per Session | 5–15 |
| Feature Adoption | 40–70% |
| Aha Moment Achievement | 30–50% |
| Power Users | 5–10% |

Most users should exhibit moderate engagement, with only a small proportion becoming power users.

---

# 9. Data Quality Benchmarks

| Metric | Expected Range |
|---------|---------------:|
| Missing Values | 1–3% |
| Duplicate Events | 2–5% |
| Event Label Variants | 1–3% |
| Timestamp Drift | 1–2% |
| Event Reordering | <2% |
| Orphan Records | Disabled by default |
| Impossible Values | Disabled by default |

These rates simulate realistic production environments while remaining recoverable through standard SQL cleaning techniques.

---

# 10. Scenario Benchmarks

Enabled scenarios should create measurable changes relative to the baseline simulation.

Examples:

| Scenario | Expected Effect |
|----------|-----------------|
| Poor Onboarding | Lower activation and Week 1 retention |
| High Ads Churn | Higher churn among Ads users |
| Referral Campaign | Higher referral conversion |
| Feature Rollout | Increased feature adoption |
| Pricing Increase | Lower trial-to-paid conversion |

Each scenario should influence only the intended metrics without introducing unrelated distortions.

---

# 11. Benchmark Tolerance

The simulator accepts natural statistical variation.

| Status | Deviation from Target |
|---------|----------------------:|
| PASS | Within ±5% |
| WARNING | ±5–10% |
| FAIL | Greater than ±10% |

Tolerance is evaluated at the aggregate level rather than for individual users.

---

# 12. Benchmark Profiles

The simulator supports multiple benchmark profiles to model different types of SaaS businesses.

Each profile defines a coherent set of business targets covering acquisition, engagement, retention, conversion, churn, and monetization.

Changing the active profile adjusts simulation behavior without requiring modifications to the generation logic.

---

## Available Profiles

| Profile | Purpose |
|----------|---------|
| Balanced | Default realistic B2B SaaS product. |
| Growth Focused | High-performing SaaS with strong activation and retention. |
| Struggling Product | Product experiencing onboarding and retention issues. |
| Enterprise SaaS | Long sales cycle with strong customer retention. |
| Product-Led Growth (PLG) | Self-service SaaS emphasizing product adoption and viral growth. |

The active profile is selected through the simulator configuration.

Example:

```yaml
simulation:
    benchmark_profile: balanced
```

---

# Profile Comparison

| Metric | Balanced | Growth | Struggling | Enterprise | PLG |
|---------|----------:|--------:|-----------:|-----------:|-----:|
| Week 1 Retention | 50% | 65% | 35% | 60% | 55% |
| Week 4 Retention | 32% | 45% | 18% | 42% | 35% |
| Trial Conversion | 38% | 48% | 22% | 28% | 42% |
| Trial → Paid | 22% | 30% | 12% | 20% | 24% |
| Renewal Rate | 82% | 90% | 65% | 93% | 85% |
| Overall Churn | 45% | 30% | 65% | 28% | 38% |
| Power Users | 8% | 12% | 3% | 10% | 9% |

These values are target ranges rather than exact outputs.

Random variation is expected within the tolerance limits defined by the simulator.

---

# Profile Characteristics

## Balanced

Recommended for:

- portfolio projects
- SQL practice
- Tableau dashboards
- Product Analytics exercises

Characteristics:

- realistic conversion funnel
- moderate retention
- moderate churn
- balanced traffic sources
- representative SaaS behavior

---

## Growth Focused

Represents a successful SaaS product.

Characteristics:

- high activation
- high feature adoption
- high retention
- low churn
- strong monetization
- larger retained cohorts

Typical use cases:

- best-practice analytics
- growth experimentation
- executive dashboards

---

## Struggling Product

Represents a product with significant product-market fit challenges.

Characteristics:

- poor onboarding
- low activation
- weak feature adoption
- early churn
- low conversion
- declining revenue

Typical analytical questions:

- Where is the funnel bottleneck?
- Which segment churns first?
- What business improvements should be prioritized?

---

## Enterprise SaaS

Models large B2B organizations with longer customer lifecycles.

Characteristics:

- fewer signups
- lower trial volume
- longer evaluation periods
- higher contract value
- stronger retention
- lower churn

Typical analyses:

- cohort retention
- account health
- renewal forecasting

---

## Product-Led Growth (PLG)

Represents self-service SaaS products.

Characteristics:

- high signup volume
- strong product exploration
- high feature usage
- viral referrals
- faster activation
- larger free user base

Typical analyses:

- activation funnel
- Aha Moment
- feature adoption
- viral growth

---

# Profile Inheritance

All benchmark profiles inherit the simulator's global business rules.

```text
Global Business Rules
            │
            ▼
Benchmark Profile
            │
            ▼
Scenario Library
            │
            ▼
Simulation Engine
            │
            ▼
Generated Dataset
```

Profiles modify target distributions but never violate core business rules.

For example:

- users cannot purchase before signup;
- retention cannot exceed 100%;
- paid users cannot exceed trial users;
- revenue cannot exist without an active subscription.

---

# QA Integration

Each profile automatically updates the QA expectations.

Example:

Balanced

Week 1 Retention

Target

50%

PASS Range

45–55%

---

Growth

Week 1 Retention

Target

65%

PASS Range

60–70%

---

Struggling

Week 1 Retention

Target

35%

PASS Range

30–40%

The Validation Engine and QA Rules automatically reference the active benchmark profile during evaluation.

---

# Future Profiles

The simulator is designed to support additional benchmark profiles without requiring changes to the core simulation engine.

Examples include:

- Freemium SaaS
- AI SaaS
- Marketplace SaaS
- Developer Tools
- FinTech SaaS
- Healthcare SaaS
- HR SaaS
- CRM SaaS
- Cybersecurity SaaS

Each future profile can define its own benchmark configuration while remaining compatible with the existing validation and QA framework.

---

# References

- qa_rules.md
- validation.md
- business_rules.md
- scenario_library.md
- retention_definition.md
- churn_definition.md
- revenue_definition.md
