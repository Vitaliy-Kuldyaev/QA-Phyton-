from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from utils.Utils import getWebBrowser


class Solenoid(object):
    __webDriver: WebDriver = None

    @staticmethod
    def getWebDriver():
        return Solenoid.__webDriver

    @staticmethod
    def openSingelton(site: str):
        if Solenoid.__webDriver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--enable-automation")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.browser_version = '100.0'
            chrome_options.set_capability(
                'selenoid:options',
                {
                    'screenResolution': '1920x1080x24',
                    'enableVNC': True,
                    'enableVideo': False,
                    'enableLog': True,
                },
            )
            driver = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',
                options=chrome_options
            )
            Solenoid.__webDriver = driver
            browser.set_driver(driver)
        browser.open_url(site)

    @staticmethod
    def teardown_module():
        browser.quit()

    @staticmethod
    def open(site: str):
        Solenoid.openSingelton(site)
