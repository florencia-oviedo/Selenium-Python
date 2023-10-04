import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_by_class():
    driver = webdriver.Chrome()
    driver.get('http://www.automationpractice.pl/index.php')
    #web_element = driver.find_element(By.CLASS_NAME,'sf-with-ul')
    #web_element.click()

    #varios elementos
    web_element = driver.find_elements(By.CLASS_NAME, 'sf-with-ul')
    print('Cantidad de elementos con esa Clase: ', len(web_element))
    web_element[0].click()
    time.sleep(10)


def test_element_by_id():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.ID, 'field2')
    web_element.send_keys('Juan')

    time.sleep(10)

def test_element_by_name():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.NAME, 'ejemplo que ande')
    web_element.send_keys('flores')

    time.sleep(5)


def test_element_by_xpath():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    web_element = driver.find_element(By.XPATH, '//*[contains(@class,"form-control") and @id="name"]')
    web_element.send_keys('Juan')

    time.sleep(5)