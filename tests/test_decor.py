import time

import pytest

from pages.demoqa import DemoQa
from conftest import browser
from pages.radiobutton import RadioButton


@pytest.mark.skip
def test_decor(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    h_5_list = demoqa.h_5_element.find_elements()

    # for item in h_5_list:
    #     print(item.text)
    assert demoqa.h_5_element.check_count_elements(6)
    for item in h_5_list:
        assert item.text != ""

#@pytest.mark.skipif(True)
def test_radio_button(browser):
    radio_but = RadioButton(browser)

    if not radio_but.code_stats():
        pytest.skip(reason = f"Страница{radio_but.base_url} недоступна")
    radio_but.visit()
    radio_but.yes.click()
    assert radio_but.yes_text.get_text() == "You have selected Yes"
    radio_but.impressive.click()
    time.sleep(3)
    #assert radio_but.impressive_text.get_text() == "You have selected Impressive"
    #assert "disabled" in radio_but.no.get_dom_attribute("class")
