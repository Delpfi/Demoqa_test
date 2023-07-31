from pages.base_page import BasePage
from components.components import WebElement
class WebTables(BasePage):
    def __init__(self,driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver,self.base_url)

        self.registration_form = WebElement(driver,"#registration-form-modal")
        self.btn_add = WebElement(driver,"#addNewRecordButton")
        self.btn_submit = WebElement(driver,"#submit")
        """Поля в диалоге"""
        self.first_name = WebElement(driver,"#firstName")
        self.last_name = WebElement(driver,"#lastName")
        self.user_email = WebElement(driver,"#userEmail")
        self.age = WebElement(driver,"#age")
        self.salary = WebElement(driver,"#salary")
        self.department = WebElement(driver,"#department")

        self.btn_record = WebElement(driver,"#edit-record-1")
        self.btn_delete = WebElement(driver,'span[title="Delete"]')
        self.user_form = WebElement(driver,"#userForm")

        """tables"""
        self.form_list = WebElement(driver,"div.rt-table > div.rt-tbody > div ")

        """Поиск строки"""
        self.search = WebElement(driver,"#searchBox")
        self.no_data = WebElement(driver, "div.rt-noData")

        """выпадающий список со строчками"""
        self.select_wrap = WebElement(driver, "span.select-wrap.-pageSizeOptions > select")
        #self.select_wrap_value = WebElement(driver, "select > option:nth-child(1)")

        self.btn_next = WebElement(driver,"div.-next > button")
        self.btn_previous = WebElement(driver,"div.-previous > button")
        """Кол-во страниц всего"""
        self.page_info = WebElement(driver,"span.-pageInfo > span")

        """Текущий номер страницы"""
        self.page_number = WebElement(driver,"input[type=number]")

        self.element_alerts = WebElement(driver,"div:nth-child(1) > div > div > div:nth-child(3) > span > div")
        """заголовок столбца First Name - имя, и на столбец можно нажать"""
        self.head_first_name = WebElement(driver,"div.rt-thead.-header > div > div:nth-child(1)")
        self.list_first_name = WebElement(driver, "div.rt-tbody > div > div > div:nth-child(1)")



