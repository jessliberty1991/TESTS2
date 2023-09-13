from pages.yandex_start_page import YandexStartPage
from pages.yandex_search_page import YandexSearchPage
from tests.utils import log


#Тест выводит логи как в консоль так и в файл
HOME_PAGE  =  "https://ya.ru/"
TEXT_FOR_INPUT = "Тензор"
EXAMPLE_URL = "https://tensor.ru"
class TestYandexPage:
    def test_search_page(self,driver,preconditions):
        try:
            log("ТЕСТ ДЛЯ ПРОВЕРКИ ПОИСКОВОЙ ВЫДАЧИ ПО ЗАПРОСУ 'ТЕНЗОР'")
            log("Переход на стартовую стрницу Яндекса")

            start_page = YandexStartPage(driver)
            input = start_page.get_search_field()
            a = type(input)
            assert type(input) != 'NoneType' ,log('Поисковая строка не найдена','Error')
            log(f"Вводим в поисковую строку текст {TEXT_FOR_INPUT}")

            start_page.input_text(TEXT_FOR_INPUT)
            log("Проверяем наличие саггеста")

            suggest = start_page.check_suggest()
            assert type(suggest) != 'NoneType', log('Подсказка не найдена','Error')
            start_page.press_enter()
            log("Перешли на страницу поисковой выдачи")
            search_page = YandexSearchPage(driver)
            result_page = search_page.get_load_result_page()
            assert type(result_page) != 'NoneType', log('Страница поисковой выдачи не найдена','Error')
            log(f"Проверяем первую ссылку на соответствие {EXAMPLE_URL} ")
            first_anchor = search_page.get_first_anchor(url = EXAMPLE_URL)
            assert first_anchor!=None, log('Первая ссылка не является целевой ссылкой','Error')
            log("Тест пройден")
        except OSError as e:
            log(str(e),'Error')








