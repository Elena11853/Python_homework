from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

#Вход на сайт
driver.get("http://uitestingplayground.com/ajax")

#Нажать на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, '#ajaxButton')
button.click()
#Ожидание появления текста в зелёной плашке
waiter = WebDriverWait(driver, 40)
waiter.until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".bg-success"), "Data loaded with AJAX get request.")
)
#Получение текста из зелёной плашки
green_text = driver.find_element(By.CSS_SELECTOR, (".bg-success"))
print(green_text.text)
#Закрыть браузер
driver.quit()

