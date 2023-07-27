import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

class WebElement:
    def __init__(self,driver,locator="", locator_type = "css"):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)


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
        return self.driver.find_elements(self.get_by_type(),self.locator)

    def check_count_elements(self,count: int):
        if len(self.find_elements()) == count:
            return True
        return False

    def get_attribute_value(self):
        return self.find_element().get_attribute("value")

    def get_dom_attribute(self, name):
        value = self.find_element().get_dom_attribute(name)
        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

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

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type"+ self.locator_type + "not correct")
        return False

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
            self.find_element()
        )

    def check_css(self, style, value = ""):
        return self.find_element().value_of_css_property(style) == value