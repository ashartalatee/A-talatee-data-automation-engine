import pandas as pd


class SchemaDiagnostic:
    """
    Mendeteksi inkonsistensi schema:
    - nama kolom
    - duplikasi kolom
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> dict:
        columns = list(self.df.columns)

        duplicate_columns = list(
            set([col for col in columns if columns.count(col) > 1])
        )

        normalized = [col.strip().lower() for col in columns]
        inconsistent_columns = (
            len(normalized) != len(set(normalized))
        )

        return {
            "total_columns": len(columns),
            "duplicate_columns": duplicate_columns,
            "inconsistent_naming": inconsistent_columns,
        }


# PUBLIC ENGINE API
def detect_schema(df: pd.DataFrame) -> dict:
    diagnostic = SchemaDiagnostic(df)
    return diagnostic.analyze()
