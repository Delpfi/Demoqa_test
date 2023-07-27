import random
import time

from pages.webtables import WebTables
from selenium import webdriver
from conftest import browser
#driver = webdriver.Chrome()
def test_webtables(browser):
    browser.maximize_window()
    obj_web_tables = WebTables(browser)
    obj_web_tables.visit()

    assert obj_web_tables.btn_add.exist()
    obj_web_tables.btn_add.click()
    assert obj_web_tables.registration_form.get_text() == "Registration Form"
    obj_web_tables.btn_submit.click()
    if obj_web_tables.user_form.get_dom_attribute("class") == "was-validated":
        print("Поля не заполнены")
    """Данные и поля , которыми будем заполнять"""
    first_name = "Ivan"
    obj_web_tables.first_name.send_keys(first_name)
    last_name = "Ivanov"
    obj_web_tables.last_name.send_keys(last_name)
    email = "IIvan@mail.ru"
    obj_web_tables.user_email.send_keys(email)
    age = random.randint(20,90)
    obj_web_tables.age.send_keys(age)
    salary = random.randint(10000,50000)
    obj_web_tables.salary.send_keys(salary)
    departmant = "Legaall"
    obj_web_tables.department.send_keys(departmant)
    """Для сохранения нажимаем submit"""
    obj_web_tables.btn_submit.click()
    assert obj_web_tables.btn_add.exist() #диалог закрылся, есть кнопка add
    time.sleep(5)
    new_person = [first_name, last_name,str(age) ,email , str(salary), departmant] # новый сотрудник
    people_list = obj_web_tables.form_list.find_elements()
    print(new_person)
    table_result = []
    for item in people_list:
        table_result.append(item.text.splitlines()) # таблица результатов, всех сотрудник
    print(table_result)
    assert new_person in table_result # проверяем, что сотрудник новый есть в общем списке
    obj_web_tables.btn_record.click() #нажать на карандаш
    time.sleep(1)
    assert obj_web_tables.registration_form.get_text() == "Registration Form" #открыт диалог с данными
    if obj_web_tables.user_form.get_dom_attribute("class") != "was-validated":
        print("Поля заполнены")
    old_first_name = obj_web_tables.first_name.get_dom_attribute("value") #получаем старое имя
    new_first_name = "Nina"
    obj_web_tables.first_name.send_keys(new_first_name)
    time.sleep(3)
    obj_web_tables.btn_submit.click() #сохраняем новое имя
    assert old_first_name != new_first_name #проверка что именна разные
    obj_web_tables.search.send_keys("IIvan@mail.ru") #найти сотрудника по email
    time.sleep(3)
    obj_web_tables.btn_delete.click()# - удалить найденную строку
    time.sleep(3)



