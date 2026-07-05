# Synthetic SaaS User Behavior Simulator v2.0

# Output Configuration

Version: 1.0

Status: Final

---

# Table of Contents

1. Purpose
2. Design Principles
3. Output Architecture
4. Output Categories
5. Configuration Structure
6. Output Generation Pipeline
7. Directory Structure
8. Validation Rules
9. Example Configuration
10. References

---

# 1. Purpose

Output Configuration defines which artifacts are generated after a simulation completes.

It controls:

- exported datasets
- validation reports
- QA reports
- logs
- metadata
- manifests
- optional analytics outputs

The Simulation Engine never writes files directly.

Instead, all exported artifacts are managed through the Output Engine.

---

# 2. Design Principles

## Configurable

Every output artifact can be enabled or disabled independently.

---

## Reproducible

Generated outputs should be sufficient to reproduce the simulation.

---

## Organized

Artifacts are grouped into predictable directories.

---

## Extensible

New output types can be introduced without modifying existing generators.

---

## Independent

Generators produce data.

The Output Engine decides what gets written.

---

# 3. Output Architecture

```text
Simulation Engine
        │
        ▼
Output Engine
        │
        ├── Dataset Export
        ├── Reports
        ├── Metadata
        ├── Validation
        ├── Logs
        └── Manifest
```

The Output Engine is responsible for writing all simulation artifacts.

---

# 4. Output Categories

The simulator supports multiple artifact types.

| Category | Description |
|----------|-------------|
| Dataset | CSV / Parquet tables |
| Validation | Validation reports |
| QA | Quality assurance reports |
| Metadata | Simulation metadata |
| Manifest | Generated file inventory |
| Logs | Execution logs |
| Statistics | Dataset statistics |
| Documentation | Optional generated documentation |

---

# 5. Configuration Structure

Every output configuration follows a common schema.

```yaml
output:

  dataset:

  reports:

  metadata:

  logging:

  export:

  compression:
```

---

## Dataset

Defines dataset export behavior.

Example

```yaml
dataset:

  csv: true

  parquet: false

  overwrite: false
```

---

## Reports

Defines analytical reports.

```yaml
reports:

  validation: true

  qa: true

  statistics: true

  manifest: true
```

---

## Metadata

Stores simulation metadata.

```yaml
metadata:

  save_config: true

  save_runtime: true

  save_seed: true
```

---

## Logging

Controls simulator logging.

```yaml
logging:

  enabled: true

  level: INFO

  save_log: true
```

Supported log levels

- DEBUG
- INFO
- WARNING
- ERROR

---

## Export

Defines destination.

```yaml
export:

  output_directory:

    output/

  create_timestamp_folder: true
```

---

## Compression

Optional dataset compression.

```yaml
compression:

  enabled: false

  format: zip
```

Supported formats

- zip
- gzip
- none

---

# 6. Output Generation Pipeline

Artifacts are exported in a fixed order.

```text
Simulation Finished
        │
        ▼
Export Datasets
        │
        ▼
Generate Reports
        │
        ▼
Generate Metadata
        │
        ▼
Generate Manifest
        │
        ▼
Write Logs
```

This order guarantees that reports always reference finalized datasets.

---

# 7. Directory Structure

Example output directory

```text
output/

└── 2026-07-06_143000/

    datasets/

        users.csv

        sessions.csv

        events.csv

        subscriptions.csv

        revenue.csv

        retention.csv

        churn.csv

    reports/

        validation_report.json

        qa_report.json

        statistics.json

    metadata/

        simulation_config.yaml

        runtime.json

        manifest.json

    logs/

        simulation.log
```

The timestamped directory prevents accidental overwriting of previous simulations.

---

# 8. Validation Rules

Before exporting, the Output Engine validates the configuration.

| Rule | Expected |
|------|----------|
| Output directory exists or can be created | PASS |
| Export format supported | PASS |
| Compression supported | PASS |
| Log level valid | PASS |
| Report types valid | PASS |

Any validation failure prevents artifact export.

---

# 9. Example Configuration

```yaml
output:

  dataset:

    csv: true

    parquet: false

    overwrite: false

  reports:

    validation: true

    qa: true

    statistics: true

    manifest: true

  metadata:

    save_config: true

    save_runtime: true

    save_seed: true

  logging:

    enabled: true

    level: INFO

    save_log: true

  export:

    output_directory: output/

    create_timestamp_folder: true

  compression:

    enabled: false

    format: none
```

---

# References

- simulator_config.md
- validation.md
- qa_rules.md
- sample_outputs.md
- config_resolution.md
