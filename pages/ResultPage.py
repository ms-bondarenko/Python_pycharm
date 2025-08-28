from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:

    def __init__(self, browser):
        self._driver = browser

    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "div.product-card__controls-container a[href='#']")
        print(len(buy_buttons))

        self._driver.execute_script("document.querySelector('div.b-basket-popinfo-e-block').style.display='none';")
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return counter