import time

from pages.alerts import Alert
from conftest import browser

def test_aller(browser):
    allert = Alert(browser)
    allert.visit()
    assert not allert.alert()
    allert.btn_aller.click()
    time.sleep(2)
    assert allert.alert()
    allert.alert().accept()


def test_alert_text(browser):
    allert_text = Alert(browser)
    allert_text.visit()
    allert_text.btn_aller.click()
    time.sleep(2)
    assert allert_text.alert().text == "You clicked a button"
    allert_text.alert().accept()
    assert not allert_text.alert()

def test_confirm(browser):
    allert_dism = Alert(browser)
    allert_dism.visit()
    allert_dism.btn_aller_confirm.click()
    time.sleep(2)
    allert_dism.alert().dismiss()
    assert allert_dism.result.get_text() == "You selected Cancel"
    time.sleep(2)


def test_prompt(browser):
    allert_prompt = Alert(browser)
    allert_prompt.visit()
    allert_prompt.btn_promt.click()
    time.sleep(2)
    allert_prompt.alert().send_keys("Vadim")
    allert_prompt.alert().accept()
    assert allert_prompt.result_prompt.get_text() == "You entered Vadim"

def test_timer_alert(browser):
    alert_timer = Alert(browser)
    alert_timer.visit()
    assert alert_timer.btn_timer_alert.visible()
    alert_timer.btn_timer_alert.click()
    time.sleep(6)
    assert alert_timer.alert().text == "This alert appeared after 5 seconds"
    alert_timer.alert().accept()
