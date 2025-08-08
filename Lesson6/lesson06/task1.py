from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")


driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Data loaded with AJAX')]"))
    )
txt=driver.find_element(By.XPATH, "//*[contains(text(), 'Data loaded with AJAX')]").text
print(txt)
driver.quit()


