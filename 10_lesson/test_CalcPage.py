import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
from Pages.CalcPage import CalcPage


@allure.feature("Калькулятор")
@allure.story("Тестирование калькулятора на правильность вычислений")
def test_calc_page():
    """Тестирование калькулятора для проверки правильности результата."""
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        with allure.step("Открытие страницы калькулятора"):
            calc_page = CalcPage(browser)
            calc_page.input_calc()

        with allure.step("Ожидание результата"):
            result = WebDriverWait(browser, 50).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '15')]"))
            )
            print(result.text)
        """Ожидаемый результат из ТЗ"""
        expected_res = 15

        with allure.step("Проверка результата"):
            assert expected_res == int(result.text), f"Ожидалось {expected_res}, но получено {result.text}"

    finally:
        with allure.step("Закрытие браузера"):
            browser.quit()
