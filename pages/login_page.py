import logging

from playwright.sync_api import Page, expect

from config.settings import Settings
from pages.base_page import BasePage


logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page, settings: Settings | None = None) -> None:
        super().__init__(page, settings)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.dashboard_heading = page.get_by_role("heading", name="Dashboard")

    def open_login_page(self) -> "LoginPage":
        logger.info("Opening OrangeHRM login page")
        self.open()
        return self

    def login(self, username: str | None = None, password: str | None = None) -> None:
        username = username or self.settings.username
        password = password or self.settings.password

        logger.info("Entering username")
        self.username_input.fill(username)
        logger.info("Entering password")
        self.password_input.fill(password)
        logger.info("Clicking Login")
        self.login_button.click()

    def assert_logged_in(self) -> None:
        logger.info("Verifying Dashboard is visible")
        expect(self.dashboard_heading).to_be_visible()
        logger.info("Login completed successfully")
