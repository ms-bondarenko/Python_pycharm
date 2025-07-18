from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.common.by import By



# Инициализация драйвера для Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")
sleep(5)
search_locator="#username"
search_input=driver.find_element(By.CSS_SELECTOR,search_locator).send_keys("tomsmith")
search_locator="#password"
search_input=driver.find_element(By.CSS_SELECTOR,search_locator).send_keys("SuperSecretPassword!")
sleep(5)