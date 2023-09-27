import logging

from selene import browser
from selene.support import by
from selene.support.jquery_style_selectors import s, ss

from utils.globalVariable import defaultAddress

__directLinkPage = "cart.html"
__nameProducts = ss(by.xpath("//*[@class='inventory_item_name']"))
__removeBtn = ss(by.xpath("//button[contains(@name,'remove')]"))

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


def getHref():
    return defaultAddress + __directLinkPage


def checkProductPresentInChar(estListProduct):
    result: bool = False
    actText = []
    try:
        for i in range(__nameProducts.size()):
            actText.append(__nameProducts[i].text)
        result = set(actText) == set(estListProduct)
    except BaseException:
        pass
    LOG.info("--- est: " + str(estListProduct))
    LOG.info("--- act: " + str(actText))
    return result


def clearCart():
    numberProductToDelete = __removeBtn.size()
    for i in range(numberProductToDelete):
        __removeBtn[0].click()
        browser.driver().refresh()
