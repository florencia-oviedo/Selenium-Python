import time
from selenium.webdriver.common.by import By

base_url = 'https://testautomationpractice.blogspot.com/'

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.wikipedia_Search = '//*[@id="Wikipedia1_wikipedia-search-input"]'
        self.date_picker = 'datepicker'
