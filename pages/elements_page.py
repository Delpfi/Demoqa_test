from pages.base_page import BasePage
from components.components import WebElement
class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url="https://demoqa.com/elements"
        super().__init__(driver, self.base_url)

        self.text_place =WebElement(driver,"#app > div > div > div.row > div.col-12.mt-4.col-md-6 ")
        self.text_elements = WebElement(driver,'div.playgound-header> div')
        self.icon = WebElement(driver, " header > a > img")
        self.btn_sidebar_first = WebElement(driver, "div:nth-child(1) > span > div")
        self.btn_sidebar_first_textbox = WebElement(driver,'div:nth-child(1) > div > ul > #item-0 > span')


        """Домашнее задание """
        self.footer_text = WebElement(driver,"footer")
        self.btn_elements= WebElement(driver,"div.home-body>div>div:nth-child(1)")

        self.btn_sidebar_two_textbox_check_box = WebElement(driver,"div:nth-child(1) > div > ul > #item-1 > span")
        self.count_element = WebElement(driver,"div:nth-child(1) > div > ul > li")
