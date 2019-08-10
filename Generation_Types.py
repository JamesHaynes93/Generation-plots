# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 20:43:19 2019

@author: s1223546
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mix = pd.read_csv('ofgem_mix.csv')
print(mix)

mix.index = pd.date_range(start = "2006-01-01", end = "2018-12-31", freq = "Q")
quarters = pd.date_range(start = "2006-01-01", end = "2018-12-31", freq = "Q")
print(mix.keys())


y =[mix['Coal'],mix['Oil'],mix['Gas'],mix['Nuclear'], mix['Hydro'], mix['Wind and Solar'], mix['Biomass'], mix['Other fuels']]

fig, ax1 = plt.subplots(figsize=(15, 5))
ax1 = plt.stackplot(quarters,y,labels=['Coal','Oil','Gas','Nuclear','Hydro','Wind and Solar','Biomass','Other fuels'])
ax1 =plt.margins(0,0)
ax1 = plt.legend(bbox_to_anchor=(1.15, 0.5))

#ax1 = mix.plot.area(figsize=(23,5))



mix['Renewable'] =  mix['Hydro'] + mix['Wind and Solar'] + mix['Biomass']
mix['Non_Renewable'] = mix['Other fuels'] + mix['Nuclear'] + mix['Coal'] + mix['Gas'] + mix['Oil']
mix['Carbon Emitting'] = mix['Other fuels'] + mix['Coal'] + mix['Gas'] + mix['Oil']
mix['Non Carbon Emitting'] = mix['Hydro'] + mix['Wind and Solar'] + mix['Biomass'] + mix['Nuclear'] 

ren_vs_non_rev = [mix['Renewable'],mix['Non_Renewable']]
carb_vs_non_carb = [mix['Non Carbon Emitting'],mix['Carbon Emitting']]

fig, axs = plt.subplots(1, 2,figsize=(15,3))
fig

print(ren_vs_non_rev)

pal = sns.color_palette("Set1")

axs[0].stackplot(quarters,ren_vs_non_rev,labels= ["Renewable","Non Renewable"],colors=pal)
axs[0].legend()
axs[0].margins(0,0)



axs[1].stackplot(quarters,carb_vs_non_carb,labels=["Non Carbon Emitting", "Carbon Emitting"])
axs[1].margins(0,0)
plt.legend()