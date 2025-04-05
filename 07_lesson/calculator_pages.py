from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Calculator_pages:

    def __init__(self, driver):
        self._driver = driver
   
    def start_testing(self,  driver):
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
           
    def set_time(self, time):
            self._driver.find_element(By.CSS_SELECTOR, 'input#delay').clear()
            self._driver.find_element(By.CSS_SELECTOR, 'input#delay').send_keys(time)

    def clicking(self):
        self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-primary' ).click()
        self._driver.find_element(By.CSS_SELECTOR, '.operator.btn.btn-outline-success' ).click()
        num = self._driver.find_elements(By.CSS_SELECTOR, '.btn.btn-outline-primary') 
        for i in num:
            if i.text =='8':
             i.click()     
        self._driver.find_element(By.CSS_SELECTOR, '.btn.btn-outline-warning' ).click()

    def waiting_result(self):
        WebDriverWait(self._driver, 55).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[style='display: none;']" )))