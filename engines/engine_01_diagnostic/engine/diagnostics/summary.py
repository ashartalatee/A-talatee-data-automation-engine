from typing import Dict


class SummaryDiagnostic:
    """
    Menggabungkan hasil diagnostic menjadi ringkasan fakta tingkat dataset.
    Tidak menganalisis ulang dan tidak mengambil keputusan.
    """

    def __init__(self, diagnostics: Dict):
        """
        diagnostics: dict berisi hasil diagnostic mentah
        dari masing-masing modul.
        """
        self.diagnostics = diagnostics

    def generate(self) -> Dict:
        return {
            "missing": self._summarize_missing(),
            "duplicate": self.diagnostics.get("duplicate", {}),
            "schema": self._summarize_schema(),
            "encoding": self._summarize_encoding(),
        }

    def _summarize_missing(self) -> Dict:
        data = self.diagnostics.get("missing", {})

        return {
            "total_columns": data.get("total_columns", 0),
            "columns_with_missing": data.get("columns_with_missing", 0),
            "max_missing_percentage": data.get("max_missing_percentage", 0.0),
        }

    def _summarize_schema(self) -> Dict:
        data = self.diagnostics.get("schema", {})

        return {
            "total_columns": data.get("total_columns", 0),
            "object_columns": data.get("object_columns", 0),
        }

    def _summarize_encoding(self) -> Dict:
        data = self.diagnostics.get("encoding", {})

        return {
            "columns_checked": data.get("columns_checked", 0),
            "columns_with_non_ascii": data.get("columns_with_non_ascii", 0),
            "max_non_ascii_percentage": data.get(
                "max_non_ascii_percentage", 0.0
            ),
        }
