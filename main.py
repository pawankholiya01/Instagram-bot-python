# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 23:36:02 2019

@author: Pawan Kholiya
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("my python bot")
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(10)
username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
password = driver.find_element_by_xpath('//*[@name="password"]')
username.send_keys("khpawan5@gmail.com")
password.send_keys("p@w@nkh5")
time.sleep(1)

password.send_keys(Keys.ENTER)
time.sleep(10)

driver.get("https://www.instagram.com/hritvikkaushik/")
time.sleep(8)
follow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/button')
time.sleep(5)
print("*****")
print(follow.text)
time.sleep(5)
if (follow.text != 'Following'and follow.text!='Requested'):
    follow.click()