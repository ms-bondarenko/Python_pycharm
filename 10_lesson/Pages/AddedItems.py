import pytest
from selenium.webdriver.common.by import By
import allure

@allure.feature("Страница добавления товаров")
class AddedItems:
    def __init__(self, browser):
        """Инициализация класса AddedItems.

        Args:
            browser: Экземпляр веб-драйвера для управления браузером.
        """
        self._driver = browser

    @allure.step("Добавление товаров в корзину")
    def added_items(self):
        """Метод для добавления товаров в корзину."""
        """Добавление рюкзака"""
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

        """Добавление футболки"""
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        """Добавление комбинезона"""
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

        """Переход в корзину"""
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()

        """Клик по кнопке 'Checkout'"""
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
