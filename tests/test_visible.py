import time

from pages.elements_page import ElementsPage
# def test_visible(browser):
#
#     browser.maximize_window()
#     elements = ElementsPage(browser)
#     elements.visit()
#     #elements.btn_sidebar_first.click()
#     #time.sleep(3)
#
#     #assert elements.btn_sidebar_first.exist()
#
#     assert elements.btn_sidebar_first_textbox.visibl()


def test_not_visable_btn_sidebar(browser):

    browser.maximize_window()
    elem = ElementsPage(browser)
    elem.visit()
    assert elem.btn_sidebar_two_textbox_check_box.visible()
    elem.btn_sidebar_first.click()
    time.sleep(2)
    assert not elem.btn_sidebar_two_textbox_check_box.visible()







