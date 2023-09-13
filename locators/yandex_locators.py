from selenium.webdriver.common.by import By

class YandexLocators:
    SEARCH_FIELD = (By.XPATH,"//input[@id = 'text' ]")
    SEARCH_FIELD_IN_IMAGES = (By.XPATH, "//input[contains(@class ,'input__control')]")
    SUGGEST = (By.CSS_SELECTOR,".mini-suggest__overlay_visible")
    SEARCH_PAGE = (By.CSS_SELECTOR,"ul#search-result" )
    FIRST_ANCHOR = (By.CSS_SELECTOR,"ul#search-result li[data-cid = '0'] a")
    ALL_SERVICE = (By.CSS_SELECTOR,'ul.services-suggest__list li a.services-suggest__item-more')
    SERVICES_PANEL = (By.CSS_SELECTOR,'div.services-more-popup')
    SERVICES_BLOCK  = (By.XPATH, "//span[@class = 'services-more-popup__item']//a[@href='https://ya.ru/images/']//div[contains(text(),'Картинки')]/ancestor::a")
    CATEGORIES_ITEM = "div.PopularRequestList div.PopularRequestList-Item_pos_"
    IMAGES_BLOCK = (By.CSS_SELECTOR,'div.serp-list_type_search')
    IMAGE_ITEM = "div.serp-list_type_search,serp-item_pos_"
    FULL_SCREEN_IMAGE = (By.CSS_SELECTOR," div.MMImageContainer img.MMImage-Preview")
    NEXT_BUTTON = (By.CSS_SELECTOR," div.MediaViewer-ButtonNext")
    BACK_BUTTON = ((By.CSS_SELECTOR," div.MediaViewer-ButtonPrev"))