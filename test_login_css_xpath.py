from playwright.sync_api import Page


def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # CSS Selector
    page.locator("input[placeholder='Username']").fill("Admin")
    page.locator("input[placeholder='Password']").fill("admin123")
    page.locator("button[type='submit']").click()

    ## xpath
    # page.locator("//input[@placeholder='Username']").fill("Admin")
    # page.locator("//input[@placeholder='Password']").fill("admin123")
    # page.locator("//button[@type='submit']").click()



