import pandas as pd
from pathlib import Path


class DataLoader:
    """
    DataLoader bertugas membaca data mentah tanpa mengubah isi.
    Jika data tidak bisa dibaca dengan aman, loader harus gagal dengan jelas.
    """

    SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".xls"]
    COMMON_ENCODINGS = ["utf-8", "latin-1", "cp1252"]

    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

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

        last_error = None

        if self.file_path.suffix.lower() == ".csv":
            for encoding in self.COMMON_ENCODINGS:
                try:
                    df = pd.read_csv(self.file_path, encoding=encoding)

                    if df.empty:
                        raise ValueError("Dataset kosong.")

                    # simpan metadata penting
                    df.attrs["detected_encoding"] = encoding
                    return df

                except Exception as e:
                    last_error = e
                    continue
        else:
            try:
                df = pd.read_excel(self.file_path)

                if df.empty:
                    raise ValueError("Dataset kosong.")

                df.attrs["detected_encoding"] = "excel-native"
                return df

            except Exception as e:
                last_error = e

        raise RuntimeError(
            f"Gagal membaca file {self.file_path.name}. "
            f"Encoding tidak aman atau file rusak. "
            f"Error terakhir: {last_error}"
        )


# PUBLIC ENGINE API (INI PENTING)
def load_dataset(file_path: str | Path) -> pd.DataFrame:
    """
    Facade function untuk CLI dan engine lain.
    """
    loader = DataLoader(file_path)
    return loader.load()
