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
url2 = "http://10.35.105.77/AGATAarea01/api/get_traffic_payload_npa_monthly?_dc=1603633437427&site_id=" + siteid + "&m=trafficsitemonthly&page=1&start=0&limit=25"
response2 = requests.get(url2).text
repl2 = re.sub("(success+|data+|jml+):", r'"\1":',response2)
jsond2 = json.loads(repl2)
alrdata2 = jsond2['data']
jmlalr2 = jsond2['jml']

print(alrdata2)
#Normalize JSON format to table format
val2 = pd.DataFrame(alrdata2)
print(val2)
traffic = val2['traffic']
payload = val2['payload']
for i in range(len(traffic)): 
    traffic[i] = float(traffic[i]) 
    payload[i] = float(payload[i])

plt.plot(val2['tanggal'], payload, color="darkgreen", marker='o', label='Payload (GB)')
plt.plot(val2['tanggal'], traffic, color="blue", marker='o', label ='Traffic (Erl)')
plt.xticks(rotation=90)
plt.ylabel("Traffic (Erl) / Payload (GB)")
plt.title("Daily Payload Site %s" %siteid)
plt.legend(loc='best')
plt.savefig("payloadsite.png", bbox_inches='tight', transparent=True)
plt.show()


