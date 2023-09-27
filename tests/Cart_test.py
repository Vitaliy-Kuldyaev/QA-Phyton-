import pytest
import testit

from page import InventoryPage
from utils.base.BaseTest import BaseTest, do
from utils.enums.UsersCredentials import UsersCredentials
from utils.globalVariable import defaultAddress
from utils.products import Products


class Test_Cart(BaseTest):

    @testit.workItemIds(102)
    @testit.links(type=testit.LinkType.DEFECT)
    @testit.displayName("saucedemo_102 Проверка корзины. Добавление элементов")
    @pytest.mark.newCartProducts(Products.getAllProduct(numberNewCartElements=3))
    @pytest.mark.usefixtures('clearCart')
    def test_Saucedemo_102(self, newCartProduct):
        do.open(defaultAddress, user=UsersCredentials.STANDARTUSER)
        do.step(InventoryPage.addProductsToCart(newCartProduct), "добавляем продукты в корзину")
        do.checkBool(InventoryPage.checkProductNumberInCart(newCartProduct), "количество товаров соответствует")
        do.checkBool(InventoryPage.checkCartContainsNewProduct(newCartProduct), "в корзину добавлены только необходимые продукты")
