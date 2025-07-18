from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(10)
# driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
# try:
#     button.click()
#     print("Кнопка была нажата!")
# except Exception as e:
#     print(f"Произошла ошибка: {e}")
try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    button.click()
    print("Кнопка была нажата!")
except Exception as e:
    print(f"Произошла ошибка: {e}")
