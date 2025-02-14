from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegionPopup(Base):
    # Locators
    locator_region_popup_close_xpath = "//div[@data-testid='region-popup-close']"

    # Getters
    def get_close_region_popup(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_region_popup_close_xpath)))

    # Actions
    def close_region_popup(self):
        self.get_close_region_popup().click()

    # Methods
    def find_close_region_popup(self):
        try:
            self.close_region_popup()
            print("Popup выбора региона закрыт")
        except TimeoutException:
            pass


class ModalWrapper(Base):
    # Locators
    locator_modal_wrapper_close_css = "div[data-testid='modal-wrapper'] .ui-9F9ST"
    locator_modal_wrapper_close_xpath = "//div[@data-testid='modal-wrapper']//div[contains(@class, 'ui-2E5Bz')]"
    locator_modal_wrapper_css = "div[data-testid='modal-wrapper']"

    # Getters
    def get_modal_wrapper_close(self):
        return WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_modal_wrapper_close_css)))

    # Actions
    def close_modal_wrapper(self):
        self.get_modal_wrapper_close().click()

    # Methods
    def find_and_close_modal_wrapper(self):
        try:
            self.close_modal_wrapper()
            print('Модальное окно ОС закрыто')
        except TimeoutException:
            pass
