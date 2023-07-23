from pages.base_page import BasePage
from components.components import WebElement
class TextBox(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/text-box"
        super().__init__(driver, self.base_url)

        """Поля для ввода данных"""
        self.user_name = WebElement(driver,"#userName")
        self.current_address = WebElement(driver, "#currentAddress")

        """Результат с данными output-выход"""
        self.output_current_address = WebElement(driver,"#output > div > #currentAddress")
        self.output_current_name = WebElement(driver,"#output > div > #name")

        """Кнопка submit"""
        self.btn_submit = WebElement(driver,"#submit")