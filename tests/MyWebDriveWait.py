from selenium.webdriver.remote.webelement import WebElement





class MyWebElement(WebElement):
    def __init__(self,name, parent, id):
        super().__init__(parent, id)
        self._rus_name = name



    def __str__(self):
        return self._rus_name






