import time

from pages.progressbar import ProgressBar
def testprogress_bar(browser):
    bar = ProgressBar(browser)
    bar.visit()
    time.sleep(2)

    bar.btn_start.click()
    while bar.progre_bar.get_dom_attribute("aria-valuenow") != "51": # while True  - клик, после break
        if bar.progre_bar.get_dom_attribute("aria-valuenow") == "51":
            bar.btn_start.click()
    time.sleep(3)

