from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")

#Ввод текста "1000" 
input = driver.find_element(By.CSS_SELECTOR, "input[type = 'number']")
input.click
input.send_keys('1000')
sleep(3)

#Очистка поля ввода
input.clear()
sleep(3)

#Ввод текста "999" 
input.send_keys('999')
sleep(3)

#Закрыть браузер
driver.close()