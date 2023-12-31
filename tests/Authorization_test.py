import testit

from page import InventoryPage
from utils.base.BaseTest import BaseTest, do
from utils.enums.UsersCredentials import UsersCredentials


class Test_authorization(BaseTest):
    # pass
    @testit.workItemID(100)
    @testit.displayName("saucedemo_100 Тестирование авторизации")
    def test_Saucedemo_100(self, uuid):
        do.open('https://www.saucedemo.com/', user=UsersCredentials.STANDARTUSER)
        do.checkBool(InventoryPage.checkHeaderNameIs(InventoryPage.estHeaderPageName), "страница загружена")

    @testit.workItemID(101)
    @testit.displayName("saucedemo_101 Тестирование авторизации. Негативный тест")
    def test_Saucedemo_101(self, randomUser):
        do.open('https://www.saucedemo.com/', loginData=randomUser)
        do.checkBool(not InventoryPage.checkHeaderNameIs(InventoryPage.estHeaderPageName), "страница не загружена")



