from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Метод получения url страницы"""

    def get_current_url(self) -> str:
        return str(self.driver.current_url)

    """Метод получения лого"""

    def get_logo_link(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='logo-link']")))

    """Метод получения заголовка"""

    def get_head_page(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wcwtp")))

    """Метод сравненния текста"""

    @staticmethod
    def assert_compare_text(word_one, word_two):
        assert word_one == word_two
