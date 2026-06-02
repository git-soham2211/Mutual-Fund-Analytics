# Mutual Fund Analytics Capstone Project

## Bluestock Internship

### Project Overview

This project focuses on Mutual Fund Analytics using Python, Pandas, and real-world mutual fund datasets.

The objective is to build an end-to-end analytics pipeline covering:

* Data Ingestion (ETL)
* Data Validation
* NAV Analysis
* Fund Performance Analysis
* Portfolio Holdings Analysis
* SIP & Industry Trends
* Dashboard Development

---

## Day 1 Deliverables

### Project Setup

* Created project folder structure
* Configured Python virtual environment
* Installed required libraries

### Data Ingestion

Loaded and analyzed 10 datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

### Data Validation

* Checked dataset dimensions
* Verified data types
* Identified missing values
* Performed AMFI code validation

### Key Findings

* All 40 AMFI scheme codes are present in NAV history
* Only one anomaly detected:

  * 12 missing values in `yoy_growth_pct` column of Monthly SIP Inflows dataset

### Technologies Used

* Python
* Pandas
* NumPy
* Requests
* SQLAlchemy
* Jupyter Notebook
* Git & GitHub

---

## Repository Structure

data/

reports/

scripts/

requirements.txt

---

## Author

Soham Srivastava

Bluestock Internship - Mutual Fund Analytics Project
