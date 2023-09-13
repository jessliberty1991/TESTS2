from pages.yandex_start_page import YandexStartPage
from pages.yandex_image_page import YandexImagePage, screenshot
from tests.utils import compare_to_screenshots,log

HOME_PAGE  =  "https://ya.ru/"
IMAGE_PAGE = 'https://ya.ru/images/'
#Тест выводит логи как в консоль так и в файл

class TestImagesPage:
    def test_image(self, driver,preconditions):
        try:
            log("ТЕСТ ДЛЯ ПРОВЕРКИ КАРТИНОК В ЯНДЕКС")
            log("Переход на стартовую страницу")
            start_page = YandexStartPage(driver)
            input = start_page.get_search_field()
            assert input,log('Не отображается поисковое поле')
            log("Клик по поисковому полю")

            start_page.click(input)
            more = start_page.get_menu_button()
            assert more, log('Не отображается иконка с надписью Все','Error')
            log("Клик по кнопке Все сервисы")

            start_page.click(more)
            img_item = start_page.get_images_category()
            assert input, log('Не отображаются категории картинок','Error')


            start_page.click(img_item)
            log("Переходим на страницу картинок")

            image_page = YandexImagePage(driver)
            image_page.switch_to_next_page()
            assert image_page.check_url(IMAGE_PAGE), log(f"URL страницы не соответствует{IMAGE_PAGE}",'Error')
            num_cat = 1
            log(f"Переходим на {num_cat} категорию  ")
            name_category = image_page.choice_category(num_cat)
            image_page.switch_to_next_page()

            res = image_page.check_text_in_search(name_category)
            assert res==True, log(f"Имя категории не находится в поисковом поле  {name_category}",'Error')
            block_images = image_page.get_result_images()
            log(f"Кликаем на первую картинку из категории")

            item = image_page.choice_image_from_block(1)
            image_page.switch_to_next_page()
            assert image_page.check_load_fullscreen_image(),log('Картинка для превью не загружена','Error')
            img_preview = image_page.get_image_preview()
            prop_img = image_page.property_element(img_preview)
            path_to_screenshot = screenshot(prop_img['x'],prop_img['y'],prop_img['w'],prop_img['h'],'img.jpg')
            log(f"При помощи стрелки вправо преходим на следующую картинку")

            image_page.switch_to_next_image()
            assert image_page.check_load_fullscreen_image(), log('Картинка для превью не загружена','Error')
            img2_preview = image_page.get_image_preview()
            path_to_screenshot2 = screenshot(prop_img['x'], prop_img['y'], prop_img['w'], prop_img['h'],
                                                       'img2.jpg')
            log("Сравниваем первую и вторую картинки")
            assert  compare_to_screenshots(path_to_screenshot,path_to_screenshot2)==False, log('Картинки не должны быть одинаковыми','Error')
            log(f"При помощи стрелки влево преходим на предыдущую картинку")

            image_page.switch_to_prev_image()
            assert image_page.check_load_fullscreen_image(), log('Картинка для превью не загружена','Error')
            path_to_screenshot3 = screenshot(prop_img['x'], prop_img['y'], prop_img['w'], prop_img['h'],
                                                        'img3.jpg')
            log("Проверяем, что вернулись на исходную картинку")

            assert compare_to_screenshots(path_to_screenshot, path_to_screenshot3), log('Текущая картинка не равна исходной','Error')
            log("Тест пройден")
        except  OSError as e:
            log(str(e),"Error")























