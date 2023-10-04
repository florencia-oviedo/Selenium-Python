import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_element_textbox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    web_element = driver.find_element(By.ID,'name')
    web_element.send_keys('Florencia')
    text = web_element.get_attribute('value')
    print(text)
    web_element.clear()
    web_element.send_keys('Sakura card captor')
    text= web_element.get_attribute('value')
    print(text)
    assert text == 'Sakura card captor'

    time.sleep(4)



