import random
import time

from selenium.webdriver import Keys

from pages.widgets_slider import Widgets_Silder
from conftest import browser


def test_value(browser):
    browser.maximize_window()
    silder = Widgets_Silder(browser)
    silder.visit()
    value_silder_old = silder.value_slider.get_attribute_value() #значение по умолчение - 25
    input_silder = silder.input_silder.find_element() #получить элемент- всю строчку range-slider
    silder.input_silder.drag_and_drop_by_offset(input_silder,random.randint(1,100),0)# - передвигаю по оси Х, так как горизонтальная строка, У=0, по полученному элементу(строку)
    value_silder_new = silder.value_slider.get_attribute_value()#получаю новое значение, после сдвига
    print(value_silder_old,value_silder_new)
    time.sleep(3)
    assert value_silder_old != value_silder_new


def test_slider(browser):
    silder = Widgets_Silder(browser)
    silder.visit()
    # assert silder.input_silder.visible()
    # assert  silder.value_slider.get_attribute_value() == "25"
    # input = silder.input_silder.find_element()
    # silder.input_silder.drag_and_drop_by_offset(input,1,0)
    # assert silder.value_slider.get_attribute_value() == "50"
    # time.sleep(5)

    while not silder.value_slider.get_attribute_value() == "50":
        silder.input_silder.send_keys(Keys.ARROW_RIGHT)

    time.sleep(5)







