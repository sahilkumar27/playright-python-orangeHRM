import logging

import pytest
from playwright.sync_api import Page, Playwright

from config.settings import Settings
from framework.driver_factory import DriverFactory
from pages.playwright_home_page import PlaywrightHomePage
from pages.login_page import LoginPage


logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


@pytest.fixture(scope="session")
def settings() -> Settings:
    return Settings.load()


@pytest.fixture
def page(playwright: Playwright, settings: Settings) -> Page:
    yield from DriverFactory.create_page(playwright, settings)


@pytest.fixture
def playwright_home_page(page: Page, settings: Settings) -> PlaywrightHomePage:
    return PlaywrightHomePage(page, settings)


@pytest.fixture
def login_page(page: Page, settings: Settings) -> LoginPage:
    return LoginPage(page, settings)
