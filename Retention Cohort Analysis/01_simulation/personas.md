# Synthetic SaaS User Behavior Simulator v2.0

# User Personas

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Persona Philosophy
3. Persona Assignment
4. Persona Library
5. Persona Comparison Matrix
6. Persona Evolution Rules
7. Validation Rules
8. References

---

# 1. Purpose

User personas represent long-term behavioral tendencies within the SaaS product.

A persona influences how users interact with the product but does not directly generate events.

Instead, personas modify hidden variables and behavioral probabilities throughout the simulation.

Each user is assigned exactly one persona during initialization.

Personas remain fixed for the entire simulation.

---

# 2. Persona Philosophy

Personas describe *why* users behave differently.

They should represent real customer archetypes commonly found in B2B SaaS products rather than marketing personas.

A persona influences:

- Activity Frequency
- Session Duration
- Feature Preference
- Upgrade Probability
- Collaboration Behavior
- Churn Risk
- Learning Speed
- Product Adoption

Personas never override business rules.

---

# 3. Persona Assignment

Each user receives one persona during user generation.

Assignment is probabilistic and configurable.

Example distribution

| Persona | Default Share |
|----------|--------------:|
| Explorer | 30% |
| Analyst | 25% |
| Collaborator | 20% |
| Executive | 10% |
| Casual User | 15% |

The distribution may be modified through configuration files.

---

# 4. Persona Library
## 4.1. Explorer

### Description

Explorer users are curious and enjoy discovering new functionality.

They generate many exploratory actions but are not always committed to long-term adoption.

---

### Typical Behavior

- Frequently explores new features
- Opens many pages
- Moderate retention
- Medium purchase intent

---

### Behavioral Profile

| Attribute | Level |
|-----------|--------|
| Activity Frequency | High |
| Session Length | Medium |
| Feature Exploration | Very High |
| Collaboration | Low |
| Upgrade Intent | Medium |
| Price Sensitivity | Medium |
| Learning Speed | Fast |
| Churn Risk | Medium |

---

### Primary Features

- dashboard_view
- feature_used
- report_created

---

### Business Impact

Explorer users contribute heavily to feature adoption metrics but have inconsistent monetization.

---


## 4.2. Analyst

### Description

Analysts rely heavily on reporting and data-driven workflows.

They seek efficiency and frequently use advanced analytical features.

---

### Behavioral Profile

| Attribute | Level |
|-----------|--------|
| Activity Frequency | High |
| Session Length | Long |
| Feature Exploration | Medium |
| Collaboration | Medium |
| Upgrade Intent | High |
| Price Sensitivity | Low |
| Learning Speed | Fast |
| Churn Risk | Low |

---

### Primary Features

- report_created
- dashboard_view
- feature_used

---

### Business Impact

Analysts are among the strongest candidates for long-term paid subscriptions.

---

## 4.3. Collaborator

### Description

Collaborators focus on teamwork and shared workflows.

---

### Behavioral Profile

| Attribute | Level |
|-----------|--------|
| Activity Frequency | High |
| Session Length | Medium |
| Collaboration | Very High |
| Upgrade Intent | High |
| Churn Risk | Low |

---

### Primary Features

- invite_team_member
- dashboard_view
- report_created

---

### Business Impact

Collaboration often drives network effects and team expansion.

---

## 4.4. Executive

### Description

Executives log in less frequently but expect immediate business value.

---

### Behavioral Profile

| Attribute | Level |
|-----------|--------|
| Activity Frequency | Low |
| Session Length | Short |
| Upgrade Intent | Very High |
| Price Sensitivity | Very Low |
| Churn Risk | Low |

---

### Primary Features

- dashboard_view
- report_created

---

### Business Impact

Executives contribute disproportionately to revenue despite low activity.

---

## 4.5. Casual User

### Description

Casual users interact occasionally with the product and often struggle to reach long-term adoption.

---

### Behavioral Profile

| Attribute | Level |
|-----------|--------|
| Activity Frequency | Low |
| Session Length | Short |
| Upgrade Intent | Low |
| Price Sensitivity | High |
| Churn Risk | High |

---

### Primary Features

- dashboard_view

---

### Business Impact

Casual users contribute significantly to churn and low-conversion cohorts.

---

# 5. Persona Comparison Matrix

| Attribute         | Explorer | Analyst | Collaborator | Executive | Casual   |
| ----------------- | -------- | ------- | ------------ | --------- | -------- |
| Activity          | High     | High    | High         | Low       | Low      |
| Session Length    | Medium   | Long    | Medium       | Short     | Short    |
| Collaboration     | Low      | Medium  | Very High    | Low       | Very Low |
| Upgrade Intent    | Medium   | High    | High         | Very High | Low      |
| Churn Risk        | Medium   | Low     | Low          | Low       | High     |
| Price Sensitivity | Medium   | Low     | Medium       | Very Low  | High     |
| Learning Speed    | Fast     | Fast    | Medium       | Medium    | Slow     |

---

# 6. Persona DNA

| Hidden Variable     | Explorer | Analyst | Collaborator | Executive | Casual |
| ------------------- | -------- | ------- | ------------ | --------- | ------ |
| Engagement Score    | 65–90    | 70–95   | 75–95        | 50–75     | 20–60  |
| Adoption Score      | 55–85    | 75–95   | 65–90        | 60–80     | 20–50  |
| Intent Score        | 50–75    | 75–95   | 70–90        | 80–100    | 20–55  |
| Collaboration Score | 20–40    | 40–70   | 85–100       | 20–40     | 0–20   |
| Price Sensitivity   | 40–70    | 20–40   | 35–60        | 0–20      | 70–100 |


# 7. Persona Evolution Rules

Personas are immutable.

However, hidden variables influenced by personas may change over time.

Example:

```

Explorer

↓

Higher Feature Usage

↓

Higher Adoption Score

↓

Eventually becomes Power User

```

The persona remains Explorer, but the user's hidden state evolves.

---

# 8. Validation Rules

The simulator validates:

- Persona distribution
- Feature preference consistency
- Upgrade consistency
- Churn consistency
- Session consistency

Datasets violating persona expectations are flagged during QA.

---

# 8. References

- simulation_spec.md
- business_rules.md
- hidden_variables.md
- scenario_library.md

