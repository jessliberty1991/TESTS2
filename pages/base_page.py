from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond
from tests.MyWebDriveWait import MyWebElement
import urllib.parse
from tests.utils import log

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self,elem_locator,name,wait_time=5):
         elem = None
         log(f"Получаем элемент {name}")
         elem = WebDriverWait(self.driver, timeout=wait_time).until(exp_cond.visibility_of_element_located(elem_locator),message = f" {str(elem)} is not found")
         my_elem = MyWebElement(name = name ,parent= elem._parent, id=elem.id)
         log(f"Получили элемент {my_elem}")
         return my_elem

    def click(self,elem):
        try:
            log(f"Клик на элемент {elem}")
            elem.click()
        except AttributeError as e:
            log(f"Элемент не является кнопкой",'error')


    def check_url(self,url,wait_time = 2):
        return  WebDriverWait(self.driver, wait_time).until(exp_cond.url_to_be(url),message = f" {url} is not valid")

    def get_substr_in_url(self, substr:str ,wait_time = 3):
        url = self.driver.current_url
        url = urllib.parse.unquote(url,encoding='utf-8',
                     errors='replace')




    def switch_to_next_page(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])


    def property_element(self,elem):
        location = elem.location
        size = elem.size
        x = location['x']
        y = location['y']
        w = x + size['width']
        h = y + size['height']
        return {'x':x,'y':y,'w':w,'h':h}

