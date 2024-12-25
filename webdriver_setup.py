from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def setup_webdriver():
    chrome_driver_path = r"C:\chromedriver-win64\chromedriver.exe"
    service = Service(chrome_driver_path)


    options = webdriver.ChromeOptions()
    chrome_prefs = {
        "profile.default_content_settings.popups": 2,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2
    }
    options.add_experimental_option("prefs", chrome_prefs)


    driver = webdriver.Chrome(service=service, options=options)
    return driver
