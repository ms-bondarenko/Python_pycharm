import pytest
from selenium.webdriver.common.by import By

class AddedItems():

    def __init__(self, browser):
        self._driver = browser

    def added_items(self):
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()