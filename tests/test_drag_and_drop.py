import time
from conftest import browser
from pages.droppable import Droppable
from selenium.webdriver import ActionChains
def test_drag_and_drop(browser):
    droppable_el = Droppable(browser)
    action_chains = ActionChains(browser)
    droppable_el.visit()
    assert droppable_el.drop.check_css('background-color',"rgba(0, 0, 0, 0)")
    action_chains.drag_and_drop(droppable_el.drag.find_element(), droppable_el.drop.find_element()).perform()
    assert droppable_el.drop.check_css("background-color", "rgba(70, 130, 180, 1)")

    action_chains.drag_and_drop_by_offset(droppable_el.drag.find_element(),-200,0).perform()
    time.sleep(2)

    assert droppable_el.drop.check_css("background-color", "rgba(70, 130, 180, 1)")