from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 30)

#Вход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Вводим задержку
delay = driver.find_element(By.ID, 'delay')
delay.clear()
delay.send_keys('45')


#
calculator = driver.find_element(By.ID, 'calculator')
keys = calculator.find_element(By.CLASS_NAME, 'keys')
btn_seven = keys.find_element(By.XPATH, "//*[text()='7']")
btn_eight = keys.find_element(By.XPATH, "//*[text()='8']")
btn_plus = keys.find_element(By.XPATH, "//*[text()='+']")
btn_equals = keys.find_element(By.XPATH, "//*[text()='=']")

#Нажатие на кнопки
btn_seven.click()
btn_plus.click()
btn_eight.click()
btn_equals.click()
# Ожидаем появления результата
WebDriverWait(driver, 50).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
# Проверяем результат
result = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert int(result) == 15, "Неверный результат"
print(result)
driver.quit()