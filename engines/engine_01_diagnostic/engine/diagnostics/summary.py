from typing import Dict


class SummaryDiagnostic:
    """
    Menggabungkan seluruh hasil diagnostic
    menjadi ringkasan yang mudah dibaca.
    """

    def __init__(self, diagnostics: Dict[str, dict]):
        self.diagnostics = diagnostics

    def analyze(self) -> dict:
        issues = []

        if self.diagnostics.get("missing", {}).get("has_missing"):
            issues.append("Missing values detected")

        if self.diagnostics.get("duplicate", {}).get("has_duplicate"):
            issues.append("Duplicate rows detected")

        if self.diagnostics.get("schema", {}).get("inconsistent_naming"):
            issues.append("Schema inconsistency detected")

        if self.diagnostics.get("encoding", {}).get("has_encoding_issue"):
            issues.append("Encoding issues detected")

        return {
            "total_checks": len(self.diagnostics),
            "issues_found": issues,
            "has_issue": len(issues) > 0,
        }


# PUBLIC ENGINE API (WAJIB ADA)
def generate_summary(diagnostics: Dict[str, dict]) -> dict:
    """
    Public facade untuk summary diagnostic.
    """
    summary = SummaryDiagnostic(diagnostics)
    return summary.analyze()
