import yaml
import pandas as pd

# Load rule YAML
with open("rules/missing_duplicates.yaml") as f:
    rules = yaml.safe_load(f)

def remove_duplicates(df):
    """
    Hapus duplikat berdasarkan rule yaml
    """
    subset = rules["duplicates"]["subset"]
    keep = rules["duplicates"]["keep"]
    df = df.drop_duplicates(subset=subset, keep=keep)
    return df

def standardize_columns(df):
    """
    Standarisasi nama kolom: lowercase, spasi underscore
    """
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

# contoh penggunaan
if __name__ == "__main__":
    df = pd.read_csv("sample_data/example_dataset_cleanet_partial.csv")
    print("Sebelum duplikat & standardisasi:")
    print(df.head())

    df = remove_duplicates(df)
    df = standardize_columns(df)

    print("\nSetelah duplikat & standardisasi:")
    print(df.head())

    # Simpan hasil parsial
    df.to_csv("sample_data/example_dataset_cleaned_v2.csv", index=False)