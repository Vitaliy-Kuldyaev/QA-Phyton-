import allure
from selene.elements import SeleneElement
from selene.support.conditions import be

from page import LoginPage
from utils.Utils import *
from utils.enums.UsersCredentials import UsersCredentials
from utils.solenoid.Solenoid import Solenoid
from utils.steps import StepBase

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()


class doClass(object):
    @allure.step("Открыть сайт: {site}, логин: {loginData}")
    def open(self, site: str, loginData: {} = None, user: UsersCredentials = None):
        Solenoid.open(site)
        self.headerLog()
        LOG.info("------- Открытие страницы: " + site)
        if loginData is not None:
            LOG.info("------- User: " + loginData.get("name"))
            self.send(LoginPage.userNameLocator, loginData.get("name"), "установить userName")
            self.send(LoginPage.userPasswordLocator, loginData.get("password"), "установить userPassword")
            self.click(LoginPage.loginBtnLocator, "кнопка LOGIN")
        if user is not None:
            LOG.info("------- User: " + user.login)
            self.send(LoginPage.userNameLocator, user.login, "Login Name: " + user.login)
            self.send(LoginPage.userPasswordLocator, user.password, "Login password: " + user.password)
            self.click(LoginPage.loginBtnLocator, "кнопка LOGIN")
        self.footerLog()

    @allure.step("Заполнить элемент: {message}")
    def send(self, el: SeleneElement, value: str, message: str):
        self.headerLog()
        LOG.info("------- Отправить значение: " + value + "  в элемент: " + el.tag_name + "  Описание: " + message)
        for i in range(5):
            LOG.info("--- проверка на наличие элемента")
            el.should(be.visible).should_be(be.enabled)
            el.clear()
            LOG.info("--- установка значения: " + value)
            el.set(value)
            LOG.info("--- --- Act text: " + el.text)
            LOG.info("--- --- Act value: " + el.get_attribute('value'))
            if el.text == value or el.get_attribute('value') == value:
                logging.info("--- Значение установлено")
                break
            else:
                logging.info("--- ERROR значение не установлено, повтор: " + str(i))
        self.footerLog()
        return self

    def headerLog(self):
        LOG.info("")
        LOG.info("")
        LOG.info("____________________________________")
        LOG.info("-------------Start Step-------------")

    def footerLog(self):
        LOG.info("-------------End Step---------------")
        LOG.info("____________________________________")

    @allure.step("Нажатие на элемент: {message}")
    def click(self, el: SeleneElement, message: str):
        self.headerLog()
        LOG.info("------- Нажатие: " + message)
        el.should_be(be.visible, 10).click()
        self.footerLog()
        return self

    @allure.step("Проверка: {message}")
    def checkBool(self, action: bool, message: str):
        self.headerLog()
        LOG.info("Проверка: " + message)
        assert action == True
        self.footerLog()
        return self

    @allure.step("Проверка: {message}")
    def checkNotBool(self, action: bool, message: str):
        self.headerLog()
        LOG.info("Проверка: " + message)
        assert action == False
        self.footerLog()
        return self

    @allure.step("Выполнить действия: {message}")
    def step(self, step: StepBase, message: str):
        LOG.info("")
        LOG.info("-------------------------------------")
        LOG.info("Выполнено действие: " + message)
        LOG.info("-------------------------------------")
        return self
