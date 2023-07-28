from pages.base_page import BasePage
from components.components import WebElement
class Alert(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/alerts"
        super().__init__(driver,self.base_url)

        self.btn_aller = WebElement(driver,"#alertButton")
        self.btn_aller_confirm = WebElement(driver,"#confirmButton")
        self.result = WebElement(driver,"#confirmResult")
        self.btn_promt = WebElement(driver,"#promtButton")
        self.result_prompt = WebElement(driver,"#promptResult")
        self.btn_timer_alert = WebElement(driver,"#timerAlertButton")