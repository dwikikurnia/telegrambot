import os
import requests
import re
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ast
from pandas.io.json import json_normalize

siteid = "RGT600"

url1 = ""
response = requests.get(url1).text
repl = re.sub("(success+|data+|jml+):", r'"\1":',response)
jsond = json.loads(repl)
alrdata = jsond['data']
jmlalr = jsond['jml']

url2 = ""
response2 = requests.get(url2).text
repl2 = re.sub("(success+|data+|jml+):", r'"\1":',response2)
jsond2 = json.loads(repl2)
alrdata2 = jsond2['data']
jmlalr2 = jsond2['jml']

val = pd.json_normalize(alrdata)
total = val['total']
for i in range(len(total)): 
    total[i] = float(total[i]) 

#Normalize JSON format to table format
val2 = pd.json_normalize(alrdata2)
print(val2)
traffic = val2['traffic']
payload = val2['payload']
for i in range(len(traffic)): 
    traffic[i] = float(traffic[i]) 
    payload[i] = float(payload[i])

total = total / 10000

plt.plot(val['tanggal'], total, color='red', marker='o', label='Revenue (Mio)')
plt.plot(val2['tanggal'], payload, color="darkgreen", marker='o', label='Payload (GB)')
plt.plot(val2['tanggal'], traffic, color="blue", marker='o', label ='Traffic (Erl)')
plt.xticks(rotation=90)
plt.ylabel("Traffic (Erl) / Payload (GB)")
plt.title("Daily Payload Site %s" %siteid)
plt.legend(loc='best')
plt.savefig("payloadsite.png", bbox_inches='tight', transparent=True)
plt.show()


