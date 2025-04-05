from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self._driver = driver

    def login_page(self):
        self._driver.get("https://www.saucedemo.com/")
        self._driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        self._driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self._driver.find_element(By.ID, 'login-button').click()