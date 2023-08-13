from conftest import browser
from pages.text_box import TextBox
import allure

@allure.feature('check attr')
@allure.story('Проверка атирибута placeholder')
@allure.severity(allure.severity_level.NORMAL)
def test_placeholder(browser):
    placeholder_attr = TextBox(browser)
    placeholder_attr.visit()
    assert placeholder_attr.user_name.get_dom_attribute("placeholder") == "Full Name"



@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail(browser):
    assert 111 == 222