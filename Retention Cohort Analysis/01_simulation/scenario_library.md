# Synthetic SaaS User Behavior Simulator v2.0

# Scenario Library

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Scenario Philosophy
3. Scenario Categories
4. Core Business Scenarios
5. Scenario Composition Rules
6. Scenario Configuration
7. Expected Business Impact
8. Recommended Analytics
9. Future Scenario Library

---

# 1. Purpose

Business scenarios introduce realistic business conditions into the simulation.

Rather than directly generating events, scenarios modify user behavior probabilities and lifecycle progression.

The objective is to create datasets that contain meaningful analytical problems similar to those found in production SaaS environments.

---

# 2. Scenario Philosophy

Scenarios should never directly force outcomes.

Instead, they influence hidden variables, lifecycle transitions, activity intensity, and conversion probabilities.

Example

```
Weak Onboarding

↓

Lower Adoption Score

↓

Lower Feature Usage

↓

Lower Aha Moment

↓

Lower Trial Conversion

↓

Lower Revenue
```

This causal chain produces explainable business insights.

---

# 3. Scenario Categories

Business scenarios are grouped into five categories.

| Category | Description |
|----------|-------------|
| Acquisition | Problems before signup |
| Activation | Problems during onboarding |
| Engagement | Problems after onboarding |
| Monetization | Subscription and pricing problems |
| Retention | Long-term user behavior |

Multiple scenarios may coexist within a single simulation.

---

# 3.1 Scenario Scope
Business scenarios are classified into three execution scopes.

| Scope        | Description                                                                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Global       | Affects the overall product experience and influences the majority of users. Only one Global scenario may be active in a single simulation.                                         |
| Segment      | Targets a specific subset of users (e.g., acquisition source, device, country, or persona). Multiple Segment scenarios may run simultaneously if they affect different populations. |
| Experimental | Represents temporary product experiments (e.g., A/B testing, feature rollout). These scenarios affect only a controlled percentage of eligible users.                               |

---

# 3.2 Scenario Combination Rules

## Scenario Combination Rules

The simulator supports multiple active scenarios simultaneously.

To avoid unrealistic behavior, the following rules apply:

- Only one Global scenario may be active in a simulation.
- Multiple Segment scenarios may coexist if they affect different user populations.
- Experimental scenarios may run together with both Global and Segment scenarios.
- When multiple scenarios influence the same behavioral variable, priority follows the Scenario Priority hierarchy.
- Conflicting scenarios targeting the same users should be avoided unless explicitly configured.

  

# 4. Core Business Scenarios

---

## 4.1 Weak Onboarding

### Business Description

Users complete signup but struggle to understand product value.

### Affected Population
| Attribute  | Target       |
| ---------- | ------------ |
| Source     | Ads, Organic |
| Country    | All          |
| Device     | Mobile       |
| Persona    | Explorer     |
| Early Plan | Free         |
| Coverage   | 75%          |

### Scenario Scope

Global

### Severity

High

### Primary Effects

- Lower Adoption Score
- Lower Engagement Score
- Delayed Aha Moment
- Fewer core feature events

### Expected Analytics Findings

- Large onboarding drop-off
- Lower Week 1 retention
- Lower Aha Moment rate

---

## 4.2 Low-Quality Paid Ads

### Business Description

Paid campaigns attract many users with weak purchase intent.

### Affected Population
| Attribute  | Target                |
| ---------- | --------------------- |
| Source     | Ads                   |
| Country    | All                   |
| Device     | All                   |
| Persona    | Explorer, Casual User |
| Early Plan | Free                  |
| Coverage   | 80%                   |

### Scenario Scope

Segment

### Severity

Medium

### Primary Effects

- Higher signup volume
- Lower Intent Score
- Lower Trial Conversion
- Lower Paid Conversion

### Expected Analytics Findings

- Ads contribute many signups
- Ads contribute poor retention
- Ads underperform Organic

---

## 4.3 Mobile UX Issues

### Business Description

Mobile users experience poor usability.

### Affected Population
| Attribute  | Target         |
| ---------- | -------------- |
| Source     | All            |
| Country    | All            |
| Device     | Mobile, Tablet |
| Persona    | All            |
| Early Plan | All            |
| Coverage   | 70%            |

### Scenario Scope

Segment

### Severity

Medium

### Primary Effects

- Shorter sessions
- Fewer feature interactions
- Lower retention

### Expected Analytics Findings

- Desktop outperforms Mobile
- Higher mobile churn

---

## 4.4 Pricing Resistance

### Business Description

Users perceive pricing as expensive.

### Affected Population
| Attribute  | Target                   |
| ---------- | ------------------------ |
| Source     | Ads, Referral            |
| Country    | India, Brazil, Indonesia |
| Device     | All                      |
| Persona    | Casual User              |
| Early Plan | Trial                    |
| Coverage   | 65%                      |

