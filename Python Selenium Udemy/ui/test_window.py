import time

from pytest import mark
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_element_iframes():
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')

    print(driver.current_window_handle)
    print(len(driver.window_handles))

    driver.find_element(By.XPATH,'//*[@id="HTML4"]/div[1]/button').click()

    print(len(driver.window_handles))

    driver.switch_to.new_window('tab')
    print(len(driver.window_handles))

    driver.close()
    driver.switch_to.window(driver.window_handles[1])

    #driver.set_window_size(1024,768)

    #driver.maximize_window()
    #driver.minimize_window()

    driver.switch_to.new_window('window')


    time.sleep(3)