import selenium
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_cart_counter():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys("Python")
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "div.product-card__controls-container a[href='#']")
    print(len(buy_buttons))

    browser.execute_script("document.querySelector('div.b-basket-popinfo-e-block').style.display='none';")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter +=1

    print(counter)
    browser.get("https://www.labirint.ru/cart/")
    full_text = browser.find_element(By.CSS_SELECTOR, "#basket-default-prod-count2").text
    count_text = full_text.split()[0]
    assert counter == int(count_text)
    sleep(3)
    browser.quit()