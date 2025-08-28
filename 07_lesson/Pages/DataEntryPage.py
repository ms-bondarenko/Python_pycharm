from selenium.webdriver.common.by import By

class DataEntryPage():

    def __init__(self, browser):
        self._driver = browser

    def data_entry(self):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Михаил")
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Бондаренко")
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("352900")
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()