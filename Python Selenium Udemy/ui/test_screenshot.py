import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By



@mark.prueba
def test_element_iframes():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    driver.save_screenshot('./imagen3.png')