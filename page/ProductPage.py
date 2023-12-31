from selene.support import by
from selene.support.shared.jquery_style import s

from utils.base.BaseTest import do

__addToCartBtn = s(by.xpath("//*[contains(@name,'add-to-cart')]"))
__backToProducts = s(by.xpath("//*[@name='back-to-products']"))



def clickToAddToCart():
    do.click(__addToCartBtn, "ProductPage add to Cart")


def clickToBackToProducts():
    do.click(__backToProducts, "ProductPage click to backToProducts")
