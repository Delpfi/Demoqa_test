import time
from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa
from conftest  import browser
def test_size_page(browser):
     page_elemen = DemoQa(browser)
     page_elemen.visit()
     browser.set_window_size(1000,300)
     time.sleep(2)
     browser.set_window_size(1000,1000)


def test_visivle_nav_bar(browser):
    elem_nav = ElementsPage(browser)
    elem_nav.visit()
    assert not elem_nav.element_nav.visible()
    browser.set_window_size(767,1000)
    time.sleep(3)
    assert elem_nav.element_nav.visible()
    browser.set_window_size(1000,1000)
    time.sleep(3)


