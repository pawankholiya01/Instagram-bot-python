# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:36:02 2019

@author: Pawan Kholiya
"""

from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys
print("my python bot")
driver = webdriver.Chrome()
driver.get("https://10.10.11.1:8090/")
time.sleep(1)
username = driver.find_element_by_xpath('//*[@id="username"]')
password = driver.find_element_by_xpath('//*[@id="password"]')
username.send_keys("login_id")
password.send_keys("pass_word")

password.send_keys(Keys.ENTER)
time.sleep(2)
sys.exit(0)
