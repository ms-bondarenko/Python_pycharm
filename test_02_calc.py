import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculator(setup):
    driver = setup
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    for value in ['7', '+', '8', '=']:
        driver.find_element(By.XPATH, f"//*[contains(text(), '{value}')]").click()


    result = WebDriverWait(driver, 50).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '15')]"))
    )

    assert result.text == "15" , f"Expected '15', but got '{result.text}'"

    if result.text == "15":
        print("результат равен 15")
    else:
        print("результат неверен")