import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_element_cookies():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    print('Cookies: ', driver.get_cookies())

    driver.add_cookie({'name':'udemy','value':'cookies browser'})
    print('Cookies: ', driver.get_cookies())

    driver.delete_cookie('udemy')
    print('Cookies: ', driver.get_cookies())

    driver.delete_all_cookies()
