import re

#sync API - It is a blocking API that waits for the action to complete before moving on to the next action. It is easier to use and understand, but it can be slower because it waits for each action to complete before moving on to the next action.
#async API - It is a non-blocking API that does not wait for the action to complete before moving on to the next action. It is faster because it does not wait for each action to complete before moving on to the next action, but it can be more difficult to use and understand

from playwright.sync_api import Page, expect
from playwright.async_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


# -- browser
# Headless - It will  not Open the browser window. It is faster and used in CI/CD pipelines.
# -- headed - It will Open the browser window. It is slower and used in local development.
# pytest --browser webkit --browser firefox  --browser chromium  --headed   -> run the test in headed mode in multiple browsers.
# pytest -k test_has_title -> run this test cases method only.

# pip install pytest-xdist -> install dependency
# --numprocesses=4 -> run the test cases in parallel mode. It will run 4 test cases in parallel.
