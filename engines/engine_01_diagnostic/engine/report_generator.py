from datetime import datetime

class FinalReportGenerator:
    def __init__(
        self,
        dataset_name: str,
        summary: dict,
        scores: dict,
        risk: str,
        business_impact: dict,
        recommendations: list
    ):
        self.dataset_name = dataset_name
        self.summary = summary
        self.scores = scores
        self.risk = risk
        self.business_impact = business_impact
        self.recommendations = recommendations

    def generate_markdown(self) -> str:
        return f"""
# 📊 Raw Data Diagnostic Report

## Dataset
**Nama File**: {self.dataset_name}

## Ringkasan Diagnostic
{self.summary}

## Skor Kualitas Data
- **Skor Dataset**: {self.scores["dataset_score"]["dataset_quality_score"]}
- **Skor Terburuk Kolom**: {self.scores["dataset_score"]["worst_column_score"]}
- **Jumlah Kolom**: {self.scores["dataset_score"]["total_columns"]}

## Risiko Data
**Kategori Risiko**: {self.risk}

## Dampak Bisnis
{self.business_impact.get("description", "")}

## Rekomendasi
""" + "\n".join(f"- {rec}" for rec in self.recommendations)
