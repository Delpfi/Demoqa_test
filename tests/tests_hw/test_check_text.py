import time

from pages.elements_page import ElementsPage


def test_page_elements_hw(browser):
    """Задание #1"""
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.footer_text.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."


    """Задание №2"""
    #
    elements_page.btn_elements.click()
    time.sleep(3)
    assert elements_page.text_place.get_text() == "Please select an item from left to start practice."