# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 16:18:38 2020

@author: hp
"""

import os
import requests
import re
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


url2 = "http://10.35.105.112/dev1/MONITA/AREA01/c_load_data_summary/wali_in_technical_area_current?_dc=1605518123239&technical_area=RTPO%20TEMBILAHAN&l1_id=all&class_input=all"
response2 = requests.get(url2).text
jsond2 = json.loads(response2)

df = pd.DataFrame(jsond2)

del(df['[C] Zuldihar Rahman'])
dwiki = df['[C] Dwiki Kurnia']
print(dwiki[1])
fajar = df['[C] Fajar Afriansyah']
yohanes = df['[C] Yohanes Marakub']
print(dwiki)

nodata = 'null'


while(nodata in dwiki): 
    dwiki.remove(nodata)

while(nodata in fajar):
    fajar.remove(nodata)
    
while nodata in yohanes:
    yohanes.remove(nodata)
    
    
dwiki1 = dwiki[0]
fajar1 = fajar[0]
yohanes1 = yohanes[0]

dwiki_series = pd.Series(dwiki1)
fajar_series = pd.Series(fajar1)
yohanes_series = pd.Series(yohanes1)

for i in range(len(dwiki_series)):
    dwiki1[i] = int(dwiki1[i])

for i in range(len(fajar_series)):
    fajar1[i] = int(fajar1[i])
    
for i in range(len(yohanes_series)):
    yohanes1[i] = int(yohanes1[i])


plt.plot(dwiki1, marker='o', label='Dwiki Kurnia')
plt.plot(fajar1, marker='o', label='Fajar Afriansyah')
plt.plot(yohanes1, marker='o', label='Yohanes Marakub')
plt.title('Total Alarm Monita Hourly')
plt.xlabel('Hour')
plt.ylabel('Total NE Alarm')
plt.legend(loc='best')