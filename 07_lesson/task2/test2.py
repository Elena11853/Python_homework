from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login import Login
from main_page import Main_page
from cart_checkout import Cart_checkout
from total_cost import Total_cost


def test_total_score():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    login = Login(driver)
    login.login_page()
    main_page = Main_page(driver)
    main_page.Main_page()
    cart_chekcout = Cart_checkout(driver)
    cart_chekcout.Cart()
    cart_chekcout.Checkout_info()
    total_cost  = Total_cost(driver)
    total_cost.Total_cost()

    