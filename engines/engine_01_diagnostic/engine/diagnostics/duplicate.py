import pandas as pd


class DuplicateRowDiagnostic:
    """
    Mendeteksi duplicate row pada dataset
    tanpa mengubah atau menghapus data.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> dict:
        total_rows = len(self.df)

        duplicate_mask = self.df.duplicated()
        duplicate_count = duplicate_mask.sum()

        duplicate_percentage = (
            round(duplicate_count / total_rows * 100, 2)
            if total_rows > 0 else 0.0
        )

        return {
            "total_rows": total_rows,
            "duplicate_rows": int(duplicate_count),
            "duplicate_percentage": duplicate_percentage,
            "has_duplicate": duplicate_count > 0,
        }


# PUBLIC ENGINE API (WAJIB ADA)
def detect_duplicate(df: pd.DataFrame) -> dict:
    """
    Public facade untuk duplicate diagnostic.
    """
    diagnostic = DuplicateRowDiagnostic(df)
    return diagnostic.analyze()
