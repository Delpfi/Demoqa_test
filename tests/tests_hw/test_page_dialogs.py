import time
from pages.modal_dialogs import ModalDialogs
def test_page_dialogs(browser):
    page_modul_dialogs = ModalDialogs(browser)
    page_modul_dialogs.visit()
    assert page_modul_dialogs.count_elements_alerts.check_count_elements(5)

