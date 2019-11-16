from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    SHOPPING_CART = (By.ID, 'nav-cart-count')
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    SEARCH_DROPDOWN_SELECTION = (By.CSS_SELECTOR, 'select#searchDropdownBox')
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-search-dropdown-card span.nav-search-label')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def click_cart(self):
        self.click(*self.SHOPPING_CART)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def click_shopping_cart(self):
        self.click(*self.SHOPPING_CART)

    def select_department(self, department_name=''):
        select_department_element = self.find_element(*self.SEARCH_DROPDOWN_SELECTION)
        select = Select(select_department_element)
        select.select_by_value(department_name)

    def verify_selected_department(self, expected_department):
        self.verify_text(expected_department,  *self.SELECTED_DEPARTMENT )
