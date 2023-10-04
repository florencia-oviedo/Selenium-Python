import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark


def test_navegacion_browser():
    driver = webdriver.Chrome()
    driver.get('https://demo.opencart.com//') #accediendo a una URl

    print(('URL actual: ', driver.current_url))

    driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/form/div/div[1]/a').click()

    print(('URL actual: ', driver.current_url))
    driver.back()
    print(('URL actual: ', driver.current_url))

    driver.forward()
    print(('URL actual: ', driver.current_url))

    driver.refresh()

    print(('URL actual: ', driver.current_url))

    time.sleep(3)


