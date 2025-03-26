from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
#Настройка ожидания
wait = WebDriverWait(driver, 10)
#Вход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


#Заполнение формы
driver.find_element(By.NAME, "first-name").send_keys('Иван')
driver.find_element(By.NAME, "last-name").send_keys('Петров')
driver.find_element(By.NAME, "address").send_keys('Ленина, 55-3')
driver.find_element(By.NAME, "e-mail").send_keys('test@skypro.com')
driver.find_element(By.NAME, "phone").send_keys('+7985899998787')
driver.find_element(By.NAME, "zip-code").send_keys('') #Оставить пустым
driver.find_element(By.NAME, "city").send_keys('Москва')
driver.find_element(By.NAME, "country").send_keys('Россия')
driver.find_element(By.NAME, "job-position").send_keys('QA')
driver.find_element(By.NAME, "company").send_keys('SkyPro')

#Нажатие кнопки Submit
Submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#Проверка полей
zip_code_input = driver.find_element(By.ID, 'zip-code')
fname_input = driver.find_element(By.ID, 'first-name')
lname_input = driver.find_element(By.ID, 'last-name')
address_input = driver.find_element(By.ID, 'address')
email_input = driver.find_element(By.ID, 'e-mail')
phone_input = driver.find_element(By.ID, 'phone')
city_input = driver.find_element(By.ID, 'city')
jobpos_input = driver.find_element(By.ID, 'job-position')
company_input = driver.find_element(By.ID, 'company')

# Проверка сообщения об успешной отправке
# Проверки, что Zip Code подсвечен красным
assert 'alert-danger' in zip_code_input.get_attribute('class'), 'Поле Zip Code не подсвечено красным'

# Проверки, что остальные поля подсвечены зеленым
fields_to_check = [
    fname_input, lname_input, address_input, email_input, phone_input, city_input, jobpos_input, company_input
]
for field in fields_to_check:
    assert 'alert-success' in field.get_attribute('class'), f'Поле {field.get_attribute("id")} не подсвечено зеленым'

#Закрыть браузер
driver.quit()