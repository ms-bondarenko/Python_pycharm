import pytest
from selenium.webdriver.common.by import By
import allure

@allure.severity("blocker")
@allure.feature("Страница логина")
class LoginPage:
    def __init__(self, browser):
        """Инициализация класса LoginPage.

        Args:
            browser: Экземпляр веб-драйвера для управления браузером.
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    @allure.step("Ввод логина и пароля")
    def login_input(self):
        """Метод для ввода логина и пароля на странице логина."""
        """Ввод имени пользователя"""
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")

        """Ввод пароля"""
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")

        """Клик по кнопке логина"""
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
