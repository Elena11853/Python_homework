#В модальном окне нажмите на кнопку Сlose

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)
close_button = driver.find_element(By.CSS_SELECTOR, ".modal .modal-footer p")
close_button.click()
sleep(3)

#Закрыть браузер
driver.close()