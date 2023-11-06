import pytest
import testit

from page import InventoryPage
from utils.base.BaseTest import BaseTest, do
from utils.enums.UsersCredentials import UsersCredentials
from utils.globalVariable import defaultAddress
from utils.products import Products


class Test_Cart(BaseTest):

    @testit.workItemID(102)
    @testit.displayName("saucedemo_102 Проверка корзины. Добавление элементов")
    @pytest.mark.newCartProducts(Products.getAllProduct(numberNewCartElements=3))
    @pytest.mark.usefixtures('clearCart')
    def test_Saucedemo_102(self, newCartProduct):
        do.open(defaultAddress, user=UsersCredentials.STANDARTUSER)
        do.step(InventoryPage.addProductsToCart(newCartProduct), "добавляем продукты в корзину")
        do.checkBool(InventoryPage.checkProductNumberInCart(newCartProduct), "количество товаров соответствует")
        do.checkBool(InventoryPage.checkCartContainsNewProduct(newCartProduct),
                     "в корзину добавлены только необходимые продукты")

    @testit.workItemID(103)
    @testit.displayName("saucedemo_103 Проверка корзины. Добавление элементов")
    @pytest.mark.newCartProducts(Products.getAllProduct(numberNewCartElements=3))
    @pytest.mark.usefixtures('clearCart')
    def test_Saucedemo_103(self, newCartProduct):
        do.open(defaultAddress, user=UsersCredentials.STANDARTUSER)
        do.step(InventoryPage.addProductsToCart(newCartProduct), "добавляем продукты в корзину")
        do.checkBool(InventoryPage.checkProductNumberInCart(newCartProduct), "количество товаров соответствует")
        do.checkBool(not InventoryPage.checkCartContainsNewProduct(newCartProduct),
                     "в корзину добавлены только необходимые продукты")
