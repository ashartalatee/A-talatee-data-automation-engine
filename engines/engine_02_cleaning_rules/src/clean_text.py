import yaml
import pandas as pd

with open("rules/text_mapping.yaml") as f:
    rules = yaml.safe_load(f)

def clean_text(df):
    text_rules = rules.get("text_cleaning", {})

    normalize = text_rules.get("normalize", {})
    lowercase = normalize.get("lowercase", False)
    strip_ws = normalize.get("strip_whitespace", False)

    for col_rule in text_rules.get("columns", []):
        col = col_rule["name"]

        if col not in df.columns:
            continue

        # Convert to string
        df[col] = df[col].astype(str)

        if strip_ws:
            df[col] = df[col].str.strip()

        if lowercase:
            df[col] = df[col].str.lower()

        # Mapping value
        mapping = col_rule.get("mapping", {})
        for canonical, variants in mapping.items():
            df[col] = df[col].replace(variants, canonical)

    return df
