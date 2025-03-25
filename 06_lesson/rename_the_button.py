from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

#Вход на сайт
driver.get("http://uitestingplayground.com/textinput")

#Ввести текст в поле ввода "SkyPro"
input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input.click()
input.send_keys('SkyPro')

#Кликнуть на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()

#Ожидание появления текста в синей кнопке
waiter = WebDriverWait(driver, 40)
waiter.until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#updatingButton"), "SkyPro")
)
#Вывод в консоль текста из кнопки
print(button.text)

#Закрыть браузер
driver.quit()