### Scenario Scope

Segment

### Severity

Low

### Primary Effects

- High Trial usage
- Low Basic conversion
- Low Pro upgrades

### Expected Analytics Findings

- Large Trial population
- Weak monetization

---

## 4.5 Feature Discovery Problem

### Business Description

Users fail to discover important product capabilities.

### Affected Population
| Attribute  | Target   |
| ---------- | -------- |
| Source     | Organic  |
| Country    | All      |
| Device     | Mobile   |
| Persona    | Explorer |
| Early Plan | Free     |
| Coverage   | 70%      |

### Scenario Scope

Global

### Severity

High

### Primary Effects

- Lower feature usage
- Delayed Aha Moment
- Lower retention

### Expected Analytics Findings

- Low feature adoption
- Weak activation

---

## 4.6 Collaboration Adoption

### Business Description

Team collaboration becomes a major growth driver.

### Affected Population
| Attribute  | Target                                 |
| ---------- | -------------------------------------- |
| Source     | Referral                               |
| Country    | United States, United Kingdom, Germany |
| Device     | Desktop                                |
| Persona    | Collaborator, Analyst                  |
| Early Plan | Basic                                  |
| Coverage   | 80%                                    |

### Scenario Scope

Segment

### Severity

Positive

### Primary Effects

- More invitations
- Higher engagement
- Longer retention

### Expected Analytics Findings

- Invite events correlate with retention
- Higher Pro adoption

---

## 4.7 High Churn

### Business Description

Users gradually stop using the product.

### Affected Population
| Attribute  | Target      |
| ---------- | ----------- |
| Source     | Ads         |
| Country    | All         |
| Device     | Mobile      |
| Persona    | Casual User |
| Early Plan | Trial       |
| Coverage   | 60%         |

### Scenario Scope

Global

### Severity

Critical

### Primary Effects

- Increasing inactivity
- Lower weekly activity
- Lower revenue

### Expected Analytics Findings

- Churn accelerates after Week 3
- Lower customer lifetime value

---

## 4.8 Strong Organic Growth

### Business Description

Organic acquisition attracts high-intent users.

### Affected Population
| Attribute  | Target                           |
| ---------- | -------------------------------- |
| Source     | Organic                          |
| Country    | United States, Canada, Australia |
| Device     | Desktop                          |
| Persona    | Analyst, Executive               |
| Early Plan | Free                             |
| Coverage   | 85%                              |

### Scenario Scope

Segment

### Severity

Positive

### Primary Effects

- Higher Engagement
- Better Trial conversion
- Higher Paid conversion

### Expected Analytics Findings

- Organic outperforms Ads
- Better retention

---

# 5. Scenario Composition Rules

Multiple scenarios may run simultaneously.

Example

```
Weak Onboarding

+

Low Quality Ads

+

Pricing Resistance
```

Result

```
Low Aha

↓

Low Trial

↓

Low Revenue
```

Scenarios should complement rather than contradict each other.

Conflicting scenarios should not be activated simultaneously unless explicitly configured.

---

# 6. Scenario Configuration

Every scenario exposes configurable parameters.

Example

```yaml
weak_onboarding:

  enabled: true

  adoption_multiplier: 0.75

  feature_usage_multiplier: 0.80
```

Scenario parameters must remain external to source code.

---

# 7. Expected Business Impact

Each scenario should create measurable differences in analytics outputs.

Examples

| Scenario | Primary KPI |
|----------|-------------|
| Weak Onboarding | Aha Moment ↓ |
| Low Quality Ads | Trial Conversion ↓ |
| Pricing Resistance | Paid Conversion ↓ |
| Mobile UX | Mobile Retention ↓ |
| High Churn | Week 4 Retention ↓ |

---

# 8. Recommended Analytics

Every scenario should be discoverable using common Product Analytics techniques.

Recommended analyses include:

- Funnel Analysis
- Cohort Retention
- Feature Adoption
- Churn Analysis
- Revenue Analysis
- Segmentation
- Conversion by Source
- Device Comparison

The simulator should never require hidden variables to identify business problems.

Insights must be obtainable from exported data alone.

---

# 9. Future Scenario Library

Potential future scenarios include:

- Seasonality
- Viral Growth
- Enterprise Adoption
- Team Expansion
- Marketing Campaigns
- Referral Programs
- Feature Launches
- Competitor Impact
- Price Increase
- Economic Downturn

These scenarios are not part of the current release but are designed for future extensibility.

---

# Scenario Priority

If multiple scenarios influence the same user attribute, priority is:

1. Explicit Configuration
2. Business Scenario
3. Persona
4. Hidden Variables
5. Default Behavior

This hierarchy ensures deterministic and reproducible simulations.

---

# References

- simulation_spec.md
- business_rules.md
- state_machine.md
- architecture.md
