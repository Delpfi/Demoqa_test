from pages.base_page import BasePage
from components.components import WebElement
class CheckBox(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/checkbox"
        super().__init__(driver,self.base_url)

        self.check_box = WebElement(driver,"span.rct-text")
        self.btn_check_box_click = WebElement(driver,"#tree-node > div > button.rct-option.rct-option-expand-all > svg")

