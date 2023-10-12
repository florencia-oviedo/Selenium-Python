import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/')
time.sleep(3)

driver.find_element(By.LINK_TEXT,'Form Authentication').click()
driver.find_element(By.ID,'username').send_keys('tomsmith')

driver.find_element(By.ID,'password').send_keys('SuperSecretPassword!')

driver.find_element(By.XPATH,'//*[@id="login"]/button').click()

textSecureArea = driver.find_element(By.XPATH,'//*[@id="content"]/div/h2').text

assert textSecureArea == 'Secure Area'