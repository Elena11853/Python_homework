#Кликнуть насинюю кнопку
#Запустить скрипт 3 раза вручную, убедиться, что он работает одинаково.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

button_class  = ".btn-primary"

button = driver.find_element(By.CSS_SELECTOR, button_class)


button.click()