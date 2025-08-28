import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


from Pages.LoginPage import LoginPage
from Pages.AddedItems import AddedItems
from Pages.DataEntryPage import DataEntryPage

def test_shop_pages():
    browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    try:
        login_page = LoginPage(browser)
        login_page.login_input()
        added_page = AddedItems(browser)
        added_page.added_items()
        data_page = DataEntryPage(browser)
        data_page.data_entry()

        summary_element = browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
        summary_text = summary_element.text.strip()
        summary_value = float(summary_text.replace('Total: ', '').replace('$', '').replace(',', ''))

        expected_sum = 58.29
        assert summary_value == expected_sum, (f"Сумма не совпадает. Извлечённая сумма:"
                                               f" ${summary_value:.2f}, Ожидаемая сумма: ${expected_sum:.2f}")
        print("Суммы совпадают", summary_value)


    finally:
        browser.quit()