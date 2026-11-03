from collections.abc import Iterator

from playwright.sync_api import Browser, Page, Playwright

from config.settings import Settings


class DriverFactory:
    """Creates a browser and page, then closes both after the test."""

    @staticmethod
    def create_browser(playwright: Playwright, settings: Settings) -> Browser:
        # Playwright exposes these three browser objects.
        if settings.browser == "chromium":
            return playwright.chromium.launch(headless=settings.headless)
        if settings.browser == "firefox":
            return playwright.firefox.launch(headless=settings.headless)
        if settings.browser == "webkit":
            return playwright.webkit.launch(headless=settings.headless)

        raise ValueError("browser must be chromium, firefox, or webkit")

    @classmethod
    def create_page(
        cls, playwright: Playwright, settings: Settings
    ) -> Iterator[Page]:
        browser = cls.create_browser(playwright, settings)
        page = browser.new_page()
        try:
            yield page
        finally:
            # Always close the browser, even when a test fails.
            browser.close()
