import pytest
from playwright.sync_api import Page

from config.settings import Settings


class BaseTest:
    """Common setup for class-based tests."""

    page: Page
    settings: Settings

    @pytest.fixture(autouse=True)
    def setup(self, page: Page, settings: Settings) -> None:
        self.page = page
        self.settings = settings
