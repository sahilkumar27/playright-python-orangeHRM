from playwright.sync_api import Page, expect

from config.settings import Settings
from pages.base_page import BasePage


class PlaywrightHomePage(BasePage):
    URL = "https://playwright.dev/"

    def __init__(self, page: Page, settings: Settings | None = None) -> None:
        super().__init__(page, settings)
        self.get_started_link = page.get_by_role("link", name="Get started")

    def open_home_page(self) -> "PlaywrightHomePage":
        self.open(self.URL)
        return self

    def assert_page_loaded(self) -> None:
        expect(
            self.page.get_by_role(
                "heading",
                name="Playwright enables reliable web automation for testing, scripting, and AI agents.",
            )
        ).to_be_visible()

    def click_get_started(self) -> None:
        self.get_started_link.click()
