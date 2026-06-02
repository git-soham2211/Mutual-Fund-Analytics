import pandas as pd
import os

data_folder = "../data/raw"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

print(f"\nTotal Files Found: {len(csv_files)}")

for file in csv_files:

    print("\n" + "="*70)

    filepath = os.path.join(data_folder, file)

    try:

        df = pd.read_csv(filepath)

        print(f"Dataset: {file}")

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(list(df.columns))

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:

        print(f"Error reading {file}")
        print(e)

    print("="*70)