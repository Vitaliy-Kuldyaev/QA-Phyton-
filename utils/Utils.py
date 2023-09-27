import logging
import time

import selene
import selene.api
import selenium

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


def headerPrecondicion():
    LOG.info("")
    LOG.info("")
    LOG.info("")
    LOG.info("--- подготовка к проверке")


def getWebBrowser() -> selenium.webdriver.Chrome:
    return selene.api.browser.driver()


def generateUUID():
    return str(int(time.time()))
