import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_element_calendar():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    calendar = driver.find_element(By.ID,'datepicker')
    calendar.click()

    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@class = "ui-state-default" and text() = "23"]').click()
    time.sleep(2)

    calendar.click()
    driver.find_element(By.XPATH, '//*[@class = "ui-state-default" and text() = "14"]').click()

    time.sleep(2)

    calendar.clear()
    calendar.send_keys('01/01/2001' + Keys.ENTER)

    time.sleep(4)



