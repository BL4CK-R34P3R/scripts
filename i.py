#/usr/bin/python3 

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = ''
password = ''

driver = webdriver.Chrome('chromedriver')
#webbrowser.open('https://jobs.virtuallytestingfoundation.org/job/csinternship/dashboard')
#signInButton = browser.find_element_by_id('submit')
#signInButton.click()

driver.get('https://account.virtuallytestingfoundation.org/login')


