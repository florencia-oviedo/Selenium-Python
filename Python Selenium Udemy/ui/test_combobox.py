import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_element_combobox():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    time.sleep(3)
    select_country = Select(driver.find_element(By.ID,'country'))
    #select_country.select_by_value('3') no tiene por valor es un ejemplo si tendria

    time.sleep(3)
    select_country.select_by_visible_text('Japan')
    time.sleep(3)
