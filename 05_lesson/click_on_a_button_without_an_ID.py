#Кликните на синюю кнопку
#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
#Имеется в виду ручной запуск скрипта, цикл в коде не нужен

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")

locator = ".btn.btn-primary"

button_without_id = driver.find_element(By.CSS_SELECTOR, locator)
button_without_id.click()