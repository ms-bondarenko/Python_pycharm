import selenium
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from Pages.CalcPage import CalcPage

def test_calc_page():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        calc_page = CalcPage(browser)
        calc_page.input_calc()

        result = WebDriverWait(browser, 50).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '15')]")))
        print(result.text)

        expected_res = 15

        assert expected_res == int(result.text)

    finally:
        browser.quit()





