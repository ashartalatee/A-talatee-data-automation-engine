import yaml
import pandas as pd
import os
from src.utils import setup_logger, log_rule, generate_report


# Setup Logging
os.makedirs("logs", exist_ok=True)
setup_logger(log_file="logs/cleaning.log")


# Load Rules
with open("rules/missing_duplicates.yaml") as f:
    rules = yaml.safe_load(f)


# Function: Clean Missing Values
def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Bersihkan missing values berdasarkan rules YAML
    """
    for col_rule in rules["missing_values"]["columns"]:
        col = col_rule["name"]
        strategy = col_rule["strategy"]

        if col not in df.columns:
            log_rule("clean_missing", f"Kolom '{col}' tidak ada di dataset — dilewati")
            continue

        if strategy == "mean":
            value = df[col].mean()
            df[col] = df[col].fillna(value)
            log_rule("clean_missing", f"Kolom '{col}' diisi mean: {value}")

        elif strategy == "median":
            value = df[col].median()
            df[col] = df[col].fillna(value)
            log_rule("clean_missing", f"Kolom '{col}' diisi median: {value}")

        elif strategy == "mode":
            value = df[col].mode().iloc[0]
            df[col] = df[col].fillna(value)
            log_rule("clean_missing", f"Kolom '{col}' diisi mode: {value}")

        elif strategy == "constant":
            value = col_rule.get("fill_value")
            df[col] = df[col].fillna(value)
            log_rule("clean_missing", f"Kolom '{col}' diisi constant: {value}")

        else:
            log_rule(
                "clean_missing",
                f"Strategy '{strategy}' tidak dikenali untuk kolom '{col}'"
            )

    return df


# Main Script (Manual Test)
if __name__ == "__main__":
    input_file = "sample_data/example_dataset.csv"
    output_file = "sample_data/example_dataset_cleaned_partial.csv"
    report_file = "sample_data/report.csv"

    df = pd.read_csv(input_file)
    print("Sebelum clean missing values:")
    print(df.head())

    df_before = df.copy()

    df_cleaned = clean_missing(df)

    generate_report(
        df_before,
        df_cleaned,
        rule_name="clean_missing",
        report_file=report_file
    )

    print("\nSetelah clean missing values:")
    print(df_cleaned.head())

    df_cleaned.to_csv(output_file, index=False)
    log_rule("clean_missing", f"Hasil clean missing disimpan di {output_file}")
