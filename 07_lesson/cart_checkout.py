from selenium.webdriver.common.by import By

class Cart_checkout:
    def __init__(self, driver):
        self._driver = driver

    def Cart(self):
        self._driver.find_element(By.ID, 'checkout').click() 

    def Checkout_info(self):
         self._driver.find_element(By.ID, "first-name").send_keys("Елена")
         self._driver.find_element(By.ID, "last-name").send_keys("Семенкова")
         self._driver.find_element(By.ID, "postal-code").send_keys('162250')
         self._driver.find_element(By.ID, "continue").click()