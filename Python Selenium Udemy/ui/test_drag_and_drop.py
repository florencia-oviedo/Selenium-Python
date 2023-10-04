import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



def test_element_combobox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    source = driver.find_element(By.ID,'draggable')
    target = driver.find_element(By.ID,'droppable')

    action = ActionChains(driver)
    action.drag_and_drop(source,target).perform()
    time.sleep(3)

