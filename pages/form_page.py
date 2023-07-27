import random

from pages.base_page import BasePage
from components.components import WebElement
class FormPage(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        super().__init__(driver,self.base_url)

        self.user_form = WebElement(driver,"#userForm")
        self.first_name = WebElement(driver,"#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.user_email = WebElement(driver, "#userEmail")
        #self.gender_radio_1 = WebElement(driver, "#genterWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)")
        self.gender_radio_1 = WebElement(driver, f"#gender-radio-{random.randint(1,3)}")
        self.user_number = WebElement(driver, "#userNumber")
        self.btn_submit = WebElement(driver, "#submit")
        self.modal_dialog = WebElement(driver, "body > div.fade.modal.show > div")
        self.btn_close_mdal = WebElement(driver, "#closeLargeModal")

        #self.close_LargeModal = WebElement(driver,"#closeLargeModal")
        self.hobbies = WebElement(driver, f"#hobbies-checkbox-{random.randint(1,3)}")
        self.current_address = WebElement(driver,"#currentAddress")

        self.input_state  = WebElement(driver,"#react-select-3-input")
        self.select_state = WebElement(driver,"#state")
        self.input_city = WebElement(driver, "#react-select-4-input")
        self.select_city = WebElement(driver, "#city")

