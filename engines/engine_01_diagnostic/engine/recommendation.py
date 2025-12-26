class RecommendationEngine:
    """
    Memberikan rekomendasi langkah lanjutan
    berdasarkan risk level dan business impact.
    Tidak melakukan perubahan data.
    """

    RECOMMENDATION_MAP = {
        "SAFE": [
            "Dataset dapat digunakan untuk analisis lanjutan",
            "Tetap lakukan monitoring kualitas data secara berkala",
            "Dokumentasikan asumsi penggunaan data"
        ],
        "RISK": [
            "Lakukan validasi tambahan pada kolom bermasalah",
            "Pertimbangkan pembersihan data terbatas sebelum analisis",
            "Diskusikan risiko dengan stakeholder sebelum keputusan dibuat"
        ],
        "CRITICAL": [
            "Tunda penggunaan dataset untuk keputusan strategis",
            "Lakukan data cleaning menyeluruh atau pengambilan ulang data",
            "Evaluasi ulang sumber dan proses pengumpulan data"
        ]
    }

    def __init__(self, risk_level: str):
        self.risk_level = risk_level

    def generate(self) -> dict:
        recommendations = self.RECOMMENDATION_MAP.get(
            self.risk_level,
            ["Tidak ada rekomendasi yang tersedia"]
        )

        return {
            "risk_level": self.risk_level,
            "recommendations": recommendations
        }
