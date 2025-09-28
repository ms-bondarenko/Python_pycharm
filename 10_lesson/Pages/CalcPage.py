import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalcPage:
    def __init__(self, browser):
        """Инициализация класса CalcPage.

        Args:
            browser: Экземпляр веб-драйвера для управления браузером.
        """
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()

    @allure.step("Ввод значения задержки и вычислений")
    def input_calc(self):
        """Метод для ввода значений в калькулятор."""
        delay_input = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        """Ввод значения задержки"""
        delay_input.send_keys("45")

        """Вводим значения в калькулятор"""
        for value in ['7', '+', '8', '=']:
            with allure.step(f"Клик по кнопке '{value}'"):
                """ищем кнопку равно по локатору текст и нажимаем на нее"""
                self._driver.find_element(By.XPATH, f"//*[contains(text(), '{value}')]").click()
