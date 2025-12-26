import pandas as pd
from engine.quality_metrics import DataQualityMetrics


class ColumnQualityScorer:
    """
    Menghitung skor kualitas per kolom berdasarkan
    missing value dan encoding risk.
    Skor 0–100 (semakin tinggi semakin baik).
    """

    def __init__(
        self,
        missing_report: pd.DataFrame,
        encoding_report: pd.DataFrame
    ):
        self.missing_report = missing_report
        self.encoding_report = encoding_report

    def score(self) -> pd.DataFrame:
        scores = []

        encoding_map = {
            row["column_name"]: row["non_ascii_percentage"]
            for _, row in self.encoding_report.iterrows()
        }

        for _, row in self.missing_report.iterrows():
            column = row["column_name"]
            missing_pct = row["missing_percentage"]
            encoding_pct = encoding_map.get(column, 0.0)

            score = 100

            # Missing value penalty
            if missing_pct >= DataQualityMetrics.MISSING_VALUE.critical:
                score -= 40
            elif missing_pct >= DataQualityMetrics.MISSING_VALUE.warning:
                score -= 20

            # Encoding penalty
            if encoding_pct >= DataQualityMetrics.ENCODING_ISSUE.critical:
                score -= 30
            elif encoding_pct >= DataQualityMetrics.ENCODING_ISSUE.warning:
                score -= 10

            scores.append({
                "column_name": column,
                "missing_percentage": missing_pct,
                "encoding_risk_percentage": encoding_pct,
                "quality_score": max(score, 0)
            })

        return pd.DataFrame(scores).sort_values(
            by="quality_score",
            ascending=False
        )


# DAY 10 — DATASET LEVEL

class DatasetQualityScorer:
    """
    Menghitung skor kualitas dataset secara keseluruhan
    berdasarkan skor kualitas tiap kolom.
    """

    def __init__(self, column_score_df: pd.DataFrame):
        self.column_score_df = column_score_df

    def score(self) -> dict:
        if self.column_score_df.empty:
            raise ValueError(
                "Column score kosong. Tidak bisa menghitung dataset score."
            )

        avg_score = self.column_score_df["quality_score"].mean()
        min_score = self.column_score_df["quality_score"].min()

        return {
            "dataset_quality_score": round(avg_score, 2),
            "worst_column_score": int(min_score),
            "total_columns": int(self.column_score_df.shape[0])
        }
