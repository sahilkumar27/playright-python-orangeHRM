from itertools import product

from playwright.sync_api import Page



# multiple buttons in same page with the help of filter method.
def test_has_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # #this is the filter method to filter the product from the list of products with the help of the text of the product.
    # product1 = page.locator('.inventory_item').filter(has_text="Sauce Labs Backpack")
    # product1.locator("button:has-text('Add to cart')").click()
    # page.wait_for_timeout(5000)

    #this is the filter method to filter the product from the list of products with the help of the button text (child of the inventory) of the product.
    product1 = page.locator('.inventory_item').filter(has=page.locator("button.btn_inventory"))
    product1.first.locator("button").click()
    page.wait_for_timeout(4000)