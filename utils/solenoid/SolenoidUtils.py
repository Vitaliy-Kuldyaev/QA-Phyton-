from selene import browser
from selenium import webdriver


class SolenoidUtils:
    __webDriver: webdriver = None

    @classmethod
    def getWebDriver(cls):
        return cls.__webDriver

    @classmethod
    def openSingelton(cls, site: str):
        if cls.__webDriver is None:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--enable-automation")
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--ignore-ssl-errors=yes')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.browser_version = '118.0'
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
            cls.__webDriver = driver
            browser.config.driver = driver
        browser.open(site)

    @classmethod
    def teardown_module(cls):
        browser.quit()

    @classmethod
    def open(cls, site: str):
        cls.openSingelton(site)
