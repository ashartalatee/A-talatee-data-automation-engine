import pandas as pd
from pathlib import Path

class DataLoader:
    """
    DatLoader bertugas membaca data mentah tanpa mengubah isi.
    jika data tidak bisa dibaca dengan aman, loader harus gagal dengan jelas.
    """

    SUPPORTED_EXTENSIONS = [".csv", "xlsx", ".xls"]

    def validate_file(self):
        if not self.file_path.exists():
            raise FileNotFoundError(f"File tidak ditemukan: {self.file_path}")
        
        if self.file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Format tidak didukung: {self.file_path.suffix}. "
                f"Gunakan CSV atau Excel."
            )
    
    def load(self) -> pd.DataFrame:
        self.validate_file()

        try:
            if self.file_path.suffix.lower() == ".csv":
                df = pd.read_csv(self.file_path)
            else:
                df = pd.read_excel(self.file_path)

        except Exception as e:
            raise RuntimeError(
                f"Gagal membaca file {self.file_path.name}: {str(e)}"
            )
        
        if df.empty:
            raise ValueError("Dataset kosong. Tidak ada baris data.")
        
        return df