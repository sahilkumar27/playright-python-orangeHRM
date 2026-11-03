import pytest
from playwright.sync_api import expect

from pages.playwright_home_page import PlaywrightHomePage


@pytest.mark.smoke
def test_playwright_home_page_loads(playwright_home_page: PlaywrightHomePage) -> None:
    playwright_home_page.open_home_page()
    playwright_home_page.assert_page_loaded()
    assert "Playwright" in playwright_home_page.get_title()


def test_get_started_navigation(playwright_home_page: PlaywrightHomePage) -> None:
    playwright_home_page.open_home_page()
    playwright_home_page.click_get_started()

    expect(playwright_home_page.page).to_have_url("https://playwright.dev/docs/intro")