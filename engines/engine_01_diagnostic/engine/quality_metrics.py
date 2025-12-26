from dataclasses import dataclass


@dataclass(frozen=True)
class QualityThreshold:
    """
    Batas toleransi kualitas data.
    Semua nilai dalam persentase (%).
    """
    warning: float
    critical: float


class DataQualityMetrics:
    """
    Definisi metrik kualitas data.
    Tidak melakukan scoring atau keputusan.
    """

    # Missing value thresholds
    MISSING_VALUE = QualityThreshold(
        warning=5.0,
        critical=20.0
    )

    # Duplicate row thresholds
    DUPLICATE_ROW = QualityThreshold(
        warning=1.0,
        critical=5.0
    )

    # Encoding issue thresholds
    ENCODING_ISSUE = QualityThreshold(
        warning=2.0,
        critical=10.0
    )
