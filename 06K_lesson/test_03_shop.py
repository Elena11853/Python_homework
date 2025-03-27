from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

#Вход на сайт
driver.get("https://www.saucedemo.com/")

# Авторизация
Username = driver.find_element(By.ID, 'user-name').send_keys('standard_user')
Password = driver.find_element(By.ID, 'password').send_keys('secret_sauce')
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()

 # Добавление товаров в корзину
backpack_add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
tshirt_add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
onesie_add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        
backpack_add_to_cart_button.click()
tshirt_add_to_cart_button.click()
onesie_add_to_cart_button.click()

# Переход в корзину
cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_link.click()
# Нажатие кнопки Checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
# Получение локаторов
first_name = driver.find_element(By.ID, "first-name")
last_name = driver.find_element(By.ID, "last-name")
postal_code = driver.find_element(By.ID, "postal-code")
continue_button = driver.find_element(By.ID, "continue")

# Заполнение формы
first_name.send_keys('Елена')
last_name.send_keys('Семенкова')
postal_code.send_keys('162250')

# Переход на итоговый экран
continue_button.click()

# получение текста с итоговой суммой
total_price_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text

# поиск итоговой суммы в тексте с итоговой суммой
assert '$58.29' in total_price_text, f"Полученный тотал: {total_price_text}, ожидаемая сумма: $58.29."

driver.quit()