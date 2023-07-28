import time

from pages.demoqa import DemoQa
from pages.accordion import Accordion
from pages.alerts import Alert
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
import pytest
from conftest import browser
def test_seo(browser):

    obj = DemoQa(browser)
    obj.visit()
    print(obj.get_title())
    assert obj.get_title() == "DEMOQA"

@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == "DEMOQA"
