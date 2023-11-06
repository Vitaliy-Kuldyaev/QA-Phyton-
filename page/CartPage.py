import logging

from selene import browser, query
from selene.support import by
from selene.support.shared.jquery_style import s, ss

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
        for i in range(__nameProducts.get(query.size)):
            actText.append(__nameProducts[i].get(query.text))
        result = set(actText) == set(estListProduct)
    except BaseException:
        pass
    LOG.info("--- est: " + str(estListProduct))
    LOG.info("--- act: " + str(actText))
    return result


def clearCart():
    while __removeBtn.get(query.size) > 0:
        __removeBtn[0].click()
    # for i in range(__removeBtn.get(query.size)):
    #     __removeBtn[i].click()
    #     browser.driver.refresh()
