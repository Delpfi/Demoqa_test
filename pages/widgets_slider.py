from pages.base_page import BasePage
from components.components import WebElement

class Widgets_Silder(BasePage):
    def __init__(self,driver):
        self.base_url= "https://demoqa.com/slider"
        super().__init__(driver,self.base_url)
        self.input_silder = WebElement(driver,"#sliderContainer > div.col-9 > span > input")
        self.value_slider = WebElement(driver,"#sliderValue")