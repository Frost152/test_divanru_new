from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base
# from utilities.logger import Logger


class MainPage(Base):
    url = "https://www.divan.ru/"

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    locator_main_catalog_css = "button.I0naS.EnFvW"
    locator_check_xpath = "//a[@aria-label='Корзина']"

    # Getters
    def get_url(self):
        return self.url

    def get_wait_main_catalog(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_main_catalog_css)))

    def get_check(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_check_xpath)))

    # Actions
    def click_main_catalog(self):
        self.get_wait_main_catalog().click()

    def click_check(self):
        self.get_check().click()

    # Methods
    def open(self):
        # Logger.add_start_step("open")
        self.driver.get(self.url)
        self.driver.maximize_window()
        # Logger.add_end_step(self.driver.current_url, "open")

    def transfer_to_cart(self):
        self.click_check()
        assert "Корзина" in WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".CJo1Y"))).text
        print('Осуществлен переход в корзину')


class Catalog(MainPage):
    # Locators
    locator_sofa_menu_item_css = ".sOgI6"
    locator_products_xpath = "//div[@data-testid='product-card' and contains(@class, '_Ud0k U4KZV')]"
    locator_buy_button_xpath = ".//div[@data-testid='buy-button']"
    locator_cart_modal_close_xpath = "//div[@data-testid='cart-modal-close']"

    # Getters
    def get_wait_sofa_menu_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_sofa_menu_item_css)))

    def get_products(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locator_products_xpath)))

    def get_buy_button(self):
        action = ActionChains(self.driver)
        products = self.get_products()
        for i in products:
            action.move_to_element(i).perform()
            yield WebDriverWait(i, 10).until(EC.element_to_be_clickable((By.XPATH, self.locator_buy_button_xpath)))

    def get_cart_modal_close(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_cart_modal_close_xpath)))

    # Actions
    def click_sofa_menu_item(self):
        self.get_wait_sofa_menu_item().click()

    def move_and_buy_product(self):
        for i in self.get_buy_button():
            i.click()
            self.get_cart_modal_close().click()
        print('Выбраны необходимые товары')

    # Methods
    def go_to_sofas(self):
        self.click_sofa_menu_item()
        self.assert_compare_text(self.get_head_page().text, "Диваны и кресла")
        print('Осуществлен переход в раздел Диваны и кресла')

    def buying_product_cart(self):
        self.move_and_buy_product()
        self.transfer_to_cart()
