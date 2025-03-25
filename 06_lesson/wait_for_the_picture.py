from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

#Вход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#Ожидание загрузки всех картинок
element = WebDriverWait(driver, 40)
element.until(
    EC.text_to_be_present_in_element ((By.CSS_SELECTOR, "div:nth-child(4)"), "Done!")
    )

#Получение атрибута srs у 3 картинки
image = driver.find_element(By.CSS_SELECTOR, "#award")
atribute_src = image.get_property("src")

#Печать атрибута
print("Атрибут = ", atribute_src)

#Закрыть браузер
driver.quit()
