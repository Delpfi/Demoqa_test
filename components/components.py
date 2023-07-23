import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

class WebElement:
    def __init__(self,driver,locator=""):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)


    def exist(self):
        try:
            #self.find_element('div.login_logo')
            self.find_element()
        except NoSuchElementException:
            return False
        return True


    def get_text(self):
        return self.find_element().text

    def visible(self):
        return self.find_element().is_displayed()


    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR,self.locator)

    def check_count_elements(self,count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    def get_attribute_value(self):
        return self.find_element().get_attribute("value")

    def drag_and_drop_by_offset(self,element,x_coords,y_coords):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element,x_coords,y_coords).perform()


    def send_keys(self,text):
        self.find_element().send_keys(text)

    def click_force(self):
        self.driver.execute_script("arguments[0].click();",self.find_element())

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + "a")
        self.find_element().send_keys(Keys.DELETE)


