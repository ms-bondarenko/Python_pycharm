from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage():

    def __init__(self, browser):
        self._driver = browser

    def go_to_cart(self):
        self._driver.get("https://www.labirint.ru/cart/")

    def get_cart_counter(self):
        try:
            full_text = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#basket-default-prod-count2"))
            ).text
            count_text = full_text.split()[0]
            return count_text
        except Exception as e:
            print("Ошибка при получении счетчика корзины:", e)
            return None  # Возвращаем None в случае ошибки