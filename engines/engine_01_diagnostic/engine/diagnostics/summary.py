import pandas as pd
from typing import Dict


class SummaryDiagnostic:
    """
    Menggabungkan hasil diagnostic menjadi ringkasan terpadu.
    Tidak mengambil keputusan, hanya menyatukan fakta.
    """

    def __init__(
        self,
        missing_report: pd.DataFrame,
        duplicate_report: Dict,
        schema_report: pd.DataFrame,
        encoding_report: pd.DataFrame,
    ):
        self.missing_report = missing_report
        self.duplicate_report = duplicate_report
        self.schema_report = schema_report
        self.encoding_report = encoding_report

    def generate(self) -> Dict:
        return {
            "missing": {
                "total_columns": int(self.missing_report.shape[0]),
                "columns_with_missing": int(
                    (self.missing_report["missing_count"] > 0).sum()
                ),
                "max_missing_percentage": float(
                    self.missing_report["missing_percentage"].max()
                ),
            },
            "duplicate": self.duplicate_report,
            "schema": {
                "total_columns": int(self.schema_report.shape[0]),
                "object_columns": int(
                    (self.schema_report["data_type"] == "object").sum()
                ),
            },
            "encoding": {
                "columns_checked": int(self.encoding_report.shape[0]),
                "columns_with_non_ascii": int(
                    (self.encoding_report["non_ascii_count"] > 0).sum()
                ),
                "max_non_ascii_percentage": float(
                    self.encoding_report["non_ascii_percentage"].max()
                ) if not self.encoding_report.empty else 0.0,
            },
        }
