from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Product(Page):
    ATC_BUTTON = (By.ID, 'add-to-cart-button')
    POPOVER_SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    SALES_DEALS_LINK = (By.XPATH, "//span[contains(text(), 'SALES & DEALS')]")
    MEGA_MENU = (By.CSS_SELECTOR, "div.nav-fullWidthSubnavFlyout")

    def open_product_page(self, product_id):
        # https://www.amazon.com/gp/product/B074TBCSC8
        self.open_page(f'gp/product/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ATC_BUTTON)
        self.actions.move_to_element(cart_button).perform()

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.POPOVER_SIZE_TOOLTIP)

    def hover_sub_nav_category_link(self, *locator):
        category_link = self.find_element(*locator)
        self.actions.move_to_element(category_link).perform()

    def mega_menu_shown(self):
        self.wait_for_element_appear(*self.MEGA_MENU)
