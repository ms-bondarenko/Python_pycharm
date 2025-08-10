from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.python.org/")
driver.find_element(By.LINK_TEXT, "Donate").click()
sleep(10)

driver.get("https://www.google.com")
search_locator="#APjFqb"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python")
search_input.send_keys(Keys.RETURN)
sleep(50)
driver.quit()

