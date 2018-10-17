import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

DRIVER = os.getenv('DRIVER', 'headless_chrome')


def get_chrome_driver():
    desired_capabilities = webdriver.DesiredCapabilities.CHROME
    desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(
        "--user-data-dir=/tmp/browserdata/chrome --disable-plugins --disable-instant-extended-api")
    desired_capabilities.update(chrome_options.to_capabilities())

    browser = webdriver.Chrome(
        executable_path='chromedriver',
        desired_capabilities=desired_capabilities)

    # Desktop size
    browser.set_window_position(0, 0)
    browser.set_window_size(1366, 768)

    return browser


def get_headless_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver')
    return driver


DRIVERS = {
    'chrome': get_chrome_driver,
    'headless_chrome': get_headless_chrome
}


def get_browser_driver():
    return DRIVERS.get(DRIVER)()
