from pages.demoqa import DemoQa
def test_seo(browser):

    obj = DemoQa(browser)
    obj.visit()
    print(obj.get_title())
    assert obj.get_title() == "DEMOQA"

