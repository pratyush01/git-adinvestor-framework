import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(autouse=True)
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://prod.adinvestor.com/signin")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

# def setup(request, browser):
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         print("Please provide valid browser")
#     driver.get("https://prod.adinvestor.com/signin")
#     driver.maximize_window()
#     request.cls.driver = driver
#     yield
#     driver.close()
#
# def pytest_adoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")











