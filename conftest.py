import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.set_window_size(1000,1000) #- width, height
    yield driver
    driver.quit()