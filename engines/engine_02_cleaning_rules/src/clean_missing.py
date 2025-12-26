import yaml
import pandas as pd

# Load rule YAML
with open("rules/missing_duplicates.yaml") as f:
    rules = yaml.safe_load(f)

def clean_missing(df):
    for col_rule in rules["missing_values"]["columns"]:
        col = col_rule["name"]
        strategy = col_rule["strategy"]
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == "constant":
            df[col].fillna(col_rule.get("fill_value"), inplace=True)
    
    return df

def remove_duplicates(df):
    subset = rules["duplicates"]["subset"]
    keep = rules["duplicates"]["keep"]
    df = df.drop_duplicates(subset=subset, keep=keep)
    return df

# Contoh penggunaan
if __name__ == "__main__":
    df = pd.read_csv("sample_data.csv")
    df = clean_missing(df)
    df = remove_duplicates(df)
    print(df.head())