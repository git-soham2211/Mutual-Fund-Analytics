# Mutual Fund Analytics Capstone Project

## Bluestock Fintech Internship

### Author

**Soham Srivastava**

---

# Project Overview

The **Mutual Fund Analytics Capstone Project** is an end-to-end data analytics solution developed as part of the Bluestock Fintech Internship Program.

The project focuses on collecting, validating, cleaning, storing, and analyzing mutual fund data using Python, SQL, and analytical techniques. The objective is to build a scalable analytics pipeline that can support business intelligence dashboards, investment analysis, portfolio insights, and mutual fund performance evaluation.

The project follows a structured workflow:

1. Data Ingestion (ETL)
2. Data Validation & Quality Checks
3. Data Cleaning & Transformation
4. SQLite Database Design
5. Exploratory Data Analysis (EDA)
6. Performance Analytics
7. Dashboard Development
8. Advanced Analytics & Recommendations

---

# Project Objectives

* Build a robust ETL pipeline for mutual fund datasets
* Validate and clean raw financial datasets
* Design a relational database schema
* Perform NAV and performance analysis
* Analyze SIP trends and investor behavior
* Generate actionable insights
* Create interactive dashboards
* Support advanced analytics and recommendation systems

---

# Technologies Used

### Programming & Data Processing

* Python
* Pandas
* NumPy

### Database

* SQLite
* SQLAlchemy

### Data Visualization

* Matplotlib
* Seaborn
* Power BI (Upcoming)

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Project Folder Structure

```text
Mutual_Fund_Analytics/

│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── reports/
│   ├── data_quality_report.txt
│   └── data_dictionary.md
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── amfi_validation.py
│   ├── data_quality_report.py
│   ├── etl_pipeline.py
│   ├── load_to_sqlite.py
│   └── validate_row_counts.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Datasets Used

The project uses 10 mutual fund datasets:

| Dataset               | Description                     |
| --------------------- | ------------------------------- |
| Fund Master           | Scheme master information       |
| NAV History           | Historical NAV records          |
| AUM by Fund House     | Asset Under Management details  |
| Monthly SIP Inflows   | SIP growth and trends           |
| Category Inflows      | Category-wise fund inflows      |
| Industry Folio Count  | Mutual fund folio statistics    |
| Scheme Performance    | Returns and risk metrics        |
| Investor Transactions | Investor-level transaction data |
| Portfolio Holdings    | Scheme portfolio constituents   |
| Benchmark Indices     | Market benchmark data           |

---

# Day 1 Deliverables

## Project Setup

* Created project folder structure
* Configured Python virtual environment
* Installed required dependencies
* Initialized Git repository
* Connected GitHub repository

---

## Data Ingestion

Loaded and analyzed all 10 datasets using Pandas.

### Validation Performed

* Dataset dimensions check
* Data type validation
* Missing value analysis
* Duplicate record verification
* AMFI code verification

---

## Live NAV Fetch

Implemented API-based NAV fetching for selected mutual fund schemes:

* SBI Bluechip Fund
* ICICI Bluechip Fund
* Nippon Large Cap Fund
* Axis Bluechip Fund
* Kotak Bluechip Fund

---

## AMFI Validation

Validated all AMFI codes against NAV history dataset.

### Result

* Total Fund Master Codes: 40
* Total NAV History Codes: 40
* Validation Status: SUCCESS

---

## Data Quality Findings

### Key Observation

Only one anomaly detected:

* 12 missing values in `yoy_growth_pct` column of Monthly SIP Inflows dataset

All other datasets passed validation checks.

---

# Day 2 Deliverables

## Data Cleaning & Transformation

Created cleaned versions of all datasets.

### Cleaned Datasets

1. 01_fund_master_clean.csv
2. 02_nav_history_clean.csv
3. 03_aum_by_fund_house_clean.csv
4. 04_monthly_sip_inflows_clean.csv
5. 05_category_inflows_clean.csv
6. 06_industry_folio_count_clean.csv
7. 07_scheme_performance_clean.csv
8. 08_investor_transactions_clean.csv
9. 09_portfolio_holdings_clean.csv
10. 10_benchmark_indices_clean.csv

---

### Cleaning Operations

* Date parsing and standardization
* Duplicate removal
* Missing value handling
* Numeric data validation
* Expense ratio validation
* NAV validation
* Transaction validation
* Data type correction

---

# SQLite Database Design

Created SQLite database:

```text
data/db/bluestock_mf.db
```

---

## Database Tables

### Dimension Tables

* dim_fund

### Fact Tables

* fact_nav
* fact_aum
* fact_transactions
* fact_performance

---

## Database Validation

Verified successful table creation and data loading.

Row count validation performed between source CSVs and database tables.

---

# SQL Development

## Schema Design

Created SQL schema using:

```text
sql/schema.sql
```

Includes:

* Primary Keys
* Foreign Keys
* Fact-Dimension Model
* Relational Structure

---

## Analytical Queries

Created:

```text
sql/queries.sql
```

Contains analytical queries for:

* Top Funds by AUM
* NAV Analysis
* Investor Trends
* Transaction Analysis
* Risk Metrics
* Performance Comparison
* Category Insights
* Fund House Analytics

---

# Reports Generated

### Data Quality Report

```text
reports/data_quality_report.txt
```

Contains:

* Missing values
* Data types
* Validation findings
* Quality observations

---

### Data Dictionary

```text
reports/data_dictionary.md
```

Contains:

* Column descriptions
* Data types
* Business definitions
* Source references

---

# Key Achievements

### Day 1

* ETL Pipeline Developed
* Data Quality Validation Completed
* Live NAV Fetch Implemented
* AMFI Validation Completed

### Day 2

* 10 Cleaned Datasets Generated
* SQLite Database Created
* Database Schema Designed
* SQL Queries Developed
* Data Dictionary Prepared
* Validation Checks Completed

---

# Upcoming Work

### Day 3

* Exploratory Data Analysis (EDA)
* Trend Analysis
* Category Analysis
* Investor Behavior Analysis

### Day 4

* Performance Analytics
* Sharpe Ratio Analysis
* Alpha/Beta Analysis
* Risk Metrics

### Day 5

* Advanced Analytics
* Recommendation Engine
* Predictive Insights

### Day 6

* Dashboard Development
* KPI Monitoring
* Interactive Visualizations

### Day 7

* Final Report
* Presentation
* Project Submission

---

# Conclusion

This project demonstrates the complete lifecycle of a financial analytics solution, starting from raw mutual fund datasets and progressing toward a fully structured analytics platform capable of supporting investment decision-making, performance monitoring, and business intelligence reporting.

The project emphasizes data quality, reproducibility, scalability, and analytical rigor while following industry-standard data engineering and analytics practices.
