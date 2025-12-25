import pandas as pd

class SchemaDiagnostic:
    """
    Menganalisis konsistensi schema dataset:
    - nama kolom
    - tipe data
    - jumlah nilai unik
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def analyze(self) -> pd.DataFrame:
        report = pd.DataFrame({
            "column_name": self.df.columns,
            "data_type": self.df.dtypes.astype(str),
            "non_null_count": self.df.notnull().sum(),
            "unique_count": self.df.nunique(dropna=True)
        })

        return report