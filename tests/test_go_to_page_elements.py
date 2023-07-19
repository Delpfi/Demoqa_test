from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from components.components import WebElement
def test_go_to_page(browser):

    browser.maximize_window()
    page_elemts = DemoQa(browser)
    page_elemts.visit()

    assert page_elemts.get_url()
    page_elemts.btn_elements.click() #страница, элемент метод

    el_page = ElementsPage(browser)
    assert el_page.equal_url()
