from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Инициализация драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/inputs")
search_locator = 'input[type="number"]'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Sky")
sleep(5)
search_input.clear()
sleep(5)
search_input.send_keys("Pro")
sleep(5)
driver.quit()