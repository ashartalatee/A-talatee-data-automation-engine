import pandas as pd
from engine.quality_metrics import DataQualityMetrics


# =====================================================
# COLUMN LEVEL SCORING
# =====================================================

class ColumnQualityScorer:
    """
    Menghitung skor kualitas per kolom berdasarkan:
    - missing value
    - encoding risk

    Skor 0–100 (semakin tinggi semakin baik)
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

            if missing_pct >= DataQualityMetrics.MISSING_VALUE.critical:
                score -= 40
            elif missing_pct >= DataQualityMetrics.MISSING_VALUE.warning:
                score -= 20

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

        return (
            pd.DataFrame(scores)
            .sort_values(by="quality_score", ascending=False)
            .reset_index(drop=True)
        )


# =====================================================
# DATASET LEVEL SCORING
# =====================================================

class DatasetQualityScorer:
    """
    Menghitung skor kualitas dataset secara keseluruhan
    berdasarkan skor kualitas tiap kolom
    """

    def __init__(self, column_score_df: pd.DataFrame):
        self.column_score_df = column_score_df

    def score(self) -> dict:
        if self.column_score_df.empty:
            raise ValueError("Column score kosong.")

        return {
            "dataset_quality_score": round(
                self.column_score_df["quality_score"].mean(), 2
            ),
            "worst_column_score": int(
                self.column_score_df["quality_score"].min()
            ),
            "total_columns": int(self.column_score_df.shape[0])
        }


def classify_risk(score: float) -> str:
    if score >= 85:
        return "LOW"
    elif score >= 65:
        return "MEDIUM"
    return "HIGH"


# =====================================================
# PUBLIC FACADE (CLI ENTRY POINT)
# =====================================================

def score_dataset(
    df: pd.DataFrame,
    diagnostics: dict,
    config: dict | None = None
) -> dict:
    """
    Facade function:
    diagnostics → column scoring → dataset scoring → risk
    """

    missing_report = diagnostics.get("missing")
    encoding_report = diagnostics.get("encoding")

    if missing_report is None:
        raise ValueError("Missing report tidak ditemukan")

    # Normalize missing
    if isinstance(missing_report, dict):
        missing_report = pd.DataFrame([
            {
                "column_name": col,
                "missing_percentage": (
                    info["missing_percentage"]
                    if isinstance(info, dict)
                    else info
                )
            }
            for col, info in missing_report.items()
        ])

    # Normalize encoding
    if encoding_report is None:
        encoding_report = pd.DataFrame(
            columns=["column_name", "non_ascii_percentage"]
        )
    elif isinstance(encoding_report, dict):
        encoding_report = pd.DataFrame([
            {
                "column_name": col,
                "non_ascii_percentage": pct
            }
            for col, pct in encoding_report.items()
        ])

    column_scores = ColumnQualityScorer(
        missing_report=missing_report,
        encoding_report=encoding_report
    ).score()

    dataset_score = DatasetQualityScorer(
        column_scores
    ).score()

    risk_level = classify_risk(
        dataset_score["dataset_quality_score"]
    )

    return {
        "dataset_score": dataset_score,
        "risk": risk_level,
        "column_scores": column_scores
    }
