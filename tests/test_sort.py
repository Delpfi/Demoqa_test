import time
from pages.webtables import WebTables
from conftest import browser

def test_sort(browser):
    sort_elemnts = WebTables(browser)
    sort_elemnts.visit()
    time.sleep(3)
    """Проверять будем по колонке First name"""
    list_no_sord = sort_elemnts.list_first_name.list_sort_elements()
    print(list_no_sord)
    sort_elemnts.head_first_name.click()
    time.sleep(2)
    list_yes_sord = sort_elemnts.list_first_name.list_sort_elements()
    #new_list_sord = sorted(list_no_sord)
    list = sort_elemnts.form_list.list_sort_elements()
    print(list)
    assert list_no_sord != list_yes_sord #проверка, что списки разные , после сортировки до/после.
