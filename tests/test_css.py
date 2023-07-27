from pages.elements_page import ElementsPage
from conftest import browser
def testflex_menu(browser):
    element = ElementsPage(browser)
    element.visit()
    assert element.element_list_check_css.check_css('flex', '0 0 25%')
    assert element.element_list_check_css.check_css('max-width',"25%")
    browser.set_window_size(500,740)
    assert element.element_list_check_css.check_css('flex', '0 0 100%')
    assert element.element_list_check_css.check_css('max-width', "100%")
    browser.set_window_size(1000,1000)
