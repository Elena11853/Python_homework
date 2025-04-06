from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from calculator_pages import Calculator_pages
def test_1():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calculator_pages = Calculator_pages(driver)
    calculator_pages.start_testing(driver)
    calculator_pages.set_time(45)
    calculator_pages.clicking()
    calculator_pages.waiting_result()

    result= driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert int(result) == 15, "Неверный результат"
    print(result)