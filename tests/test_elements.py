import time

from pages.check_box import CheckBox
from pages.elements_page import ElementsPage
# def test_find_elements(browser):
#     elem_page = ElementsPage(browser)
#     elem_page.visit()
#
#     assert elem_page.count_element.check_count_elements(9)


def test_count_checkbox(browser):
    check_box = CheckBox(browser)
    check_box.visit()

    assert check_box.check_box.check_count_elements(1)
    check_box.btn_check_box_click.click()
    time.sleep(3)
    assert check_box.check_box.check_count_elements(17)

    for element in check_box.check_box.find_elements():
        assert element.is_displayed()

    check_box.refresh()
    assert check_box.check_box.check_count_elements(1)

