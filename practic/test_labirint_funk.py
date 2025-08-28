import selenium
from selenium import webdriver
from  selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cookie = {
    "name": "cookie_policy",
    "value": "1"
}


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
def open_labirint():
    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.add_cookie(cookie)

def search(term):
    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

def add_books():
    buy_buttons = browser.find_elements(By.CSS_SELECTOR, "div.product-card__controls-container a[href='#']")
    print(len(buy_buttons))

    browser.execute_script("document.querySelector('div.b-basket-popinfo-e-block').style.display='none';")
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter +=1
    return counter

def go_to_cart():
    browser.get("https://www.labirint.ru/cart/")

def get_cart_counter():
    try:
        full_text = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#basket-default-prod-count2"))
        ).text
        count_text = full_text.split()[0]
        return count_text
    except Exception as e:
        print("Ошибка при получении счетчика корзины:", e)
        return None  # Возвращаем None в случае ошибки


def test_cart_counter():
    open_labirint()
    search("dskhn9863yiorklfhdssfsd7778787///7sg")
    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    assert added == int(cart_counter)

    browser.quit()