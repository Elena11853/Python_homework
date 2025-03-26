
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

# Вводим задержку
Username = driver.find_element(By.ID, '#user-name').send_keys('standard_user')
Password = driver.find_element(By.ID, '#password').send_keys('secret_sauce')
login_button = driver.find_element(By.ID, '#login-button')
login_button.click()

 # Добавление товаров в корзину
backpack_add_to_cart_button = driver.find_element(By.ID, "#add-to-cart-sauce-labs-backpack")
tshirt_add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
onesie_add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        
backpack_add_to_cart_button.click()
tshirt_add_to_cart_button.click()
onesie_add_to_cart_button.click()
