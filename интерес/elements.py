from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

txt=driver.find_element(By.CSS_SELECTOR,"a[data-statlog='2informers.stocks.item.1']").text
id=driver.find_element(By.CSS_SELECTOR,"a[data-statlog='2informers.stocks.item.1']").id
href=driver.find_element(By.CSS_SELECTOR,"a[data-statlog='2informers.stocks.item.1']").get_attribute("href")
ff=driver.find_element(By.CSS_SELECTOR,"a[data-statlog='2informers.stocks.item.1']").value_of_css_property("font-family")
color=driver.find_element(By.CSS_SELECTOR,"a[data-statlog='2informers.stocks.item.1']").value_of_css_property("color")
print(txt)
print(id)
print(href)
print(ff)
print(color)