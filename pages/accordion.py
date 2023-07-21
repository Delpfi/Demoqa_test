from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver,self.base_url)
        self.elemnts_accordion = WebElement(driver,"#section1Content > p")
        self.btn_element_accordion = WebElement(driver,"#section1Heading")

        self.elements_content_section_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.elements_content_section_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.elements_content_section_3 = WebElement(driver, '#section3Content > p')