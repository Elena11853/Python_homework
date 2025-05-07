from selenium.webdriver.common.by import By
import allure


class Store():
    @allure.step("Открытие сайта магазина: " \
    "https://www.saucedemo.com/")

    def __init__(self, driver: str):
        """
        Конструктор класса Store
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)

    @allure.step("Ввод в поле Username")
    def authorization_username(self, term: str):
        """ Заполняет поле ввода имени пользователя на странице авторизации. 
        :param username: Имя пользователя для входа. :type username: str """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)

    @allure.step("Ввод в поле Password и клик по кнопке Login")
    def authorization_password(self, term: str): 
        """ Заполняет поле пароля и нажимает кнопку "Login". 
        :param password: Пароль для входа. :type password: str """ 
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    @allure.step("Добавление в корзину товаров")
    def add_to_cart(self):
        """ Добавляет выбранные товары в корзину. """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    allure.step("Переход в корзину")
    def shopping_cart(self):
        """ Переходит в раздел корзины покупок. """
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    @allure.step("Нажатие Checkout")
    def checkout(self):
        """ Нажимает кнопку перехода к оформлению заказа. """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    @allure.step("Ввод в поле First Name")
    def input_first_name(self, term: str):
        """ Заполняет поле первого имени покупателя. 
        :param first_name: Первое имя клиента. :type first_name: str """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(term)

    @allure.step("Ввод в поле Last Name")
    def input_last_name(self, term: str):
        """ Заполняет поле фамилии покупателя. 
        :param last_name: Фамилия клиента. :type last_name: str """
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(term)

    @allure.step("Ввод в поле Zip/Postal Code")
    def input_postal_code(self, term: str):
        """ Заполняет поле почтового индекса. :param postal_code: Почтовый индекс. 
        :type postal_code: str """
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(term)

    @allure.step("Нажатие Continue")
    def button_continue(self):
        """ Продолжает оформление заказа, нажимая кнопку "Continue". """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    @allure.step("Отображение со страницы Итоговой стоимости (Total)")
    def summary_total(self) -> str:
        """ Возвращает строку с общей суммой заказа. :return: Общая сумма заказа. :rtype: str """
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total