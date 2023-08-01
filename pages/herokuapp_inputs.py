from pages.base_page import BasePage
from components.components import WebElement

class Inputs(BasePage):
    def __init__(self,driver):
        self.base_url = "https://the-internet.herokuapp.com/inputs"
        super().__init__(driver,self.base_url)

        self.fild = WebElement(driver, "input[type=number]")
        self.fild_1 = WebElement(driver, '//*[@id="content"]/div/div/div/input',"xpath")