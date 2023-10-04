import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_element_iframes():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    my_iframe = driver.find_element(By.ID,'frame-one796456169')

    driver.switch_to.frame(my_iframe)

    driver.find_element(By.ID,'RESULT_TextField-0').send_keys('Flor')

    time.sleep(3)