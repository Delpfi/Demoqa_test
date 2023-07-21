import time

from pages.demoqa import DemoQa
def test_size_page(browser):
    page_elemen = DemoQa(browser)
    page_elemen.visit()
    browser.set_window_size(1000,300)
    time.sleep(2)
    browser.set_window_size(1000,1000)

