import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def browser():
    edge_driver_path = r"C:\Users\SMART\Desktop\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    browser.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")

    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3"))
    )
    browser.execute_script("arguments[0].scrollIntoView();", button)
    actions = ActionChains(browser)
    actions.move_to_element(button).click().perform()

    zip_code_field=browser.find_element(By.CSS_SELECTOR, "#zip-code")

    background_color = browser.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;",
                                              zip_code_field)

    print("Цвет фона элемента с ID 'zip-code':", background_color)

    expected_background = "rgb(248, 215, 218)"

    assert expected_background == background_color, "Цвета не совпадают"
    print("zip_code" + str(expected_background == background_color))

    field_ids = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position",
        "company"
        ]
    for field_id in field_ids:
        field_element = browser.find_element(By.ID, field_id)
        background_color = (browser.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;",
                                                  field_element))

        expected_backgrounds = [
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)",
            "rgb(209, 231, 221)"
        ]

        all_match = True
        for field_id, expected_background in zip(field_ids, expected_backgrounds):
            field_element = browser.find_element(By.ID, field_id)
            background_color = browser.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;",
                                                      field_element)

            if expected_background != background_color:
                print(
                    f"Цвет фона для элемента '{field_id}' не совпадает. Ожидалось: {expected_background}, получено: {background_color}")
                all_match = False

        if all_match:
            print("Все цвета совпадают")
        else:
            print("Некоторые цвета не совпадают")
