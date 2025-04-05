from selenium.webdriver.common.by import By

class Main_page:
    def __init__(self, driver):
        self._driver = driver

    def Main_page(self):
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

      