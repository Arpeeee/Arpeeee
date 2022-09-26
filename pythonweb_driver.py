# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:21:42 2022

@author: user

python for web
"""

from selenium import webdriver
import pandas as pd

your_email = input('your email : ')
your_password = input('your password : ')

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

email.send_keys(your_email)
password.send_keys(your_password)

password.submit()
#
search = bower.find_element_by_name('query')
search.send_keys(inputtext)


bower = webdriver.Chrome()
bower.get('https://varsome.com/')

bower.find_element_by_class_name('select-selected').send_keys = 'hg19'
