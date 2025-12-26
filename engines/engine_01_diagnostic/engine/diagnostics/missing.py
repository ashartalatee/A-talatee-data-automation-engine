import pandas as pd

def detect_missing(df: pd.DataFrame) -> dict:
    """
    Menghitung missing value per kolom.
    Tidak menyimpan state.
    Tidak mengubah data.
    """

    total_rows = len(df)

    result = {}

    for col in df.columns:
        missing_count = int(df[col].isnull().sum())
        missing_pct = round(
            (missing_count / total_rows * 100) if total_rows > 0 else 0,
            2
        )

        result[col] = {
            "missing_count": missing_count,
            "missing_percentage": missing_pct
        }

    return result
