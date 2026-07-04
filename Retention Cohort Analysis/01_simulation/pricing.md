# Synthetic SaaS User Behavior Simulator v2.0

# Pricing & Subscription Model

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Subscription Philosophy
3. Subscription Plans
4. Plan Features
5. Upgrade Rules
6. Downgrade Rules
7. Trial Rules
8. Billing Rules
9. Revenue Recognition
10. Pricing Benchmarks
11. Validation Rules
12. References

---

# 1. Purpose

This document defines the subscription plans, pricing model, billing rules, and revenue generation logic used by the simulator.

The objective is not to simulate a real payment gateway, but to produce realistic subscription behavior and revenue data for product analytics.

---

# 2. Subscription Philosophy

The pricing model follows a typical B2B SaaS subscription lifecycle.

```

Signup

↓

Free

↓

Trial

↓

Basic

↓

Pro

```

Subscription changes are driven by user behavior, hidden variables, and business scenarios.

---

# 3. Subscription Plans

| Plan | Monthly Price | Description |
|------|--------------:|-------------|
| Free | $0 | Limited access to core features |
| Trial | $0 | Full access for a limited time |
| Basic | $29 | Individual professionals and small teams |
| Pro | $79 | Advanced collaboration and analytics |

Prices are configurable through the simulator configuration.

---

# 4. Plan Features

| Capability | Free | Trial | Basic | Pro |
|------------|:----:|:-----:|:-----:|:---:|
| Dashboard | ✓ | ✓ | ✓ | ✓ |
| Core Features | Limited | ✓ | ✓ | ✓ |
| Reports | Limited | ✓ | ✓ | ✓ |
| Team Collaboration | ✗ | ✓ | Limited | ✓ |
| Priority Support | ✗ | ✗ | ✗ | ✓ |

These feature differences influence user behavior throughout the simulation.

---

# 5. Upgrade Rules

Allowed upgrade path:

```

Free

↓

Trial

↓

Basic

↓

Pro

```

Rules:

- Users must start on the Free plan.
- Trial is optional and controlled by business scenarios.
- Users cannot skip directly from Free to Pro unless explicitly enabled.
- Upgrade probability depends on hidden variables and business scenarios.

---

# 6. Downgrade Rules

Downgrades are optional.

Allowed transitions:

```

Pro

↓

Basic

↓

Free

```

Rules:

- Downgrades occur after subscription expiration or cancellation.
- Downgraded users retain historical revenue.
- Downgraded users continue generating product activity.

---

# 7. Trial Rules

Default trial duration:

14 days

Rules:

- Trial begins immediately after activation.
- Trial users have full feature access.
- Trial expiration does not automatically convert to paid.
- Paid conversion depends on user behavior.

---

# 8. Billing Rules

Billing occurs only for paid subscriptions.

Rules:

- Free users generate no invoices.
- Trial users generate no invoices.
- Billing occurs after successful plan activation.
- Failed billing may be simulated in future versions.

---

# 9. Revenue Recognition

Revenue is recognized at the subscription start date.

Revenue Types:

| Type | Description |
|------|-------------|
| Monthly Subscription | Default recurring revenue |
| Upgrade Revenue | Revenue generated after plan upgrade |

Revenue is always associated with:

- user_id
- subscription_id
- billing_date
- plan
- amount

---

# 10. Pricing Benchmarks

Expected distribution:

| Plan | Expected Share |
|------|---------------:|
| Free | 70–80% |
| Trial | 8–15% |
| Basic | 8–12% |
| Pro | 2–5% |

Expected conversion:

| Transition | Expected Range |
|-----------|---------------:|
| Free → Trial | 20–35% |
| Trial → Basic | 10–20% |
| Basic → Pro | 20–35% |

These values serve as validation benchmarks and may vary depending on active business scenarios.

---

# 11. Validation Rules

The simulator validates:

- Valid upgrade paths
- Valid downgrade paths
- Billing consistency
- Revenue consistency
- Subscription chronology
- Plan distribution
- Conversion benchmarks

Datasets failing validation are rejected.

---

# 12. References

- business_rules.md
- simulation_spec.md
- state_machine.md
- revenue_definition.md
