import yaml
import pandas as pd
from src.utils import setup_logger, log_rule

logger = setup_logger("format_validation")

# Load rule YAML
with open("rules/format_validation.yaml") as f:
    rules = yaml.safe_load(f)


def validate_dates(df):
    """
    Validasi dan standardisasi format date (schema-aware)
    """
    applied_cols = []

    for col_rule in rules.get("date_format", {}).get("columns", []):
        col = col_rule["name"]
        fmt = col_rule.get("format")

        if col not in df.columns:
            logger.warning(f"[DATE] Column '{col}' not found — skipped")
            continue

        df[col] = pd.to_datetime(df[col], errors="coerce")

        if fmt:
            df[col] = df[col].dt.strftime(fmt)

        applied_cols.append(col)

    log_rule("date_format", applied_cols)
    return df


def validate_numeric(df):
    """
    Validasi numeric range & null (schema-aware)
    """
    applied_cols = []

    for col_rule in rules.get("numeric_validation", {}).get("columns", []):
        col = col_rule["name"]

        if col not in df.columns:
            logger.warning(f"[NUMERIC] Column '{col}' not found — skipped")
            continue

        min_val = col_rule.get("min")
        max_val = col_rule.get("max")
        allow_null = col_rule.get("allow_null", True)

        if not allow_null:
            df[col] = df[col].fillna(0)

        if min_val is not None:
            df[col] = df[col].apply(lambda x: max(x, min_val))

        if max_val is not None:
            df[col] = df[col].apply(lambda x: min(x, max_val))

        applied_cols.append(col)

    log_rule("numeric_validation", applied_cols)
    return df
