import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()


    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()


    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()


    driver.find_element(By.CSS_SELECTOR, "#checkout").click()


    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Михаил")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Бондаренко")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("352900")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()


    summary_element = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
    summary_text = summary_element.text.strip()
    summary_value = float(summary_text.replace('Total: ', '').replace('$', '').replace(',', ''))


    expected_sum = 58.29
    assert summary_value == expected_sum, (f"Сумма не совпадает. Извлечённая сумма:"
                                           f" ${summary_value:.2f}, Ожидаемая сумма: ${expected_sum:.2f}")
    print("Суммы совпадают", summary_value)

