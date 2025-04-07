from selenium.webdriver.common.by import By

class Total_label:
    def __init__(self, driver):
        self._driver = driver

    def Total_label(self):
        total_label = self._driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
        print (total_label)