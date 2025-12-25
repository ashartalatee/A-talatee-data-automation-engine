import pandas as pd
import re


class EncodingDiagnostic:
    """
    Mendeteksi potensi masalah encoding dengan mencari
    karakter non-ASCII dan simbol aneh pada kolom object/string.
    """

    NON_ASCII_PATTERN = re.compile(r"[^\x00-\x7F]")

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> pd.DataFrame:
        object_columns = self.df.select_dtypes(include=["object"]).columns

        records = []

        for col in object_columns:
            series = self.df[col].dropna().astype(str)

            non_ascii_count = series.apply(
                lambda x: bool(self.NON_ASCII_PATTERN.search(x))
            ).sum()

            records.append({
                "column_name": col,
                "non_ascii_count": int(non_ascii_count),
                "total_non_null": int(series.shape[0]),
                "non_ascii_percentage": round(
                    (non_ascii_count / series.shape[0]) * 100, 2
                ) if series.shape[0] > 0 else 0.0
            })

        return pd.DataFrame(records).sort_values(
            by="non_ascii_percentage",
            ascending=False
        )
