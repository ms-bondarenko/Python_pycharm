from time import sleep

import selenium
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CartPage import CartPage
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage

def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.set_cookie_poicy()
    main_page.search('python')

    result_page = ResultPage(browser)
    to_be =result_page.add_books()

    cart_page = CartPage(browser)
    cart_page.go_to_cart()
    as_is = cart_page.get_cart_counter()

    assert to_be == int(as_is)

    sleep(5)