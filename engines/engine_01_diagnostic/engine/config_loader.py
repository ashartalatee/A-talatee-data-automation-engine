import yaml
from pathlib import Path

class ConfigLoader:
    """
    Membaca dan memvalidasi konfigurasi engine.
    """

    def __init__(self, config_path: str = "config/default.yaml"):
        self.config_path = Path(config_path)
        self.config = self._load()

    def _load(self) -> dict:
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config not found: {self.config_path}")

        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get(self, section: str, default=None):
        return self.config.get(section, default)
