import logging

from selene.conditions import visible
from selene.support import by
from selene.support.jquery_style_selectors import s

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
        nameHeader.assure(visible, timeout=5)
        LOG.info("Header Name = : " + nameHeader.text)
        if nameHeader.text == estHeaderName:
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
    if numberProductsInCart.should_be(visible, 10).text == str(len(estListProduct)):
        return True


def checkCartContainsNewProduct(estListProduct):
    do.click(linkToCartPage, "открываем корзину")
    return CartPage.checkProductPresentInChar(estListProduct)
