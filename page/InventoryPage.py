import logging
from selene import have, query
from selene.support import by
from selene.support.conditions.be import visible
from selene.support.shared.jquery_style import s
from page import ProductPage, CartPage
from utils.base.BaseTest import do

nameHeader = s(by.xpath("//div[@class='app_logo']"))
numberProductsInCart = s(by.xpath("//*[@class='shopping_cart_badge']"))
linkToCartPage = s(by.xpath("//*[@class='shopping_cart_link']"))

estHeaderPageName = "Swag Labs"
inventoryHtml = "https://www.saucedemo.com/inventory.html"

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


def checkHeaderNameIs(estHeaderName: str):
    try:
        nameHeader.with_(timeout=5).should(visible)
        LOG.info("Header Name = : " + nameHeader.get(query.text))
        if nameHeader.get(query.text) == estHeaderName:
            return True
        else:
            return False
    except BaseException:
        return False


def addProductsToCart(listProducts: list):
    for CartElement in listProducts:
        do.click(s(by.text(CartElement)), "нажатие на продукт: " + CartElement)
        ProductPage.clickToAddToCart()
        ProductPage.clickToBackToProducts()


def checkProductNumberInCart(estListProduct):
    if numberProductsInCart.get(query.text) == str(len(estListProduct)):
        return True


def checkCartContainsNewProduct(estListProduct):
    do.click(linkToCartPage, "открываем корзину")
    return CartPage.checkProductPresentInChar(estListProduct)
