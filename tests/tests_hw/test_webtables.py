import random
import time

from selenium.webdriver import ActionChains, Keys

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


def test_webtable_text(browser):
    browser.maximize_window()
    obj_web_tables_1 = WebTables(browser)
    obj_web_tables_1.visit()

    assert not obj_web_tables_1.no_data.exist()
    people_list_1 = obj_web_tables_1.form_list.find_elements()
    for item in people_list_1:
        obj_web_tables_1.btn_delete.click()
    assert not obj_web_tables_1.form_list.find_elements()

def test_next_previous(browser):
    #browser.maximize_window()
    action = ActionChains(browser)
    webtable_next_previous = WebTables(browser)
    webtable_next_previous.visit()
    # find_elemnt = webtable_next_previous.element_alerts.find_element()
    # action.move_to_element(find_elemnt).perform()
    time.sleep(5)
    assert webtable_next_previous.get_url() == "https://demoqa.com/webtables" #проверка, что открыта страница webtable
    webtable_next_previous.select_wrap.click_force()
    webtable_next_previous.select_wrap.send_keys("5 rows")
    webtable_next_previous.select_wrap.send_keys(Keys.ENTER)
    time.sleep(3)

    assert webtable_next_previous.select_wrap.get_attribute_value() == '5' # проверка, что 5 строк только на 1 странице
    assert webtable_next_previous.btn_next.get_dom_attribute("disabled") #проверка, что Next -кнопка не активна
    assert webtable_next_previous.btn_previous.get_dom_attribute("disabled") #проверка, что Previous -кнопка не активна
#Сотрудники - создаем 3 раза
    i=0
    while i<3:
        webtable_next_previous.btn_add.click()
        first_name = "Ivan"
        webtable_next_previous.first_name.send_keys(first_name)
        last_name = "Ivanov"
        webtable_next_previous.last_name.send_keys(last_name)
        email = "IIvan@mail.ru"
        webtable_next_previous.user_email.send_keys(email)
        age = random.randint(20, 90)
        webtable_next_previous.age.send_keys(age)
        salary = random.randint(10000, 50000)
        webtable_next_previous.salary.send_keys(salary)
        departmant = "Legaall"
        webtable_next_previous.department.send_keys(departmant)
        """Для сохранения нажимаем submit"""
        webtable_next_previous.btn_submit.click()
        i+=1
    assert not webtable_next_previous.btn_next.get_dom_attribute("disabled") # кнопка Next доступна
    assert webtable_next_previous.page_info.get_text() == "2" #проверка, что появилась 2-ая страница
    time.sleep(2)
    webtable_next_previous.btn_next.click() #кликаем на Next
    assert webtable_next_previous.page_number.get_dom_attribute("value") == "2" #проверка , что открылась вторая старница
    time.sleep(3)
    webtable_next_previous.btn_previous.click()
    assert webtable_next_previous.page_number.get_dom_attribute("value") == "1" #проверка , что открылась первая старница
    time.sleep(3)




