from pages.base_page import BasePage
from components.components import WebElement
class InternetHeroku(BasePage):

    def __init__(self,driver):
        self.base_url = "https://the-internet.herokuapp.com/"
        super().__init__(driver,self.base_url)

        self.btn_add = WebElement(driver,"#content > ul > li:nth-child(2) > a")
        self.btn_element = WebElement(driver,"#content > div > button")

        self.btn_elements_list = WebElement(driver,"div.example > div> button")
        #self.btn_del_1 = WebElement(driver,"#elements > button:nth-child(1)")
        self.btn_del = WebElement(driver,"#elements > button")