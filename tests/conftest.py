from selenium import webdriver
import pytest
from loguru import logger
from tests.utils import log

HOME_PAGE = "https://ya.ru"
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(HOME_PAGE)
    driver.maximize_window()
    yield driver
    driver.quit()
    return driver

@pytest.fixture
def preconditions(request):
    logger.add("debug/"+request.node.name+".log")
    log("=====================================")
    log("test case name :" + str(request.node.name))
    log("test file :" + str(request.fspath))
    yield
    log("test case name :" + str(request.node.name)+" is finished")
