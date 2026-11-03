import os
from pathlib import Path


class Settings:
    """Reads values from config.properties and stores them for the test run."""

    def __init__(self, path: Path | None = None) -> None:
        # config.properties is in the same folder as this Python file.
        path = path or Path(__file__).with_name("config.properties")
        values = self._read_properties(path)

        # Environment variables take priority over the properties file.
        self.base_url = os.getenv("BASE_URL", values.get("base_url", ""))
        self.username = os.getenv("ORANGEHRM_USERNAME", values.get("username", ""))
        self.password = os.getenv("ORANGEHRM_PASSWORD", values.get("password", ""))
        self.browser = os.getenv(
            "PLAYWRIGHT_BROWSER", values.get("browser", "chromium")
        )
        self.headless = os.getenv(
            "PLAYWRIGHT_HEADLESS", values.get("headless", "false")
        ).lower() == "true"

    @staticmethod
    def _read_properties(path: Path) -> dict[str, str]:
        values: dict[str, str] = {}

        if not path.exists():
            return values

        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip()

        return values

    @classmethod
    def load(cls, path: Path | None = None) -> "Settings":
        """Keeps the existing Settings.load() usage beginner-friendly."""
        return cls(path)
