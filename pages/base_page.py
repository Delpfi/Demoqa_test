import logging
import time
from components.components import WebElement
from selenium.webdriver.common.by import By
class BasePage:
    def __init__(self,driver, base_url):
        self.driver = driver
        self.base_url = base_url

        self.metaView = WebElement(driver, 'head > meta')

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self): #кнопка назад
        self.driver.back()

    def forward(self): #вперед кнопка
        self.driver.forward()

    def refresh(self): #обновить
        self.driver.refresh()


    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def  equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False

