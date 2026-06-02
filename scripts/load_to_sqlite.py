import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"
DB = BASE_DIR / "data" / "db" / "bluestock_mf.db"

engine = create_engine(
    f"sqlite:///{DB}"
)

print("Loading Tables...")

# dim_fund
fund = pd.read_csv(
    RAW / "01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# fact_nav
nav = pd.read_csv(
    PROCESSED /
    "02_nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# fact_aum
aum = pd.read_csv(
    RAW / "03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

# fact_transactions
txn = pd.read_csv(
    PROCESSED /
    "08_investor_transactions_clean.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

# fact_performance
perf = pd.read_csv(
    PROCESSED /
    "07_scheme_performance_clean.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")

print(DB)