import pandas as pd
import os

data_folder = "../data/raw"

report = []

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

for file in csv_files:

    df = pd.read_csv(os.path.join(data_folder,file))

    report.append(f"\nDataset : {file}")
    report.append(f"Rows : {df.shape[0]}")
    report.append(f"Columns : {df.shape[1]}")
    report.append(f"Missing Values : {df.isnull().sum().sum()}")
    report.append(f"Duplicates : {df.duplicated().sum()}")

with open("../reports/data_quality_report.txt","w") as f:
    f.write("\n".join(report))

print("Data Quality Report Generated Successfully")