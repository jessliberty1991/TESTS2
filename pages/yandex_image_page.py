from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.yandex_locators import YandexLocators
import urllib.parse
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image, ImageGrab


def screenshot(x, y, w, h, file_name):
    img = ImageGrab.grab((x, y, w, h))
    img.save(file_name)
    return file_name


class YandexImagePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._search_field=''
        self._block_images=''

    def get_image_preview(self):
        return self.find(YandexLocators.FULL_SCREEN_IMAGE, wait_time=4,name="Полноэкранная картинка")

    def switch_to_next_image(self):


        button_next = self.get_next_button()
        try:
            self.click(button_next)
        except:
            AttributeError('Элемент next_button не является кнопкой')
        self.switch_to_next_page()


    def switch_to_prev_image(self):
        button_prev = self.get_back_button()
        self.click(button_prev)
        self.switch_to_next_page()
        time.sleep(3)


    def get_search_field(self):
        self._search_field = self.find(YandexLocators.SEARCH_FIELD_IN_IMAGES, wait_time=4,name="Поисковое поле")
        return self._search_field

    def check_text_in_search(self,word:str):
         url = urllib.parse.unquote(self.driver.current_url)
         split_url = url.split('&text=')
         text = split_url[len(split_url)-1]
         return text == word

    def get_result_images(self):
        return self.find(YandexLocators.IMAGES_BLOCK, wait_time=8,name="Блок картинок")

    def choice_image_from_block(self,num_image:int):
        """Принимает в качетве аргумента порядковый номер картинки из блока
        Возвращает выбранную картинку"""

        num_image = num_image - 1
        locator = (By.CSS_SELECTOR, YandexLocators.IMAGE_ITEM + str(num_image) + ' a')
        item = self.find(locator, wait_time=5, name = f"Картинка #{num_image+1}")
        assert item != None , 'Отсутствует первая картнка в блоке'
        self.click(item)
        return item

    def check_load_fullscreen_image(self):
        img = self.find(YandexLocators.FULL_SCREEN_IMAGE ,wait_time=10,name="Контейнер для картинки")
        LOCATOR = (By.CSS_SELECTOR,".MMImage-Preview")
        img_scr = self.find(LOCATOR,wait_time=6,name="Полноэкранная картинка")
        width = img_scr.get_attribute("width")
        height = img_scr.get_attribute("height")
        return not ((width == 24)and(height == 24))

    def get_next_button(self):
        return  self.find(YandexLocators.NEXT_BUTTON , wait_time=6,name="Кнопка вперед")

    def get_back_button(self):
        return self.find(YandexLocators.BACK_BUTTON, wait_time=6,name="Кнопка назад")


    def choice_category(self, num_category: int):
        """Приниает порядковый номер категории и возвращает в качестве значения название категории"""

        num_category = num_category-1
        locator = (By.CSS_SELECTOR, YandexLocators.CATEGORIES_ITEM + str(num_category) + ' a')
        locator_with_text = (By.CSS_SELECTOR, YandexLocators.CATEGORIES_ITEM + str(num_category) + ' a .PopularRequestList-SearchText')
        item = self.find(locator,wait_time=4,name="Категория")
        name_category = self.find(locator_with_text, wait_time=4,name="Имя категории")
        self.click(item)
        return name_category.text













