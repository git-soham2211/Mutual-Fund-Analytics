import pandas as pd
from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RAW = BASE_DIR / "data" / "raw"
PROCESSED = BASE_DIR / "data" / "processed"

PROCESSED.mkdir(exist_ok=True)

# =============================
# 1. CLEAN NAV HISTORY
# =============================

print("Cleaning NAV History...")

nav = pd.read_csv(RAW / "02_nav_history.csv")

# convert date

nav["date"] = pd.to_datetime(nav["date"])

# sort

nav = nav.sort_values(
    ["amfi_code", "date"]
)

# remove duplicates

nav = nav.drop_duplicates()

# validate nav > 0

nav = nav[nav["nav"] > 0]

# forward fill NAV

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav.to_csv(
    PROCESSED / "02_nav_history_clean.csv",
    index=False
)

print("NAV History Cleaned")


# =============================
# 2. CLEAN INVESTOR TRANSACTIONS
# =============================

print("Cleaning Investor Transactions...")

txn = pd.read_csv(
    RAW / "08_investor_transactions.csv"
)

# standardize transaction type

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

# validate amount

txn = txn[
    txn["amount_inr"] > 0
]

# convert date

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# valid kyc values

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

txn = txn[
    txn["kyc_status"].isin(valid_kyc)
]

txn.to_csv(
    PROCESSED /
    "08_investor_transactions_clean.csv",
    index=False
)

print("Investor Transactions Cleaned")


# =============================
# 3. CLEAN SCHEME PERFORMANCE
# =============================

print("Cleaning Scheme Performance...")

perf = pd.read_csv(
    RAW / "07_scheme_performance.csv"
)

numeric_cols = [

    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"

]

for col in numeric_cols:

    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# expense ratio validation

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    PROCESSED /
    "07_scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance Cleaned")

print("\nDAY 2 CLEANING COMPLETED")