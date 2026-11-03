from playwright.sync_api import Page

from config.settings import Settings


class BasePage:
    def __init__(self, page: Page, settings: Settings | None = None) -> None:
        self.page = page
        self.settings = settings or Settings.load()

    def open(self, url: str | None = None) -> None:
        self.page.goto(url or self.settings.base_url, wait_until="domcontentloaded")

    def get_title(self) -> str:
        return self.page.title()
