class BusinessImpactMapper:
    """
    Memetakan risk level dataset ke dampak bisnis potensial.
    Tidak memberi rekomendasi teknis, hanya konsekuensi.
    """

    IMPACT_MAP = {
        "SAFE": [
            "Analisis dan laporan cenderung stabil",
            "Keputusan bisnis dapat dibuat dengan tingkat kepercayaan tinggi",
            "Risiko kesalahan operasional relatif rendah"
        ],
        "RISK": [
            "Hasil analisis berpotensi bias atau tidak konsisten",
            "Keputusan bisnis perlu validasi tambahan",
            "Ada risiko koreksi di tahap lanjutan"
        ],
        "CRITICAL": [
            "Hasil analisis berpotensi menyesatkan",
            "Keputusan bisnis berisiko salah arah",
            "Potensi kerugian waktu, biaya, dan reputasi"
        ]
    }

    def __init__(self, risk_level: str):
        self.risk_level = risk_level

    def map(self) -> dict:
        impacts = self.IMPACT_MAP.get(
            self.risk_level,
            ["Dampak bisnis tidak terdefinisi"]
        )

        return {
            "risk_level": self.risk_level,
            "business_impacts": impacts
        }
