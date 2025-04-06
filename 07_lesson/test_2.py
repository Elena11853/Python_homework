from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from login import Login
from main_page import Main_page
from cart_checkout import Cart_checkout
from total_label import Total_label


def test_2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login = Login(driver)
    login.login_page()
    main_page = Main_page(driver)
    main_page.Main_page()
    cart_chekcout = Cart_checkout(driver)
    cart_chekcout.Cart()
    cart_chekcout.Checkout_info()
    total_cost  = Total_label(driver)
    total_cost.Total_label()

    total_price_text = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    assert '$58.29' in total_price_text, f"Полученный тотал: {total_price_text}, ожидаемая сумма: $58.29."
