from asyncio import wait_for

from playwright.sync_api import Page, expect

def test_js_alert_handling(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(5000);
    page.once("dialog", lambda dialog:dialog.accept())
    page.wait_for_timeout(5000);
    page.get_by_text("Click for JS Alert").click()
    page.wait_for_timeout(5000);
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")



def test_js_confirm_cancel(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(5000);
    page.once("dialog", lambda dialog:dialog.dismiss())
    page.wait_for_timeout(5000);
    page.get_by_text("Click for JS Confirm").click()
    page.wait_for_timeout(5000);
    expect(page.locator("#result")).to_have_text("You clicked: Cancel")


def test_js_prompt_text(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_timeout(5000);
    page.once("dialog", lambda dialog:dialog.accept("Hello World"))
    page.wait_for_timeout(5000);
    page.get_by_text("Click for JS Prompt").click()
    page.wait_for_timeout(5000);
    expect(page.locator("#result")).to_have_text("You entered: Hello World")
