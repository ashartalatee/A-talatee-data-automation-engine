import yaml
import pandas as pd
import os
from utils import setup_logger, log_rule, generate_report

# Setup Logging
os.makedirs("logs", exist_ok=True)
setup_logger(log_file="logs/cleaning.log")

# Load Rule YAML
with open("rules/missing_duplicates.yaml") as f:
    rules = yaml.safe_load(f)

# Function: Clean Missing Values
def clean_missing(df):
    """
    Bersihkan missing values berdasarkan rules
    """
    for col_rule in rules["missing_values"]["columns"]:
        col = col_rule["name"]
        strategy = col_rule["strategy"]

        if col not in df.columns:
            log_rule("clean_missing", f"Kolom '{col}' tidak ada di dataset")
            continue

        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
            log_rule("clean_missing", f"Kolom '{col}' diisi mean")
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
            log_rule("clean_missing", f"Kolom '{col}' diisi median")
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
            log_rule("clean_missing", f"Kolom '{col}' diisi mode")
        elif strategy == "constant":
            fill_val = col_rule.get("fill_value")
            df[col].fillna(fill_val, inplace=True)
            log_rule("clean_missing", f"Kolom '{col}' diisi constant: {fill_val}")
    return df

# Main Script
if __name__ == "__main__":
    # Baca dataset
    input_file = "sample_data/example_dataset.csv"
    output_file = "sample_data/example_dataset_cleaned_partial.csv"
    report_file = "sample_data/report.csv"

    df = pd.read_csv(input_file)
    print("Sebelum clean missing values:")
    print(df.head())

    # Copy untuk report
    df_before = df.copy()

    # Bersihkan missing values
    df_cleaned = clean_missing(df)

    # Generate report
    generate_report(df_before, df_cleaned, rule_name="clean_missing", report_file=report_file)

    print("\nSetelah clean missing values:")
    print(df_cleaned.head())

    # Simpan hasil bersih
    df_cleaned.to_csv(output_file, index=False)
    log_rule("clean_missing", f"Hasil clean missing disimpan di {output_file}")
