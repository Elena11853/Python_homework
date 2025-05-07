from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure


class Calculator_pages():
    @allure.step(
        'Открытие страницы: "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"'
    )
    def __init__(self, driver: str):
        """
        Конструктор класса Calculator_pages
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        """
        Открывает страницу калькулятора.
        """
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(50)

    @allure.step("Ввод в поле по локатору #delay")
      
    def delay(self, term: str):
        """ Устанавливает задержку отображения результатов вычислений. 
        :param term: Значение задержки (число в секундах), которое вводится в поле "#delay". 
        :type term: str """
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    @allure.step("Нажатие на кнопки калькулятора")
    def click(self, text):
        """ Нажимает указанную кнопку на калькуляторе. :param button_text
        : Текстовая метка искомой кнопки калькулятора. :type button_text: str """
        self._driver.find_element(By.XPATH, f"//*[contains(text(),'{text}')]").click()

    @allure.step("Проверка результата через 50 секунд")
    def screen(self, answer) -> str:
        """ Проверяет результат вычисления путем ожидания появления 
        ожидаемого текста на экране калькулятора. 
        :param expected_answer: Ожидаемый результат вычисления, который 
        должен появиться на дисплее. 
        :type expected_answer: str :return
        : Текстовое значение экрана калькулятора после завершения ожидания. 
        :rtype: str """
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), answer)
        )
        return screen.text