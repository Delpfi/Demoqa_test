import time
from pages.text_box import TextBox
from conftest import browser

def test_text_box(browser):
    elementes_box = TextBox(browser)
    elementes_box.visit()
    full_name = "Vadim"
    elementes_box.user_name.send_keys(full_name)
    print(elementes_box.user_name.get_text())
    time.sleep(3)
    current_address = "Блюхеро 7"
    elementes_box.current_address.send_keys(current_address)
    elementes_box.btn_submit.click()
    time.sleep(5)

    output_elements_name= elementes_box.output_current_name.get_text().split(':')[1]
    output_elements_address = elementes_box.output_current_address.get_text().split(':')[1]
    assert output_elements_name == full_name
    assert output_elements_address == current_address

