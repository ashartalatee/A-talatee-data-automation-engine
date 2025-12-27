import csv
from pathlib import Path
from datetime import datetime

class OutputWriter:
    """
    Menulis output engine ke format standar (CSV & Markdown).
    """

    def __init__(self, base_dir: str = "reports"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

    def write_dataset_score(self, dataset_name: str, score: int, risk_level: str, batch: bool = False):
        target_dir = self.base_dir / "csv" / ("batch" if batch else "")
        target_dir.mkdir(parents=True, exist_ok=True)

        file_path = target_dir / "dataset_scores.csv"
        is_new = not file_path.exists()

        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new:
                writer.writerow(["date", "dataset", "score", "risk_level"])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d"),
                dataset_name,
                score,
                risk_level
            ])

    def write_column_scores(self, dataset_name: str, column_scores: dict, batch: bool = False):
        target_dir = self.base_dir / "csv" / ("batch" if batch else "")
        target_dir.mkdir(parents=True, exist_ok=True)

        file_path = target_dir / "column_scores.csv"
        is_new = not file_path.exists()

        with open(file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if is_new:
                writer.writerow(["date", "dataset", "column", "score"])

            for col, score in column_scores.items():
                writer.writerow([
                    datetime.now().strftime("%Y-%m-%d"),
                    dataset_name,
                    col,
                    score
                ])
