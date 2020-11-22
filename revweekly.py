import os
import requests
import re
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ast
from pandas.io.json import json_normalize


#Define Revenue
siteid = "RGT514"
siteid = siteid.upper()
url1 = ""
response = requests.get(url1).text
repl = re.sub("(success+|data+|jml+):", r'"\1":',response)
jsond = json.loads(repl)
alrdata = jsond['data']
jmlalr = jsond['jml']

#Define dataframe
df = pd.DataFrame(alrdata)
val1 = df.drop_duplicates(subset=['voice', 'total'])
val = val1.reset_index(drop=True)

#convert string total to float total
total = val['total']

for i in range(len(total)): 
    total[i] = float(total[i]) 
  
#convert y label to Milions
total = total / 1000000

#Define Axis
fig,ax = plt.subplots()

#Create plot
p1 = ax.plot(val['week'], total, color='red', marker='o', label='Revenue (Mio)')

#Create horizontal lines
ax.hlines(2*7, len(total), 0, label= 'Bronze (U60)', color = 'black', linestyle='--')
ax.hlines(3.33*7, len(total), 0, label= 'Silver (U100)', color = 'gray', linestyle='--')
ax.hlines(6.66*7, len(total), 0, label= 'Gold (U200)', color = 'gold', linestyle='--')
ax.hlines(13.33*7, len(total), 0, label= 'Platinum (U400)', color = 'cyan', linestyle='--')

ax.tick_params(axis='y', labelcolor='red')
ax.set_ylabel('Revenue (Mio)', color='red')

ax.set_xticks(val['week'])
ax.set_xticklabels(val['week'], rotation=90)
ax.legend(loc='best')

#Save figure plot
plt.title('Daily Productivity Site %s' %siteid)
plt.savefig("revenuesite.png", bbox_inches='tight', transparent=True)
plt.show()
