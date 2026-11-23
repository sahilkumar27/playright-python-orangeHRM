from playwright.sync_api import Page


def test_has_title(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
    page.wait_for_timeout(5000)
    page.go_back()

    page.wait_for_timeout(5000)
    page.go_forward()

    page.wait_for_timeout(5000)
    page.reload()

    page.wait_for_timeout(5000)  # Wait for 5 seconds to allow the page to load


#fixture - A fixture is a function that runs before each test case method. It is used to set up the test environment and provide the necessary resources for the test case method to run. In this case, the fixture is used to create a new page object for each test case method. The page object is used to interact with the web page and perform actions such as clicking buttons, filling out forms, and navigating to different pages.
# and in easy way to understand - it is an object basically representing a real browser tab or window. It allows you to interact with the web page, perform actions, and retrieve information from the page. The Page object is created by the Playwright framework when you launch a browser instance and open a new tab or window. It provides methods and properties to interact with the web page, such as clicking buttons, filling out forms, navigating to different pages, and retrieving information from the page.
# codegen - `playwright codegen {url}` -> whatever the event you perform in the application, it will provide the script
# playright trace viewer {`pytest --tracing=on`} -> let you visually debug tests by replaying each step with DOM snapshots, network requests, and console logs. It helps identify issues and understand test failures.
# `playwright show-trace test-results/test-browser-navigation-py-test-has-title-chromium/trace.zip` -> to open the test results you can use this command.
# `https://trace.playwright.dev/` -> you can also upload the trace.zip file to this website to view the test results.