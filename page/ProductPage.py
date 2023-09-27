from selene.support import by
from selene.support.jquery_style_selectors import s, ss

from utils.base.BaseTest import do

__addToCartBtn = s(by.xpath("//*[contains(@name,'add-to-cart')]"))
__backToProducts = s(by.xpath("//*[@name='back-to-products']"))



def clickToAddToCart():
    do.click(__addToCartBtn, "ProductPage add to Cart")


def clickToBackToProducts():
    do.click(__backToProducts, "ProductPage click to backToProducts")
