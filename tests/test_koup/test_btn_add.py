import time

from selenium.webdriver import ActionChains

from conftest import browser
from pages.internet_heroku_app import InternetHeroku
def test_btn_add(browser):
    btn_element = InternetHeroku(browser)
    btn_element.visit()
    assert btn_element.equal_url()
    assert btn_element.btn_add.visible()
    btn_element.btn_add.click()
    assert btn_element.get_url() == "https://the-internet.herokuapp.com/add_remove_elements/"
    assert btn_element.btn_element.get_text() == "Add Element"
    assert btn_element.btn_element.get_dom_attribute("onclick") == "addElement()"
    action = ActionChains(browser)
    btn_el = btn_element.btn_element.find_element()
    action.double_click(btn_el).perform()
    action.double_click(btn_el).perform()
    time.sleep(5)
    list_elements = btn_element.btn_elements_list.find_elements()
    #assert btn_element.btn_elements_list.check_count_elements(4)

    for i in list_elements:
         btn_element.btn_del.click()
         time.sleep(2)
    time.sleep(3)

    assert not btn_element.btn_del.exist()