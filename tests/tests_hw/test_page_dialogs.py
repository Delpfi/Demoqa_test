import time
from pages.modal_dialogs import ModalDialogs
from conftest import browser
def test_page_dialogs(browser):
    page_modul_dialogs = ModalDialogs(browser)
    page_modul_dialogs.visit()
    assert page_modul_dialogs.count_elements_alerts.check_count_elements(5)

def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    modal_dialogs.back()
    browser.set_window_size(900,400)
    modal_dialogs.forward()
    assert modal_dialogs.get_url() == 'https://demoqa.com/'
    assert modal_dialogs.get_title() == "DEMOQA"
    browser.set_window_size(1000,1000)