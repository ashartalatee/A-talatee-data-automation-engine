import logging
import pandas as pd
from datetime import datetime

# Setup logging
def setup_logger(log_file="logs/cleaning.log"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

# Logging per rule
def log_rule(rule_name, message):
    logging.info(f"[{rule_name}] {message}")

# Generate simple report
def generate_report(df_before, df_after, rule_name, report_file="sample_data/report.csv"):
    """
    Membuat report sederhana: perbedaan jumlah missing / duplikat sebelum & sesudah rule
    """
    report = {
        "rule": rule_name,
        "rows_before": df_before.shape[0],
        "rows_after": df_after.shape[0],
        "columns_before": df_before.shape[1],
        "columns_after": df_after.shape[1],
        "missing_before": df_before.isnull().sum().sum(),
        "missing_after": df_after.isnull().sum().sum()
    }
    report_df = pd.DataFrame([report])
    
    try:
        existing = pd.read_csv(report_file)
        report_df = pd.concat([existing, report_df], ignore_index=True)
    except FileNotFoundError:
        pass
    
    report_df.to_csv(report_file, index=False)
