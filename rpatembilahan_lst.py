# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 03:13:54 1010

@author: hp
"""
import telebot
import datetime
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
# coding=utf-8
import sys
# sys.setdefaultencoding() does not exist, here!
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')
from unidecode import unidecode
import requests, json, urllib,time
import MySQLdb
import os
import mysql.connector
from mysql.connector import Error
import logging

logging.basicConfig(filename="/home/dwiki/logbot.log",level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
bot = "947011165:AAHpIt9HVlPrbkXC6bS07h2UqbITCCNUDXU" # Bot RTPO Tembilahan
r = requests.get('https://api.telegram.org/bot%s/getupdates?timeout=30' %bot)
jsondata = r.content
pesan = ""
text_plat = ""
text_gold = ""
text_silver = ""
text_bronze = ""
data = json.loads(jsondata)
print (data)


#def log(message,perintah):
#  tanggal = datetime.datetime.now()
#  tanggal = tanggal.strftime('%d-%B-%Y')
#  nama_awal = message.chat.first_name
#  nama_akhir = message.chat.last_name
#  id_user = message.chat.id
#  text_log = '{}, {}, {} {}, {} \n'.format(tanggal, id_user, nama_awal, nama_akhir, perintah)
#  log_bot = open('log_rpabot.txt','a')
#  log_bot.write(text_log)
#  log_bot.close()
  
for x in data['result']:
  print "\n"
  try:
    update_id = x['update_id']
  except KeyError:
    print 'No Update'
  else:
    requests.get('https://api.telegram.org/bot%s/getupdates?offset=%s' %(bot,(update_id + 1)), proxies=urllib.getproxies())

  number = x['message']['text']
  user = open('user.txt','r')
  user = user.read()
  chat_id = x['message']['from']['id']
  shift = number [-2:]
  first_name = x['message']['from']['first_name']
  if number ==  '/start':
    first_name = x['message']['from']['first_name']
    pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n"
    
  elif "create" in number:
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Create TOTI %s Done" %cari + "\n\n"
        PATH = '/usr/bin/chromedriver'
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://sumbagteng.toti-telkomsel.com")

        username = driver.find_element_by_name("username")
        username.send_keys("rtpo_tembilahan")

        password = driver.find_element_by_name("password")
        password.send_keys("SEL_AHAN")

        login = driver.find_element_by_name("submit")
        login.click()
        time.sleep(2)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pull-right-container"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Create Multiple Tiket"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "select2-selection__arrow"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "select2-search__field"))
            )
            element.send_keys(cari)
            time.sleep(2)
            element.send_keys(Keys.ENTER)  
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "permasalahan"))
            )
            element.send_keys("PLN OFF | KWH Problem") 
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "pic"))                 
            )
            element.send_keys(first_name)  # ganti nama id
            time.sleep(1)
            element.send_keys(Keys.ENTER)
                
        except:
            print("Tiket tidak berhasil dibuat")
            driver.quit()

           
        driver.quit()
  
          
  elif "ssopen" in number:    
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot Done" + "\n\n"
        PATH = '/usr/bin/chromedriver'
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://sumbagteng.toti-telkomsel.com")
        driver.set_window_size(1500, 1080)
        driver.maximize_window()
        #username = driver.find_element_by_name("username")
        #username.send_keys("rtpo_tembilahan")

        #password = driver.find_element_by_name("password")
        #password.send_keys("SEL_AHAN")

        #login = driver.find_element_by_name("submit")
        #login.click()

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            element.send_keys("rtpo_tembilahan")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            element.send_keys("SEL_AHAN")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "submit"))
            )
            element.click()
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pull-right-container"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Data Open"))
            )
            element.click()
            #driver.execute_script("document.body.style.zoom='60%'")
            time.sleep(2)
            driver.save_screenshot("/home/dwiki/screenshot.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()

        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshot.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()

  elif "close" in number:
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Close TOTI %s Done" %cari + "\n\n"
        PATH = '/usr/bin/chromedriver'
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("https://sumbagteng.toti-telkomsel.com")

        username = driver.find_element_by_name("username")
        username.send_keys("rtpo_tembilahan")

        password = driver.find_element_by_name("password")
        password.send_keys("SEL_AHAN")

        login = driver.find_element_by_name("submit")
        login.click()
        time.sleep(2)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "pull-right-container"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Data Open"))
            )
            element.click()
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input.form-control.input-sm"))
            )
            element.click()
            element.send_keys(cari)
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn.btn-info.btn-sm.share-cover"))
            )
            element.click()   
            time.sleep(6)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button#skip-rating-tiket.btn.btn-info.skip-rating-tiket"))
            )
            element.click() 
            time.sleep(2)    
            
        except:
            print("Close tiket tidak berhasil")
            driver.quit()

        driver.quit()
        
  elif "scdfmc" in number:
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Create SCD FMC %s Done" %cari + "\n\n"
        PATH = '/usr/bin/chromedriver'
        options = Options()
        options.page_load_strategy = 'normal'
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        driver.get("http://10.9.97.226/mbp/#/auth")
        
        username = driver.find_element_by_id("input-email")
        username.send_keys("dwikikun")
        
        password = driver.find_element_by_id("input-password")
        password.send_keys("Poring@1234")
        time.sleep(1.5)
        password.send_keys(Keys.ENTER)
        
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "nb-menu"))
            )
            element.click()
            time.sleep(1.5)
        
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Monitoring MBP"))
            )
            element.click()
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "nb-plus"))
            )
            element.click()
            time.sleep(1)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ngx-dropdown-button"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search"))
            )
            element.click()
            element.send_keys(cari)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "available-items"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "form-control-sm"))
            )
            element.click()
            element.send_keys(Keys.ARROW_DOWN)
            element.send_keys(Keys.ENTER)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-md.btn-primary"))
            )
            element.click()
            time.sleep(2)
            
            
        except:
            print("Tiket tidak berhasil dibuat")
            driver.quit()
        
        driver.quit()
        
  elif "ssranpag" in number:
    if str(chat_id) in str(user):    
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot Done" + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.35.193.59/cacti/plugins/weathermap/weathermap-cacti-plugin.php")

        try:
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("dewadis")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("apaya")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            driver.get("http://10.35.193.59/cacti/plugins/weathermap/weathermap-cacti-plugin.php?action=viewmap&id=4763d17a5b018eec9322")
            #driver.execute_script("document.body.style.zoom='75%'")
            time.sleep(2)
            driver.save_screenshot("screenshotcacti.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotcacti.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()
    
    else:
       pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
       
  elif "ssridar" in number:
    if str(chat_id) in str(user):    
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot Done" + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.1.73.190/cacti/plugins/weathermap/weathermap-cacti-plugin.php?action=viewmap&id=31f702521f439d5c7b9d")

        try:
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("admin")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("ganteng123")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            #driver.execute_script("document.body.style.zoom='75%'")
            time.sleep(2)
            driver.save_screenshot("screenshotmeridar.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotmeridar.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()
    
    else:
       pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
       
  elif "ssrikep" in number: 
    if str(chat_id) in str(user):   
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot Done" + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.1.73.190/cacti/plugins/weathermap/weathermap-cacti-plugin.php?group_id=3")

        try:
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("admin")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("ganteng123")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            #driver.execute_script("document.body.style.zoom='75%'")
            time.sleep(2)
            driver.save_screenshot("screenshotmerikep.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotmerikep.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()
  
    else:
         pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
       
  elif "sssumbar" in number:  
    if str(chat_id) in str(user):   
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot Done" + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.1.73.190/cacti/plugins/weathermap/weathermap-cacti-plugin.php?group_id=6")

        try:
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("admin")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("ganteng123")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            #driver.execute_script("document.body.style.zoom='75%'")
            time.sleep(2)
            driver.save_screenshot("screenshotmesumbar.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotmesumbar.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()
  
    else:
       pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
                    
  elif "sstn" in number: 
    if str(chat_id) in str(user):    
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot CACTI TN %s Done" %cari + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.37.2.188/cacti/")

        try:
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("cacti")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("cacti")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            
            driver.get("http://10.37.2.188/cacti/graph_view.php")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "tree_4_anchor"))
            )
            element.click()
            
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "filter"))
            )
            #element.click()
            element.send_keys(cari)
            time.sleep(2)
            element.send_keys(Keys.ENTER)
            time.sleep(1.5)  
            #driver.execute_script("document.body.style.zoom='50%'")
            time.sleep(2)
            driver.save_screenshot("screenshotcactitn.png")
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit() 
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotcactitn.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()   
  
    else:
         pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
         
  
  elif "sstelkom" in number: 
    if str(chat_id) in str(user):    
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot CACTI Telkom %s Done" %cari + "\n\n"
        PATH = '/usr/bin/phantomjs'
        driver = webdriver.PhantomJS()  
        driver.get("http://10.1.73.190/cacti/")
        
        try:
    
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_username"))
            )
            element.send_keys("admin")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login_password"))
            )
            element.send_keys("ganteng123")
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            
            driver.get("http://10.1.73.190/cacti/graph_view.php?action=preview&host_id=0&graph_template_id=0")
            time.sleep(1)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "filter"))
            )
            time.sleep(1)
            #element.click()
            element.send_keys(cari)
            time.sleep(2)
            element.send_keys(Keys.ENTER)
            time.sleep(2)
            driver.save_screenshot("screenshotcactitlkm.png")
            time.sleep(2)
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "graphimage"))
            )
            element.click()
            time.sleep(1.5)
            driver.save_screenshot("screenshotcactitlkm2.png")
            time.sleep(2)
            
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotcactitlkm.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines() 
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotcactitlkm2.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()  
  
    else:
         pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')
        
       
  elif "ssenm" in number: 
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        from selenium.webdriver.firefox.options import Options   
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Screenshot EAS ENM Done" + "\n\n"
        binary = '/usr/bin/firefox'
        options = Options()
        options.page_load_strategy = 'normal'
        options.headless = True
        driver = webdriver.Firefox(options=options, firefox_binary=binary)
        
        driver.get("https://ran7enm01.telkomsel.co.id/login/?goto=https://ran7enm01.telkomsel.co.id")
        time.sleep(2)
        
        #private = driver.find_element_by_id("details-button")
        #private.click()
        
        #proceed = driver.find_element_by_id("proceed-link")
        #proceed.click()
        #time.sleep(1.5)
        
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "loginNoticeOk"))
            )
            element.click()
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "loginUsername"))
            )
            element.send_keys("dwikikun")
            
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "loginPassword"))
            )
            element.send_keys("Poring@123")
               
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.torLogin-Holder-formButtonImage"))
            )
            element.click()  
            time.sleep(1.5)
                
            driver.get("https://ran7enm01.telkomsel.co.id/#alarmoverview/alarmviewer")
            time.sleep(5)
            driver.execute_script("document.body.style.zoom='40%'")
            time.sleep(1.5)
            driver.save_screenshot("screenshotenm.png")
            
        
        except:
            print("Screenshot tidak berhasil")
            driver.quit()
        
        driver.quit()        
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/screenshotenm.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()
        
        
  elif 'getid' in number:
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + 'Your ID = ' + str(chat_id)
                    
  elif 'help' in number:
        pesan = 'Hello %s :)' %first_name + "\n"
        pesan+= '/getid - Get Your Telegram ID' + "\n"
        pesan+= '/create [siteid] - Create tiket ANT TOTI'+ "\n"
        pesan+= '/close [siteid] - Close tiket ANT TOTI'+ "\n"
        pesan+= '/ssopen - Screenshot tiket Open ANT TOTI'+ "\n"
        pesan+= '/scdfmc [siteid] - Create tiket SCD FMC BAST'+ "\n"
        pesan+= '/ssranpag - Screenshot CACTI Router RAN PAG'+ "\n"
        pesan+= '/ssridar - Screenshot CACTI Arnet Telkom Ridar'+ "\n"
        pesan+= '/ssrikep - Screenshot CACTI Arnet Telkom Rikep'+ "\n"
        pesan+= '/sssumbar - Screenshot CACTI Arnet Telkom Sumbar'+ "\n"
        pesan+= '/sstn [siteid] - Screenshot CACTI Minilink TN'+ "\n"
        pesan+= '/sstelkom [siteid] - Screenshot CACTI Metro / GPON Telkom'+ "\n"
        pesan+= '/ssenm - Screenshot EAS Aktif ENM7 Dwiki'+ "\n"
        pesan+= '/monita - NE down RTPO Tembilahan'+ "\n"
        pesan+= '/mon [walisite] - NE down Walisite'+ "\n"
        pesan+= '/rev [siteid] - Revenue Site ID Based'+ "\n"
        pesan+= '/scriptbb [nename] [subnetwork] [ipoam] [ossmodel] - Create Script Migrasi OAM ENM BB' + '\n' + '<strong>Contoh : /scriptbb N-TAK050MM1-SUNGAI-KUNING LTE_Pekanbaru 10.146.244.173 20.Q1-R83A03</strong>'+ "\n\n"
        pesan+= '/scriptduw [nename] [rncname] [ipoam] [ossmodel] - Create Script Migrasi OAM ENM DUW' + '\n' + '<strong>Contoh : /scriptduw E_TAK050W_Sungai_Kuning RNTAK02 10.142.9.129 18.Q4-U.4.1010</strong>'+ "\n"
        #pesan_all_encode = urllib.quote(pesan.encode('utf-8'))
        requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,pesan), proxies=urllib.getproxies())
        break
  
  elif 'monita' in number:
        class color:
            BOLD = ''
            END = ''
        
        querya = "http://10.35.105.112/MONITA/AREA01/c_frame/get_current_list_alarm_a1?_dc=1580826954406&action=All-All-All-All&filter%5B0%5D%5Bfield%5D=technical_area_name&filter%5B0%5D%5Bdata%5D%5Btype%5D=string&filter%5B0%5D%5Bdata%5D%5Bvalue%5D=tembilahan&page=1&start=0&limit=2000"
        reqd = requests.get(querya).text
        repl = re.sub("(success+|data+|jml+):", r'"\1":',reqd)
        jsond = json.loads(repl)
        #print(jsond['data'][0]['class_name'])
        jmlalr=jsond['jml']
        alrdata=jsond['data']
        pesan = "Hello <strong>%s</strong> :)" %first_name + "\n" + "Berikut Alarm MONITA Tembilahan" + "\n\n"
        
        pesan+=("Total Alarm : %s" %jmlalr)
        pesan+=("\n" + color.BOLD + "DIAMOND" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'DIAMOND' :
                diamond = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + " \n " + alrdata[i]['freetext'] 
                i + 1
                pesan+=("\n" + diamond + "\n")
        text_plat = ("\n" +color.BOLD + "PLATINUM" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'PLATINUM' :
                platinum = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + " \n " + alrdata[i]['freetext']
                i + 1
                text_plat+=("\n" + platinum + "\n")
                
        text_gold = ("\n" + color.BOLD + "GOLD" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'GOLD' :
                gold = alrdata[i]['bts_id'] +  " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + " \n " + alrdata[i]['freetext'] 
                i + 1
                text_gold+=("\n" + gold + "\n")
                
        text_silver = ("\n" + color.BOLD + "SILVER" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'SILVER' :
                silver = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    " + alrdata[i]['wali_name'] + " \n " + alrdata[i]['freetext'] 
                text_silver+=("\n" + silver + "\n")
                
        text_bronze =("\n" + color.BOLD + "BRONZE" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'BRONZE' :
                bronze = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + " \n " + alrdata[i]['freetext']
                text_bronze+=("\n" + bronze + "\n")    
                
  elif 'mon' in number:
        class color:
            BOLD = ''
            END = ''
        cari = (number.split())[1]
        querya = "http://10.35.105.112/MONITA/AREA01/c_frame/get_current_list_alarm_a1?_dc=1594094740563&action=All-All-All-All&filter%5B0%5D%5Bfield%5D=wali_name&filter%5B0%5D%5Bdata%5D%5Btype%5D=string&filter%5B0%5D%5Bdata%5D%5Bvalue%5D=" + cari + "&page=1&start=0&limit=2000"
        reqd = requests.get(querya).text
        repl = re.sub("(success+|data+|jml+):", r'"\1":',reqd)
        jsond = json.loads(repl)
        #print(jsond['data'][0]['class_name'])
        jmlalr=jsond['jml']
        alrdata=jsond['data']
        pesan = "Hello <strong>%s</strong> :)" %first_name + "\n" + "Berikut Alarm MONITA %s" %cari + "\n\n"       

        pesan+=("Total Alarm : %s" %jmlalr)
        pesan+=("\n" + color.BOLD + "DIAMOND" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'DIAMOND' :
                diamond = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + "\n" + alrdata[i]['freetext'] 
                i + 1
                pesan+=("\n" + diamond + "\n")
        text_plat = ("\n" +color.BOLD + "PLATINUM" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'PLATINUM' :
                platinum = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + "\n" + alrdata[i]['freetext']
                i + 1
                text_plat+=("\n" + platinum + "\n")
                
        text_gold = ("\n" + color.BOLD + "GOLD" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'GOLD' :
                gold = alrdata[i]['bts_id'] +  " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + "\n" + alrdata[i]['freetext'] 
                i + 1
                text_gold+=("\n" + gold + "\n")
                
        text_silver = ("\n" + color.BOLD + "SILVER" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'SILVER' :
                silver = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    " + alrdata[i]['wali_name'] + "\n" + alrdata[i]['freetext'] 
                text_silver+=("\n" + silver + "\n")
                
        text_bronze =("\n" + color.BOLD + "BRONZE" +color.END + "\n")
        for i in range(len(alrdata)):
            if (alrdata[i]['class_name']) == 'BRONZE' :
                bronze = alrdata[i]['bts_id'] + " \t| " + alrdata[i]['band_name'] + " | " + alrdata[i]['aging'] + " |    "+ alrdata[i]['wali_name'] + "\n" + alrdata[i]['freetext']
                text_bronze+=("\n" + bronze + "\n")  

  elif "rev" in number: 
    if str(chat_id) in str(user):
        import pandas as pd
        import matplotlib.pyplot as plt
        plt.switch_backend('Agg')
        cari = (number.split())[1]
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + "Berikut Revenue Site %s" %cari + "\n\n" 
                
        sample_data = pd.read_csv('revenue_monthly_tembilahan_2019.csv')
        
        siteid = sample_data[sample_data.site == cari]
        plt.plot(siteid.month, siteid.rev_total / 10**6,'-o', label = "Revenue")
        plt.hlines(60, 12, 1, label= 'Under 60', color = 'red')
        plt.hlines(siteid.rev_total.mean() / 10**6, 12, 1, label= "Average", color = 'forestgreen')
        plt.legend(loc='best')
        plt.title("Revenue Site " + cari)
        plt.xlabel("Month (2019)")
        plt.ylabel("Revenue (Mio)")
        plt.savefig("revenue.png")    
        
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/revenue.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()  
  
    else:
         pesan = ('Not Registered, Please Contact Dwiki Kurnia (08118383795)')    
                   
  elif "scriptbb" in number:
        #data = pd.read_excel('NEname Sumbagteng.xlsx')
        ipoam = (number.split())[3]
        nename = (number.split())[1]
        subnetwork = (number.split())[2]
        ossmodel = (number.split())[4]
        #siteid = (data[data.site == nename2][data.rat == '3G'])
        #nename = siteid.sitename
        
        pesan = ('Berikut script migrasi OAM ENM Baseband | Running secara bergantian per baris :)') + '\n\n' + ('<strong>Script Create</strong>' + '\n') + ('cmedit create NetworkElement=' + nename + ' networkElementId=' + nename + ', neType="RadioNode", ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork=' + subnetwork + ',MeContext=' + nename + '", ossModelIdentity=' + ossmodel + '\n\n') + ('cmedit set NetworkElement=' + nename + ' controllingRnc="NetworkElement=null"' + '\n\n') + ('cmedit create NetworkElement=' + nename +',ComConnectivityInformation=1 ComConnectivityInformationId=1, ipAddress="' + ipoam + '", port=6513, transportProtocol=TLS -ns=COM_MED -v=1.1.0' + '\n\n') + ('secadm credentials create --secureusername rbs --secureuserpassword "rbs" -n ' + nename + '\n\n') + ('cmedit set NetworkElement=' + nename +',CmNodeHeartbeatSupervision=1 active=true' + '\n\n') + ('cmedit set NetworkElement=' + nename +',InventorySupervision=1 active=true' + '\n\n') + ('cmedit set NetworkElement=' + nename +',PmFunction=1 pmEnabled=true' + '\n\n') + ('cmedit set ' + nename +' networkElement timezone=Asia/Jakarta' + '\n\n') + ('alarm enable ' + nename +'' + '\n') + '\n\n' + ('<strong>Script Delete</strong>' + '\n') + ('alarm disable ' + nename + '\n\n') + ('cmedit set NetworkElement=' + nename + ',CmNodeHeartbeatSupervision=1 active=false'+ '\n\n') + ('cmedit set NetworkElement=' + nename + ',InventorySupervision=1 active=false' + '\n\n') + ('cmedit set NetworkElement=' + nename + ',FmAlarmSupervision=1 active=false'+ '\n\n') + ('cmedit set NetworkElement=' + nename + ',PmFunction=1 pmEnabled=false' + '\n\n') + ('cmedit action NetworkElement=' + nename + ',CmFunction=1 deleteNrmDataFromEnm' + '\n\n') + ('cmedit delete NetworkElement=' + nename + ' -ALL --force' + '\n\n') + ('cmedit delete NetworkElement=' + nename + ' -all' + '\n')  
       
  elif "scriptduw" in number:
        ipoam = (number.split())[3]
        nename = (number.split())[1]
        subnetwork = (number.split())[2]
        ossmodel = (number.split())[4]
        
        pesan = ('Berikut script migrasi OAM ENM DUW | Running secara bergantian per baris :)') + '\n\n' + ('<strong>Script Create</strong>' + '\n') + ('cmedit create NetworkElement=' + nename + ' networkElementId=' + nename + ', neType="RBS", ossPrefix="SubNetwork=ONRM_ROOT_MO,SubNetwork=' + subnetwork + ',MeContext=' + nename + '", ossModelIdentity=' + ossmodel + '\n\n') + ('cmedit set NetworkElement=' + nename + ' controllingRnc="NetworkElement=' + subnetwork + '"' + '\n\n') + ('cmedit create NetworkElement=' + nename +',CppConnectivityInformation=1 CppConnectivityInformationId=1, ipAddress="' + ipoam + '", port=80 -ns=CPP_MED -v=1.0.0' + '\n\n') + ('secadm credentials create --secureusername rbs --secureuserpassword "rbs" -n ' + nename + '\n\n') + ('cmedit set NetworkElement=' + nename +',CmNodeHeartbeatSupervision=1 active=true' + '\n\n') + ('cmedit set NetworkElement=' + nename +',InventorySupervision=1 active=true' + '\n\n') + ('cmedit set NetworkElement=' + nename +',PmFunction=1 pmEnabled=true' + '\n\n') + ('cmedit set ' + nename +' networkElement timezone=Asia/Jakarta' + '\n\n') + ('alarm enable ' + nename +'' + '\n') + '\n\n' + ('<strong>Script Delete</strong>' + '\n') + ('alarm disable ' + nename + '\n\n') + ('cmedit set NetworkElement=' + nename + ',CmNodeHeartbeatSupervision=1 active=false'+ '\n\n') + ('cmedit set NetworkElement=' + nename + ',InventorySupervision=1 active=false' + '\n\n') + ('cmedit set NetworkElement=' + nename + ',FmAlarmSupervision=1 active=false'+ '\n\n') + ('cmedit set NetworkElement=' + nename + ',PmFunction=1 pmEnabled=false' + '\n\n') + ('cmedit action NetworkElement=' + nename + ',CmFunction=1 deleteNrmDataFromEnm' + '\n\n') + ('cmedit delete NetworkElement=' + nename + ' -ALL --force' + '\n\n') + ('cmedit delete NetworkElement=' + nename + ' -all' + '\n')       

  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,pesan), proxies=urllib.getproxies())	
  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=65111950&text=%s&parse_mode=HTML' %(bot,pesan), proxies=urllib.getproxies())	
  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,text_plat), proxies=urllib.getproxies())	
  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,text_gold), proxies=urllib.getproxies())
  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,text_silver), proxies=urllib.getproxies())	
  requests.get('https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=HTML' %(bot,chat_id,text_bronze), proxies=urllib.getproxies())			

