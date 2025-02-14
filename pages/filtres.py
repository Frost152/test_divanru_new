import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class BaseFilters(Base):
    # Locators
    locator_all_filters_button_CSS = ".S5eSU"
    locator_select_filter_xpath = "//span[text()='{}']"
    locator_apply_button_css = ".rt4b5 button"
    locator_apply_text_button_css = ".cu9ho"
    locator_apply_button_wait_text_xpath = "//span[text()='Секунду...']"
    locator_apply_button_num_text_css = ".pWRim"
    locator_filter_disclosure_button_css = ".ho0uq .VCJHC"
    locator_show_all_button_xpath = "//span[text()='Показать все']"
    locator_selected_filters_css = ".xuao5"

    locator_filter_set_css = "#{}"
    locator_range_block_xpath = ".//div[@class='gn9QX'][.//div[@class='uQG07' and text()='{}']]"
    locator_range_min_xpath = ".//input[@data-testid='rangeMin']"
    locator_range_max_xpath = ".//input[@data-testid='rangeMax']"

    # locator_range_min_xpath = ".//input[@class='ui-Rfz9j'][1]"
    # locator_range_max_xpath = ".//input[@class='ui-Rfz9j'][2]"

    # Getters
    def get_all_filters_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_all_filters_button_CSS)))

    def get_select_filter(self, filter_name):
        return WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_select_filter_xpath.format(filter_name))))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_button_css)))

    def get_apply_text_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_text_button_css))).text

    def get_apply_button_wait_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_apply_button_wait_text_xpath)))

    def get_apply_button_num_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_button_num_text_css))).text

    def get_filter_disclosure_button(self):
        return WebDriverWait(self.driver, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.locator_filter_disclosure_button_css)))

    def get_show_all_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator_show_all_button_xpath)))

    def get_selected_filters_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.locator_selected_filters_css)))

    def get_filter_set(self, name_filter_set):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_filter_set_css.format(name_filter_set))))

    def get_range_block(self, name_filter_set, range_block_name):
        return self.get_filter_set(name_filter_set).find_element(By.XPATH, self.locator_range_block_xpath.format(
            range_block_name))

    def get_range_min(self, name_filter_set, range_block_name):
        return self.get_range_block(name_filter_set, range_block_name).find_element(By.XPATH,
                                                                                    self.locator_range_min_xpath)

    def get_range_max(self, name_filter_set, range_block_name):
        return self.get_range_block(name_filter_set, range_block_name).find_element(By.XPATH,
                                                                                    self.locator_range_max_xpath)

    # Actions

    def click_apply_button(self):
        self.get_apply_button().click()

    def click_all_filters_button(self):
        self.get_all_filters_button().click()

    def click_select_filter(self, filter_name):
        action = ActionChains(self.driver)
        try:
            action.move_to_element(self.get_select_filter(filter_name)).perform()
            self.get_select_filter(filter_name).click()
        except ElementClickInterceptedException:
            time.sleep(1)
            action.move_to_element(self.get_select_filter(filter_name)).perform()
            self.get_apply_text_button()
            self.get_select_filter(filter_name).click()

    def click_filter_disclosure_button(self):
        action = ActionChains(self.driver)
        try:
            elements = self.get_filter_disclosure_button()
            for i in elements:
                try:
                    action.move_to_element(i).perform()
                    i.click()
                except ElementClickInterceptedException:
                    time.sleep(1)
                    action.move_to_element(i).perform()
                    i.click()
        except TimeoutException:
            pass

    def click_show_all_button(self):
        action = ActionChains(self.driver)
        try:
            elements = self.get_show_all_button()
            for i in elements:
                try:
                    action.move_to_element(i).perform()
                    i.click()
                except ElementClickInterceptedException:
                    time.sleep(1)
                    action.move_to_element(i).perform()
                    i.click()
        except TimeoutException:
            pass

    def move_range_min(self, name_filter_set, range_block_name, x_min_param):
        action = ActionChains(self.driver)
        elem = self.get_range_min(name_filter_set, range_block_name)
        try:
            action.move_to_element(elem).click_and_hold(elem).move_by_offset(x_min_param, 0).release().perform()
        except ElementClickInterceptedException:
            time.sleep(1)
            action.move_to_element(elem).click_and_hold(elem).move_by_offset(x_min_param, 0).release().perform()

    def move_range_max(self, name_filter_set, range_block_name, x_max_param):
        action = ActionChains(self.driver)
        elem = self.get_range_max(name_filter_set, range_block_name)
        try:
            action.move_to_element(elem).click_and_hold(elem)
            time.sleep(1)
            action.move_by_offset(x_max_param, 0).release().perform()
        except ElementClickInterceptedException:
            time.sleep(1)
            action.move_to_element(elem).click_and_hold(elem)
            time.sleep(1)
            action.move_by_offset(x_max_param, 0).release().perform()

    # Methods

    def open_all_filters(self):
        self.click_filter_disclosure_button()
        self.click_show_all_button()
        print('Открыт блок фильтров')

    def selecting_multiple_filters(self, *args):
        for i in args:
            self.click_select_filter(i)
            self.get_apply_text_button()
        num = self.get_apply_button_num_text()
        print(f"Выбрано {num}")

    def selecting_range_filter(self, name_filter_set, range_block_name, min_param, max_param):
        min_param = int(min_param)
        max_param = int(max_param)
        self.move_range_min(name_filter_set, range_block_name, min_param)
        self.move_range_max(name_filter_set, range_block_name, max_param)


    def enter_filters(self, *args):
        self.click_apply_button()
        # tp = tuple([i.text for i in self.get_selected_filters_button()])
        # assert args in tp or args == tp
        print('Выбраны необходимые фильтры')
