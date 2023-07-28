import time

from pages.form_page import FormPage
from conftest import browser

def test_form_validate(browser):
    form_validate = FormPage(browser)
    form_validate.visit()
    print(form_validate.user_email.get_dom_attribute("pattern"))
    assert form_validate.first_name.get_dom_attribute("placeholder") == "First Name"
    assert form_validate.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert form_validate.user_email.get_dom_attribute("placeholder") == "name@example.com"
    assert form_validate.user_email.get_dom_attribute("pattern") == "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$" #регулятор выражение
    form_validate.btn_submit.click_force()
    time.sleep(3)
    print(form_validate.user_form.get_dom_attribute("class"))
    assert form_validate.user_form.get_dom_attribute("class") == "was-validated"