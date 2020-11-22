import os
import requests
import re
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ast
from pandas.io.json import json_normalize

siteid = "BKG597"
url2 = ""
response2 = requests.get(url2).text
repl2 = re.sub("(success+|data+|jml+):", r'"\1":',response2)
jsond2 = json.loads(repl2)
alrdata2 = jsond2['data']
jmlalr2 = jsond2['jml']

#Define dataframe
df = pd.DataFrame(alrdata2)
df = df[df['TAHUN'] == '2020'] 
val2 = df.reset_index(drop=True)

#convert string traffic & payload to float
traffic = val2['traffic']
payload = val2['payload']
for i in range(len(traffic)): 
    traffic[i] = float(traffic[i]) 
    payload[i] = float(payload[i])
print(traffic)


plt.plot(val2['WEEK'], payload, color="darkgreen", marker='o', label='Payload (GB)')
plt.plot(val2['WEEK'], traffic, color="blue", marker='o', label ='Traffic (Erl)')
plt.xticks(rotation=90)
plt.ylabel("Traffic (Erl) / Payload (GB)")
plt.title("Daily Payload Site %s" %siteid)
plt.legend(loc='best')
plt.savefig("payloadsite.png", bbox_inches='tight', transparent=True)
plt.show()

