from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class CartPage(Base):
    # Locators
    locator_select_all_css = ".imlid"
    locator_without_authorization_css = ".hFIoz"
    locator_phone_css = "[name='OrderForm[mobile]']"
    locator_address_css = "[name='OrderForm[address]']"
    locator_check_out_button_css = "[data-testid='checkout-button']"
    locator_final_label_css = ".CRIlJ"

    # Getters
    def get_select_all(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_select_all_css)))

    def get_without_authorization(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_without_authorization_css)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_phone_css)))

    def get_address(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_address_css)))

    def get_check_out_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_check_out_button_css)))

    def get_final_label(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_final_label_css)))

    # Actions
    def click_select_all(self):
        self.get_select_all().click()

    def click_without_authorization(self):
        self.get_without_authorization().click()

    def send_phone(self, phone):
        self.get_phone().send_keys(phone)

    def send_address(self, address):
        self.get_address().send_keys(address)
        self.get_address().send_keys(Keys.DOWN)
        self.get_address().send_keys(Keys.ENTER)

    def click_check_out_button(self):
        self.get_check_out_button().click()

    # Methods

    def order_confirmation(self, phone, address):
        self.click_select_all()
        self.click_without_authorization()
        self.send_phone(phone)
        self.send_address(address)
        print('Данные успешно заполнены')

    def order_finally(self):
        self.click_check_out_button()
        assert self.get_final_label().text == "Спасибо за заказ!"
        print("Заказ успешно оформлен")
