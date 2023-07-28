import time
from conftest import browser
import pytest
from pages.accordion import Accordion
from pages.alerts import Alert
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserTab
@pytest.mark.parametrize("pages", [Accordion, Alert, DemoQa, BrowserTab] )
def test_seo_mets(browser,pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.metaView.exist()
    assert page.metaView.get_dom_attribute("name") == "viewport"
    assert page.metaView.get_dom_attribute("content") == "width=device-width,initial-scale=1"

