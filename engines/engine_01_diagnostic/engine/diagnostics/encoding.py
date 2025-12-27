import pandas as pd


class EncodingDiagnostic:
    """
    Mendeteksi potensi masalah encoding
    pada kolom bertipe object/string.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> dict:
        encoding_issues = []

        for col in self.df.select_dtypes(include=["object"]).columns:
            try:
                # coba encode-decode sederhana
                self.df[col].astype(str).str.encode("utf-8")
            except Exception:
                encoding_issues.append(col)

        return {
            "string_columns": list(
                self.df.select_dtypes(include=["object"]).columns
            ),
            "encoding_issue_columns": encoding_issues,
            "has_encoding_issue": len(encoding_issues) > 0,
        }


# PUBLIC ENGINE API (WAJIB)
def detect_encoding(df: pd.DataFrame) -> dict:
    """
    Public facade untuk encoding diagnostic.
    """
    diagnostic = EncodingDiagnostic(df)
    return diagnostic.analyze()
