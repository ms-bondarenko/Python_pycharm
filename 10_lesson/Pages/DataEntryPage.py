from selenium.webdriver.common.by import By
import allure


@allure.feature("Страница ввода данных")
class DataEntryPage:
    def __init__(self, browser):
        """Инициализация класса DataEntryPage.

        Args:
            browser: Экземпляр веб-драйвера для управления браузером.
        """
        self._driver = browser

    @allure.step("Ввод данных пользователя")
    def data_entry(self):
        """Метод для ввода данных пользователя на странице ввода."""
        """Ввод имени"""
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Михаил")

        """Ввод фамилии"""
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Бондаренко")

        """Ввод почтового индекса"""
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("352900")

        """Клик по кнопке продолжения"""
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
