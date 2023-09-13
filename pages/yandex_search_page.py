from pages.base_page import BasePage
import time
from locators.yandex_locators import YandexLocators
from selenium.webdriver.common.keys import Keys

class YandexSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
       #self.search_page = self.find(YandexLocators.SEARCH_FIELD,wait_time=5)
        #self.first_anchor = self.find(YandexLocators.FIRST_ANCHOR,wait_time=5)

    def get_load_result_page(self):
        return self.find(YandexLocators.SEARCH_PAGE,wait_time=5,name="Страница поисковой выдачи")

    def get_first_anchor(self,url:str):
         """Принимает адрес ссылки и проверяет является ли ссылка первой в поисковой выдаче"""

         first_anchor = (YandexLocators.FIRST_ANCHOR[0],YandexLocators.FIRST_ANCHOR[1]+f"[href='{url}']")
         elem = self.find(first_anchor,wait_time=4,name="Первая ссылка")
         return elem








