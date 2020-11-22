import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


title = "Bottom 10 Video Share Kecamatan"
savefile = "vidsharekec"
dataset = pd.read_csv("D:\Tutela\Report NS\Tbh 16 November 2020\%s.csv" %savefile)
df = dataset.pivot_table(values='measure0', index='dimension0', columns='dimensionColor', fill_value=0)
df['Total Device'] = df['3'] + df['Indosat Ooredoo'] + df['Smartfren'] + df['Telkomsel'] + df['XL']

#Add Column with Percentage
df['Telkomsel (%)'] = (df['Telkomsel'] / df['Total Device']) * 100
df['XL (%)'] = (df['XL'] / df['Total Device']) * 100
df['Indosat (%)'] = (df['Indosat Ooredoo'] / df['Total Device']) * 100
df['3 (%)'] = (df['3'] / df['Total Device']) * 100
df['Smartfren (%)'] = (df['Smartfren'] / df['Total Device']) * 100

#Delete integer values
del(df['Total Device'])
del(df['Indosat Ooredoo'])
del(df['Smartfren'])
del(df['Telkomsel'])
del(df['3'])
del(df['XL'])

#Sort Percentage Telkomsel
df_sort = df.sort_values(['Telkomsel (%)'])
dfbottom = df_sort[0:10]

#Create plot
dfbottom.plot(stacked=True, kind='barh', color=['red', 'blue', 'yellow', 'purple', 'orange'])
plt.title(title)
plt.legend(loc='best')
plt.ylabel('Kecamatan')
plt.xlabel('Share (%)')
plt.savefig("D:\Tutela\Report NS\Tbh 16 November 2020\%s.png" %savefile, bbox_inches='tight', transparent=True)
plt.show()

