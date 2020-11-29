import pandas as pd
import requests
import re
import json

siteid = input("Masukkan Site ID : ")
siteid = siteid.upper()
urlnos = 'http://10.35.105.77/AGATAarea01/load_data_summary/only_site_panel_id_data_nos_network_profile_site?_dc=1606567409913&site_id=' + siteid + '&page=1&start=0&limit=20'
urlrto = 'http://10.35.105.77/AGATAarea01/load_data_summary/only_site_panel_id_data_rto_network_profile_site?_dc=1606567426164&site_id=' + siteid + '&page=1&start=0&limit=20'
response_nos = requests.get(urlnos).text
response_rto = requests.get(urlrto).text
repl_nos = re.sub("(success+|data+|jml+):", r'"\1":',response_nos)
repl_rto = re.sub("(success+|data+|jml+):", r'"\1":',response_rto)
jsond_nos = json.loads(repl_nos)
jsond_rto = json.loads(repl_rto)
alrdata_nos = jsond_nos['data']
alrdata_rto = jsond_rto['data']

dfnos = alrdata_nos[0]
dfrto = alrdata_rto[0]
print("Site ID \t\t: ", dfnos['site_id'])
print("Site Name \t\t: ", dfnos['site_name'].upper())
print("Class Name \t\t: ", dfnos['class_name'].upper())
print("Status Site \t: ", dfrto['utilities_name'].upper())
print("Band Technology : ", dfrto['band_conf'])
print("Wali Name \t\t: ", dfnos['wali_name'].upper())
print("RTPO Name \t\t: ", dfnos['technical_area_name'].upper())
print("NS Name \t\t: ", dfnos['departement_name'].upper())
print("Sub Branch Name : ", dfrto['sub_branch_name'].upper())
print("TP Name \t\t: ", dfnos['tower_provider_name'].upper())
print("Koordinat \t\t: ", dfrto['latitude'], ",", dfrto['longitude'])
print("Alamat \t\t\t: ", dfnos['alamat'])
