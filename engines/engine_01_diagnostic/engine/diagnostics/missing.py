import pandas as pd

class MissingValueDiagnostic:
    """
    Mendeteksi dan melaporkan missing value per kolom
    tanpa mengubah data asli.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> pd.DataFrame:
        total_rows = len(self.df)

        report = (
            self.df.isnull()
            .sum()
            .reset_index()
            .rename(columns={
                "index": "column_name",
                0: "missing_count"
            })
        )

        report["missing_percentage"] = (
            report["missing_count"] / total_rows * 100
        ).round(2)

        report = report.sort_values(
            by="missing_percentage",
            ascending=False
        )

        return report