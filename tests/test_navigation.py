from pages.elements_page import ElementsPage
from pages.demoqa import DemoQa
def test_navigation(browser):
    page_DemoQ = DemoQa(browser)
    page_elem= ElementsPage(browser)

    page_DemoQ.visit()
    page_DemoQ.btn_elements.click()
    page_DemoQ.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert page_elem.equal_url()