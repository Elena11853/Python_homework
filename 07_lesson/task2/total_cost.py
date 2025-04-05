from selenium.webdriver.common.by import By

class Total_cost:
    
    def __init__(self, driver):
        self._driver = driver

    def Total_cost(self):
        total_cost_text = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        assert '$58.29' in total_cost_text, f"Полученный тотал: {total_cost_text}, ожидаемая сумма: $58.29."