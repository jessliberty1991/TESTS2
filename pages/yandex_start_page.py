from pages.base_page import BasePage
from locators.yandex_locators import YandexLocators
from selenium.webdriver.common.keys import Keys
import time
from tests.utils import log

class YandexStartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._search_field = self.find(YandexLocators.SEARCH_FIELD,wait_time=3,name="Поисковая строка")

    def get_search_field(self):
        return  self._search_field

    def input_text(self,text: str):
        log(f"Вводим {text} в  {str(self._search_field)}")
        self._search_field.send_keys(text)
        return self._search_field

    def check_suggest(self):
        return self.find(YandexLocators.SUGGEST,wait_time=1,name="Саггест")

    def press_enter(self):
        self._search_field.send_keys(Keys.ENTER)

    def get_menu_button(self):
        return self.find(YandexLocators.ALL_SERVICE, wait_time=2,name ="Кнопка меню")

    def get_panel_service(self):
        return self.find(YandexLocators.SERVICES_PANEL, wait_time=2,name="Панель сервисов яндекса")

    def get_images_category(self):
        return self.find(YandexLocators.SERVICES_BLOCK, wait_time=4,name="Категории")









