import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_element_textbox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    checkbox = driver.find_element(By.ID, 'sunday')
    print('Seleccionado: ', checkbox.is_selected())
    time.sleep(3)
    checkbox.click()
    time.sleep(3)

    print("tipo de elemento: ", checkbox.get_attribute('type'))
    print('Seleccionado: ',checkbox.is_selected())