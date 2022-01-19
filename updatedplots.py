# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 11:24:52 2021

@author: Dileep Kumar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.chdir('E:\mynotes\datascience')
data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','?????'])
'''
print(data.head(4))
print("--------------------")
print(data.loc[1433:'KM'])
'''
#drawing an updated scatter plot
'''
data.dropna(axis=0, inplace=True)
sns.set(style="darkgrid")
sns.regplot(x=data['Age'],y=data["Price"],marker="*",fit_reg=False)
plt.show

#updated scatter plot of three components
sns.set(style="darkgrid")
sns.lmplot(x='Age',y='Price',data=data,fit_reg=False,hue='FuelType',legend=True,palette='Set1')
print(data['FuelType'])

#drawing an updated hiistgram

sns.displot(data["FuelType"],kde=False,bin=5)
plt.show()

#drawing an barplot
print(data["Age"])
sns.countplot(x='Age',data=data,hue="Automatic")
plt.show()

#dtrawing an box plot 
sns.boxplot(x=data["FuelType"],y=data["Age"],hue="Automatic",data=data)

#box-whisker plots
f,(ax_box,ax_hist)=plt.subplot(222,gridspec_kw={"height_ratios":(.15,.85)})
sns.boxplot(data["Price"],ax=ax_box)
sns.displot(data["Price"],ax=ax_hist,kde=False)
plt.show()
'''
#pairwise plots
data.dropna(axis=0, inplace=True)
sns.pairplot(data,kind='scatter',hue="FuelType")
plt.show()