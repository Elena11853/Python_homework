from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_pages import Calculator_pages


def test_HW2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_pages = Calculator_pages(driver)
    calculator_pages.start_testing(driver)
    calculator_pages.set_time(45)
    calculator_pages.clicking()
    calculator_pages.waiting_result()
    