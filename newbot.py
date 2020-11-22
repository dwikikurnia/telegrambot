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
  print ("\n")
  try:
    update_id = x['update_id']
  except KeyError:
    print ('No Update')
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
        
  elif 'getid' in number:
        pesan = 'Hello <strong>%s</strong> :)' %first_name + "\n" + 'Your ID = ' + str(chat_id)
                    
  elif 'help' in number:
        pesan = 'Hello %s :)' %first_name + "\n"
        pesan+= '/getid - Get Your Telegram ID' + "\n"
        #pesan+= '/create [siteid] - Create tiket ANT TOTI'+ "\n"
        #pesan+= '/close [siteid] - Close tiket ANT TOTI'+ "\n"
        #pesan+= '/ssopen - Screenshot tiket Open ANT TOTI'+ "\n"
        #pesan+= '/scdfmc [siteid] - Create tiket SCD FMC BAST'+ "\n"
        #pesan+= '/ssranpag - Screenshot CACTI Router RAN PAG'+ "\n"
        #pesan+= '/ssridar - Screenshot CACTI Arnet Telkom Ridar'+ "\n"
        #pesan+= '/ssrikep - Screenshot CACTI Arnet Telkom Rikep'+ "\n"
        #pesan+= '/sssumbar - Screenshot CACTI Arnet Telkom Sumbar'+ "\n"
        #pesan+= '/sstn [siteid] - Screenshot CACTI Minilink TN'+ "\n"
        #pesan+= '/sstelkom [siteid] - Screenshot CACTI Metro / GPON Telkom'+ "\n"
        #pesan+= '/ssenm - Screenshot EAS Aktif ENM7 Dwiki'+ "\n"
        pesan+= '/monita - NE down RTPO Tembilahan'+ "\n"
        pesan+= '/mon [walisite] - NE down Walisite'+ "\n"
        pesan+= '/prod [siteid] - Revenue Site ID Based'+ "\n"
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

  elif "prod" in number: 
    if str(chat_id) in str(user):
        import pandas as pd
        import matplotlib.pyplot as plt
        import re
        import requests
        import json
        from pandas.io.json import json_normalize
        cari = (number.split())[1]
        pesan = "Hello <strong>%s</strong> :)" %first_name + "\n" + "Berikut Productivity Site %s" %cari + "\n\n" 
        queryb = "http://10.35.105.77/AGATAarea01/api/get_revenue_npa?_dc=1603524758517&site_id=" + cari + "&m=revenuesitedaily&page=1&start=0&limit=25"
        response = requests.get(queryb).text
        repl = re.sub("(success+|data+|jml+):", r'"\1":',response)
        jsond = json.loads(repl)
        alrdata = jsond['data']
        jmlalr = jsond['jml']

		#Define Payload & Traffic
        url2 = "http://10.35.105.77/AGATAarea01/api/get_traffic_payload_npa?_dc=1603536899911&site_id=" + cari + "&m=trafficsitedaily&page=1&start=0&limit=25"
        response2 = requests.get(url2).text
        repl2 = re.sub("(success+|data+|jml+):", r'"\1":',response2)
        jsond2 = json.loads(repl2)
        alrdata2 = jsond2['data']
        jmlalr2 = jsond2['jml']

		#Normalisasi format JSON to format Table
        val = json_normalize(alrdata)
        val2 = json_normalize(alrdata2)

		#Vlookup revenue, payload, traffic
        inner_join = pd.merge(val, val2, on ='tanggal', how ='inner')

		#convert string to float column 'total'
        total = inner_join['total']
        traffic = inner_join['traffic']
        payload = inner_join['payload']
        for i in range(len(total)): 
            total[i] = float(total[i]) 
            traffic[i] = float(traffic[i]) 
            payload[i] = float(payload[i])
		  
		#convert y label to Milions
        total = total / 1000000

		#Define Axis
        fig,ax = plt.subplots()
        ax2 = ax.twinx()

		#Create plot
        p1 = ax.plot(inner_join['tanggal'], total, color='red', marker='o', label='Revenue (Mio)')
        p2 = ax2.plot(inner_join['tanggal'], payload, color="darkgreen", marker='o', label='Payload (GB)')
        p3 = ax2.plot(inner_join['tanggal'], traffic, color="blue", marker='o', label ='Traffic (Erl)')

		#Create horizontal lines
		# ax.hlines(2, len(total), 0, label= 'Bronze (U60)', color = 'black', linestyle='--')
		# ax.hlines(3.33, len(total), 0, label= 'Silver (U100)', color = 'gray', linestyle='--')
		# ax.hlines(6.66, len(total), 0, label= 'Gold (U200)', color = 'gold', linestyle='--')
		# ax.hlines(13.33, len(total), 0, label= 'Platinum (U400)', color = 'cyan', linestyle='--')

		#Setting parameter plot
        ax.tick_params(axis='y', labelcolor='red')
        ax2.tick_params(axis='y', labelcolor='darkgreen')
        ax.set_ylabel('Revenue (Mio)', color='red')
        ax2.set_ylabel('Payload (GB) | Traffic (Erl)', color='darkgreen')

        ax.set_xticks(inner_join['tanggal'])
        ax.set_xticklabels(inner_join['tanggal'], rotation=90)
        ax2.set_xticks(inner_join['tanggal'])
        ax2.set_xticklabels(inner_join['tanggal'], rotation=90)

		#Combine legend plot
        lns = p1+p2+p3
        labs = [l.get_label() for l in lns]
        ax.legend(lns, labs, frameon=True, loc='best')

		#Save figure plot
        plt.title('Daily Productivity Site %s' %cari)
        plt.savefig("revenuesite.png", bbox_inches='tight', transparent=True)    
        
        send = os.popen ("curl -F chat_id='%s' -F photo=@'/home/dwiki/revenuesite.png' https://api.telegram.org/bot%s/sendPhoto" % (chat_id,bot)).readlines()  
  
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

