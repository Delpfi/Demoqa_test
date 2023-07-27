from conftest import browser
from pages.text_box import TextBox
def test_placeholder(browser):
    placeholder_attr = TextBox(browser)
    placeholder_attr.visit()
    assert placeholder_attr.user_name.get_dom_attribute("placeholder") == "Full Name"
