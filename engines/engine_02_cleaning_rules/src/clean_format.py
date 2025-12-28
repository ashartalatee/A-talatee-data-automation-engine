import yaml
import pandas as pd

# Load rule YAML
with open("rules/format_validation.yaml") as f:
    rules = yaml.safe_load(f)

def validate_dates(df):
    """
    Validasi dan standardisasi format date
    """
    for col_rule in rules["date_format"]["columns"]:
        col = col_rule["name"]
        fmt = col_rule["format"]
        df[col] = pd.to_datetime(df[col], errors='coerce')  # coerce invalid dates
        df[col] = df[col].dt.strftime(fmt)  # ubah ke format standar
    return df

def validate_numeric(df):
    """
    Validasi numeric range dan null
    """
    for col_rule in rules["numeric_validation"]["columns"]:
        col = col_rule["name"]
        min_val = col_rule.get("min")
        max_val = col_rule.get("max")
        allow_null = col_rule.get("allow_null", True)

        # Non-null check
        if not allow_null:
            df[col].fillna(0, inplace=True)  # default fill 0 jika null

        # Range validation
        if min_val is not None:
            df[col] = df[col].apply(lambda x: x if x >= min_val else min_val)
        if max_val is not None:
            df[col] = df[col].apply(lambda x: x if x <= max_val else max_val)
    return df

# Contoh penggunaan
if __name__ == "__main__":
    df = pd.read_csv("sample_data/example_dataset_cleaned_v2.csv")
    print("Sebelum format validation:")
    print(df.head())

    df = validate_dates(df)
    df = validate_numeric(df)

    print("\nSetelah format validation:")
    print(df.head())

    # Simpan hasil parsial
    df.to_csv("sample_data/example_dataset_cleaned_v3.csv", index=False)
