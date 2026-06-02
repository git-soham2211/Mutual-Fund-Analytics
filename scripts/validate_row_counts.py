import pandas as pd
import sqlite3

conn = sqlite3.connect("../data/db/bluestock_mf.db")

checks = [
    ("../data/processed/01_fund_master_clean.csv", "dim_fund"),
    ("../data/processed/02_nav_history_clean.csv", "fact_nav"),
    ("../data/processed/03_aum_by_fund_house_clean.csv", "fact_aum"),
    ("../data/processed/08_investor_transactions_clean.csv", "fact_transactions"),
    ("../data/processed/07_scheme_performance_clean.csv", "fact_performance"),
]

print("\nROW COUNT VALIDATION\n")
print("-" * 50)

for csv_file, table in checks:

    csv_rows = len(pd.read_csv(csv_file))

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        conn
    )["cnt"][0]

    status = "PASS" if csv_rows == db_rows else "FAIL"

    print(
        f"{table:<20} CSV={csv_rows:<8} DB={db_rows:<8} {status}"
    )

conn.close()