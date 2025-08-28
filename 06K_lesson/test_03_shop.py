import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_shop(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    search_input = driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    search_input = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

    button = driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    button_Labs_Backpack = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    button_Shirt = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    button_onecie = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    trash = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
    sleep(5)


