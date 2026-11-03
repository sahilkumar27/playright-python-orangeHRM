from pages.login_page import LoginPage


def test_orangehrm_user_can_login(login_page: LoginPage) -> None:
    login_page.open_login_page()
    login_page.login()
    login_page.assert_logged_in()
