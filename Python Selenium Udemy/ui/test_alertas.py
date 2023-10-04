import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


def test_element_alertas():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    driver.find_element(By.XPATH,'//*[@id="HTML9"]/div[1]/button[2]').click()
    alerta = Alert(driver)
    texto = alerta.text
    print('texto de alerta: ',texto)

    alerta.accept()
    #alerta.dismiss()


    assert driver.find_element(By.ID,'demo').text == 'You pressed OK!'

    time.sleep(3)