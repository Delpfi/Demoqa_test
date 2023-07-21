import random
import time

from pages.widgets_slider import Widgets_Silder



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








