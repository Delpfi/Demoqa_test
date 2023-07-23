import time

from selenium.webdriver import  Keys
from pages.form_page import FormPage
from conftest import browser
def test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()

    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testervich")
    form_page.user_email.send_keys("test@mail.ru")
    time.sleep(2)
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("79997563641")
    form_page.hobbies.click_force()
    form_page.current_address.send_keys("Блюхеро 11корп2")

    #Задание со звездочкой
    # form_page.select_state.click()
    # form_page.input_state.send_keys("Haryana")
    # form_page.input_state.send_keys(Keys.ENTER)
    # form_page.select_city.click()
    # form_page.input_city.send_keys("Panipat")
    # form_page.input_city.send_keys(Keys.ENTER)

    # time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(5)
    # form_page.close_LargeModal.send_keys(Keys.ENTER)
    # time.sleep(2)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_mdal.click_force()

def test_state_City(browser):
    form_page_SC = FormPage(browser)
    form_page_SC.visit()
    browser.maximize_window()
    # Задание со звездочкой
    form_page_SC.select_state.click()
    form_page_SC.input_state.send_keys("Haryana")
    form_page_SC.input_state.send_keys(Keys.ENTER)
    form_page_SC.select_city.click()
    form_page_SC.input_city.send_keys("Panipat")
    form_page_SC.input_city.send_keys(Keys.ENTER)
    time.sleep(5)

