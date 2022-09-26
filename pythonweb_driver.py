# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:21:42 2022

@author: user

python for web
"""

from selenium import webdriver
import pandas as pd

exl = pd.read_excel('C:/Users/user/Downloads/A2648-F-HRD801-middle.xlsx')
keys = ['Chr','Start', 'End', 'Ref', 'Alt']
inputtext = ''
for i in keys:
    inputtext += str(exl[i][4])
    inputtext += ' '

#start with login page
bower = webdriver.Chrome()
bower.get('https://varsome.com/sign-in/?ssologin=1&next=https://varsome.com/')

cookies_button = bower.find_element_by_id('onetrust-accept-btn-handler')
cookies_button.click()

email = bower.find_element_by_name('username')
password = bower.find_element_by_name('password')

email.send_keys('B07404014@ntu.edu.tw')
password.send_keys('zonalin890721')

password.submit()
#
search = bower.find_element_by_name('query')
search.send_keys(inputtext)

https://varsome.com/
bower = webdriver.Chrome()
bower.get()
