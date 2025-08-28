from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# browser= webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https://ya.ru")
    sleep(5)
    browser.save_screenshot('./ya_'+browser.name+'.png')
    sleep(5)
    browser.quit()

make_screenshot(Chrome)
make_screenshot(ff)