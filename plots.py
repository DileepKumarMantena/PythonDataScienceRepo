# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:38:14 2021

@author: Dileep Kumar
"""

import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('E:\mynotes\datascience')#changing the directory
    



data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
print(data['KM'].head(5))
#drawing a scatter plot

data.dropna(axis=0,inplace=True)
plt.scatter(data['Age'], data['Price'], c='blue')
plt.title('scatter plot of price vs age of cars')
plt.xlabel('Age(months)')
plt.xlabel('price(euros)')
plt.show()

#drawing a histogram

plt.hist(data['KM'])
plt.hist(data['KM'],color='green',edgecolor='white',bins=5)
plt.title('histogram of title ')
plt.xlabel('kilometer')
plt.ylabel('frequency')
plt.show()

#drawing a barplot

counts=[979,170,12]
fueltype=('Petrol','Diesel','CNG')
index=np.arange(len(fueltype))
plt.bar(index,counts,color=['orange','white','green'])
plt.title('barplot of fuel items')
plt.xlabel('fueltype')
plt.ylabel('frequency')
plt.xticks(index,fueltype,rotation=90)
plt.show()