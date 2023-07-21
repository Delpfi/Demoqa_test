import time
from pages.accordion import Accordion

def test_visivle_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    assert accordion_page.elemnts_accordion.visible()

    accordion_page.btn_element_accordion.click()
    time.sleep(2)
    assert not accordion_page.elemnts_accordion.visible()


def test_visible_accordion_default(browser):
    accordion_visible = Accordion(browser)
    accordion_visible.visit()

    assert not accordion_visible.elements_content_section_1.visible()
    assert not accordion_visible.elements_content_section_2.visible()
    assert not accordion_visible.elements_content_section_3.visible()



