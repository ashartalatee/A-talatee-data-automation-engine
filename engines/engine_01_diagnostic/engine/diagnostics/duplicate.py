import pandas as pd

class DuplicateRowDiagnostic:
    """
    Mendeteksi duplicate row pada dataset
    tanpa mengubbah atau menghapus data.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> dict:
        total_rows = len(self.df)

        duplicate_mask = self.df.duplicated()
        duplicate_count = duplicate_mask.sum()

        duplicate_percentage = (
            duplicate_count / total_rows * 100
        ).round(2) if total_rows > 0 else 0.0

        return {
            "total_rows": total_rows,
            "duplicate_rows": int(duplicate_count),
            "duplicate_percentage": duplicate_percentage
        }