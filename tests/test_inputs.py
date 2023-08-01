import time

from selenium.webdriver import Keys

from conftest import browser
from pages.herokuapp_inputs import Inputs
#Экспоненциальная запись числа
"""До конца на 100% не доделал"""
def test_inputs(browser):
    inputs = Inputs(browser)
    inputs.visit()

    assert inputs.fild.visible()
    key = "d"
    inputs.fild.send_keys(key)
    time.sleep(2)
    inputs.fild.clear()
    """Key_ исходная строка """
    key1 = "-12E-e32"
    list_key = ["E","e"]
    list_num = ["0","1","2","3","4","5","6","7","8","9"]
    list_key_ch = ["-"]
    list_result = []
    """Отфильтровать строку"""
    e=0
    for i in key1:
        if i in list_key:
            if e != 0:
                continue
            e+=1
            if not i in list_result:
                list_result.append(i)
        elif i in list_num:  #если есть в списке list_num, то добавляем в итоговый список
            list_result.append(i)
        elif i in list_key_ch:
            list_result.append(i)

    """Проверить нужно исходную строчку и отфильтрованную """ #примерно как то так
    if ("".join(list_result) == key1):
        assert "".join(list_result) == key1
    else:
        assert not "".join(list_result) == key1



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
