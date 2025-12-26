class RiskClassifier:
    """
    Mengklasifikasikan tingkat risiko dataset
    berdasarkan skor kualitas keseluruhan dan kolom terburuk.
    """

    def __init__(
        self,
        dataset_quality_score: float,
        worst_column_score: int
    ):
        self.dataset_quality_score = dataset_quality_score
        self.worst_column_score = worst_column_score

    def classify(self) -> dict:
        # Kondisi KRITIS: bom waktu
        if self.dataset_quality_score < 60 or self.worst_column_score < 40:
            level = "CRITICAL"
            message = (
                "Data berisiko tinggi dan tidak disarankan "
                "digunakan tanpa perbaikan signifikan."
            )

        # Kondisi RISIKO: bisa lanjut dengan catatan
        elif self.dataset_quality_score < 80:
            level = "RISK"
            message = (
                "Data memiliki risiko dan perlu perhatian "
                "sebelum digunakan untuk keputusan penting."
            )

        # Kondisi AMAN: layak lanjut
        else:
            level = "SAFE"
            message = (
                "Data relatif aman dan layak digunakan "
                "untuk analisis lanjutan."
            )

        return {
            "risk_level": level,
            "risk_message": message
        }
