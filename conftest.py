import logging
import random

import allure
import pytest
from mimesis import Person, Locale
from selenium import webdriver
from selene import browser
from webdriver_manager.chrome import ChromeDriverManager

from page import CartPage
from utils.Utils import generateUUID
from utils.base.BaseTest import do

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger()
prev_test_screenshot = None
prev_test_page_source = None


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'htmlunit',
                              'version': '2',
                              'javascriptEnabled': True})
    browser.config.driver = driver
    browser.config.driver = (webdriver.Chrome(ChromeDriverManager().install()))
    yield
    browser.quit()


@pytest.fixture(autouse=True)
def uuid(request):
    return generateUUID()


@pytest.fixture(autouse=True)
def randomUser():
    person = Person(Locale.RU)
    name = person.username(mask='l_d')
    password = person.password(length=16, hashed=False)
    do.headerLog()
    LOG.info("------- Генерация пользователя")
    LOG.info("------- Login: " + name)
    LOG.info("------- Password: " + password)
    do.footerLog()
    return {"name": name, "password": password}


@pytest.fixture()
def newCartProduct(request):
    marker = request.node.get_closest_marker('newCartProducts')
    data = None if marker is None else list(marker.args[0][0])
    numberNewCartElements = None if marker is None else marker.args[0][1]
    if len(data) < numberNewCartElements:
        do.headerLog()
        LOG.info("------- Ошибка: количество запрашиваемых товаров не больше количества тестовых")
        do.footerLog()
        return None
    randomPosition = random.sample(range(len(data)), numberNewCartElements)
    resultListProducts = []
    for i in randomPosition:
        resultListProducts.append(data[i])
    return resultListProducts


@pytest.fixture()
def clearCart():
    yield
    do.open(CartPage.getHref())
    do.step(CartPage.clearCart(), "очистка корзины")


def pytest_exception_interact():
    with allure.step('Screenshot'):
        last_screenshot = browser.config.last_screenshot
        allure.attach.file(
            source=last_screenshot,
            attachment_type=allure.attachment_type.PNG
        )
