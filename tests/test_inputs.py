import time

from selenium.webdriver import Keys

from conftest import browser
from pages.herokuapp_inputs import Inputs
#Экспоненциальная запись числа
def test_inputs(browser):
    inputs = Inputs(browser)
    inputs.visit()

    assert inputs.fild.visible()
    key = "d"
    inputs.fild.send_keys(key)
    time.sleep(2)
    inputs.fild.clear()
    key1 = "e-1232"
    inputs.fild.send_keys(key1)
    inputs.fild.send_keys(Keys.ENTER)
    #print(inputs.fild_1.find_element())
    time.sleep(2)
    inputs.fild.clear()
    i=0
    while i <5:
        inputs.fild.send_keys(Keys.UP)
        i+=1
    time.sleep(2)
    inputs.fild.clear()
    y=0
    while y > -5:
        inputs.fild.send_keys(Keys.DOWN)
        y-=1
    time.sleep(2)
    inputs.fild.clear()
    time.sleep(3)

    #assert inputs.fild.text == "e-1232"