from pages.elements_page import ElementsPage
def test_find_elements(browser):
    elem_page = ElementsPage(browser)
    elem_page.visit()

    assert elem_page.count_element.check_count_elements(9)