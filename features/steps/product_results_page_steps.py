from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULT = (By.XPATH,
                  "//span[@class='celwidget slot=SEARCH_RESULTS template=SEARCH_RESULTS widgetId=search-results "
                  "index=0']//img[@class='s-image']")
SALES_DEALS_LINK = (By.XPATH, "//span[contains(text(), 'SALES & DEALS')]")


@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULT).click()
    sleep(1.5)


@then('Search result for <expected_result> is shown')
def verify_result(context, product):
    # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    # # assert result_text == '"dress"', f"Expected text is dress but got {result_text}"
    # assert product in result_text, f"Expected text is dress but got {result_text}"
    context.app.search_results.verify_result_shown(product)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@when('Hover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()


@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()


# ~~~~~~~~~~~~~~~~~~~~~~~Sales & Deals~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@when('Hovering over {department} link')
def hover_sales_and_deals(context, department):
    context.app.product_page.hover_sub_nav_category_link(*SALES_DEALS_LINK)


@then('Verifies user sees the mega menu deals')
def mega_menu_shown(context):
    context.app.product_page.mega_menu_shown()
