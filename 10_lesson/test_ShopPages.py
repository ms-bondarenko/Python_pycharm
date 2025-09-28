from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import allure

from Pages.LoginPage import LoginPage
from Pages.AddedItems import AddedItems
from Pages.DataEntryPage import DataEntryPage


@allure.feature("Тестирование магазина")
@allure.story("Проверка сумм на страницах магазина")
def test_shop_pages():
    """Тестирование страниц магазина для проверки правильности итоговой суммы."""
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    try:
        with allure.step("Вход на страницу логина"):
            login_page = LoginPage(browser)
            login_page.login_input()

        with allure.step("Добавление товаров в корзину"):
            added_page = AddedItems(browser)
            added_page.added_items()

        with allure.step("Ввод данных на странице ввода"):
            data_page = DataEntryPage(browser)
            data_page.data_entry()

        with allure.step("Получение итоговой суммы"):
            summary_element = browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
            summary_text = summary_element.text.strip()
            summary_value = float(summary_text.replace('Total: ', '').replace('$', '').replace(',', ''))

        expected_sum = 58.29

        with allure.step("Проверка итоговой суммы"):
            assert summary_value == expected_sum, (f"Сумма не совпадает. Извлечённая сумма:"
                                                   f" ${summary_value:.2f}, Ожидаемая сумма: ${expected_sum:.2f}")
            print("Суммы совпадают", summary_value)

    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
