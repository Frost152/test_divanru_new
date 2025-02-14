import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.add_argument("--headless")
    options.page_load_strategy = "eager"
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    # driver = webdriver.Chrome(options=options, service=ChromeService(executable_path=r"C:\Users\Кукло Кирилл\.wdm\drivers\chromedriver\win64\132.0.6834.159\chromedriver.exe"))
    yield driver
    # При необходимости закрывать браузер, раскомментировать строку 15
    # driver.quit()
