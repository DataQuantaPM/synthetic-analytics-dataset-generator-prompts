# Synthetic analytics dataset generator prompts

A collection of synthetic dataset prompts, Python generator scripts, and generated CSV datasets for analytics portfolio projects.

This repository is created to help data analytics learners build realistic datasets when public datasets do not match the case study they want to analyze.

Instead of only searching for datasets on Kaggle or other public sources, this repo shows that you can also design and generate your own dataset using a structured prompt and Python.

<br>

---

<br>

## Why This Repository Exists

Finding the right dataset for a portfolio project is not always easy.

Public datasets are useful, but sometimes they are:

- too generic
- too clean
- missing important columns
- not aligned with the business case
- not suitable for the analysis you want to practice

For example, if you want to build a specific project about funnel drop-offs, retention, churn, revenue loss, or cohort analysis, the exact dataset you need may not exist.

That is why this repository provides reusable dataset prompts and Python scripts to generate synthetic datasets with realistic logic.

The goal is not to create random dummy data.

The goal is to create datasets that can support realistic analytics practice.

<br>

---

<br>

## What This Repository Contains

Each dataset folder contains:

| File | Description |
|---|---|
| `README.md` | Overview of the dataset and its use case |
| `Dataset Prompt.md` | Full prompt used to generate the synthetic dataset |
| `Prompt Explanation.md` | Explanation of the logic behind the prompt |
| `generate_dataset.py` | Python script used to generate the dataset |
| `dataset.csv` | Generated synthetic dataset |

<br>

---

<br>

## Available Datasets

| No. | Dataset Project | Main Analysis Use Case | Link Access |
|---|---|---|---|
| 01 | SaaS Funnel Analysis | Funnel conversion, drop-off analysis, revenue leakage | link |
| 02 | SaaS Retention & Cohort Analysis | Retention, churn, cohort analysis, aha moment analysis | ( Click Here )[https://github.com/DataQuantaPM/synthetic-analytics-dataset-generator-prompts/tree/main/Retention%20Cohort%20Analysis] |

More datasets may be added in the future.

<br>

---

<br>

## How to Use This Repository

### 1. Choose a dataset case study

Open one of the dataset folders based on the type of project you want to build.

For example:

- SaaS Funnel Analysis
- SaaS Retention & Cohort Analysis

---

### 2. Read the dataset prompt

Open `Dataset Prompt.md`.

This file explains the full dataset generation request, including:

- business context
- dataset structure
- expected columns
- user behavior logic
- dirty data rules
- validation requirements

You can copy and modify the prompt based on your own project idea.

---

### 3. Run the Python script

Each folder includes a Python generator script.

Example command:

`python generate_saas_retention_dataset.py`

The script will generate a CSV dataset that can be used for SQL, Tableau, Excel, Power BI, or other analytics tools.

---

### 4. Analyze the dataset

You can use the generated dataset to practice:

- data cleaning
- exploratory data analysis
- SQL analysis
- cohort analysis
- retention analysis
- churn analysis
- funnel analysis
- revenue analysis
- dashboard creation
- business insight writing

<br>

---

<br>

## What Makes These Datasets More Realistic

The datasets in this repository are designed with realistic business and data logic.

Depending on the project, the datasets may include:

- event-level user activity
- user progression over time
- acquisition sources
- session behavior
- plan or subscription status
- revenue events
- churn behavior
- retention patterns
- feature usage behavior
- dirty data such as typos, nulls, duplicates, and inconsistent labels

The datasets are synthetic, but they are designed to behave closer to real analytics data than random dummy rows.

<br>

---

<br>

## Important Note About Synthetic Data

All datasets in this repository are synthetic.

They are not real company data.

They are created for:

- learning
- portfolio practice
- case study simulation
- SQL practice
- dashboard practice
- analytics storytelling

Do not present these datasets as real company datasets.

If you use them in a portfolio project, be transparent that the data is synthetic and generated for learning purposes.

<br>

---

<br>

## Recommended Portfolio Workflow

A good analytics project should not stop at generating a dataset.

Recommended workflow:

1. Define the business problem
2. Generate the synthetic dataset
3. Clean the data
4. Analyze key metrics
5. Create visualizations
6. Write business insights
7. Recommend actions

The most important part is not just the dataset.

The most important part is how you use the dataset to answer a business question.

<br>

---

<br>

## Example Project Questions

You can use these datasets to answer questions such as:

### Funnel Analysis

- Where do users drop off in the funnel?
- Which acquisition source has the weakest conversion?
- How much revenue is potentially lost from funnel drop-off?
- Which funnel stage should be optimized first?

### Retention & Cohort Analysis

- How does user retention change by signup cohort?
- Which source brings users with better long-term retention?
- When do users usually churn?
- Do users who use core features early retain better?
- Which segment should be prioritized for retention improvement?

<br>

---

<br>

## Tools You Can Use

These datasets can be used with:

- SQL
- Python
- Excel
- Tableau
- Power BI
- Google Sheets
- Looker Studio

The Python scripts are used only to generate the synthetic datasets.

The actual analysis can be done using any analytics tool.

<br>

---

<br>

## Who This Repository Is For

This repository is useful for:

- beginner data analysts
- aspiring product analysts
- analytics portfolio builders
- students learning SQL and dashboarding
- people who cannot find the right public dataset
- learners who want to practice realistic business analysis

<br>

---

<br>

## Limitations

Synthetic datasets are useful, but they have limitations.

They may not fully capture:

- real customer behavior
- unexpected business events
- production data complexity
- real company constraints
- actual market dynamics

The datasets are designed for practice, not for real business decision-making.

<br>

---

<br>

## How to Customize the Prompts

You can modify the dataset prompts to fit your own project.

For example, you can change:

- industry
- business context
- number of users
- number of rows
- event names
- revenue logic
- dirty data level
- retention pattern
- funnel steps
- segment behavior

If you customize the prompt, always validate the generated dataset before using it in your analysis.

<br>

---

<br>

## Final Thought

You do not always need to wait until you find the perfect dataset.

Sometimes, the better approach is to design the dataset based on the problem you want to analyze.

Public datasets are useful.

But when the right dataset does not exist, you can build your own.
