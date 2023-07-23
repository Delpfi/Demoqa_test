import time

from pages.text_box import TextBox

def test_clear(browser):
    user_name = TextBox(browser)
    user_name.visit()
    user_name.user_name.send_keys("Vadim")
    time.sleep(2)
    user_name.user_name.clear()
    time.sleep(2)
    assert user_name.user_name.get_text() == ""