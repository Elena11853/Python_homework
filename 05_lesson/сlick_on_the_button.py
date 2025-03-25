#Пять раз клиунуть на кнопку Add Element
#Собрать список кнопок Delete ивывести размер списка.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

button_add_element = driver.find_element(By.CSS_SELECTOR, "button")

for i in range(5):
    button_add_element.click()

button_delete = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")

print("Размер списка равен: ", len(button_delete))

