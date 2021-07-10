# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:57:01 2020

@author: LARRY PRATO
"""
# Whasapp bot for sending file and a message for a list of cellphone numbers using selenium
from selenium import webdriver
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('lang=pt-br')
driver = webdriver.Chrome(executable_path = r'C:/Users/userpath/Selenium/chromedriver.exe',  chrome_options=options) #replace userpath for your path
driver.implicitly_wait(5)
driver.get('https://web.whatsapp.com/')
time.sleep(10)


df= pd.read_excel('C:/Users/filepath/file.xlsx') #replace userpath for your file list
for i in range(n):
    name = df['nome'][i]
    telefone = str(df['telefone'][i])
    file_tem = df['documento'][i]
    mensagem = df['texto'][i]
    
    filepath="C:/Users/filepath1/"+file_tem # replace filepath1 by your filepath
    
    aux = 'https://api.whatsapp.com/send?phone='+telefone
    driver.get(aux)
    step1 = driver.find_element_by_class_name("_whatsapp_www__block_action")
    step1.click()
    step2 = driver.find_element_by_link_text('use o WhatsApp Web') 
    step2.click()
    
    chat_box = driver.find_element_by_class_name('_3uMse')
    chat_box.click()
    time.sleep(3)
    chat_box.send_keys(mensagem)
    time.sleep(5)
    botao_enviar = driver.find_element_by_xpath("//span[@data-testid='send']")
    time.sleep(3)
    botao_enviar.click()
    time.sleep(3)
    attachment_box = driver.find_element_by_xpath('//div[@title = "Anexar"]')
    attachment_box.click()
    time.sleep(3)
    image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(filepath)
    time.sleep(3)
    botao_enviar = driver.find_element_by_xpath("//span[@data-testid='send']")
    time.sleep(3)
    botao_enviar.click()
    time.sleep(3)  