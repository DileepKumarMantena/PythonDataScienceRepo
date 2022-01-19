# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 22:52:48 2021

@author: Dileep Kumar
"""

import os 
import pandas as pd 

os.chdir('E:\mynotes\datascience')

data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????'])
data1=data.copy()
data2=data1.copy()
#null=data.isna().sum()
#print(null)
missing=data[data2.isnull().any(axis=1)]
#print(missing)
#print(data2.describe())
mean=data['Age'].mean()
#print(mean)
data2["Age"].fillna(data2["Age"].mean(),inplace=True)
median=data2["KM"].median()
#print(median)
data2["Age"].fillna(data2["Age"].median(),inplace=True)
meanhp=data2["HP"].mean()
#print('mean of hp is',meanhp)
data2["Age"].fillna(data2["HP"].mean(),inplace=True)
newnull=data.isnull().sum()
#print(newnull)
series=data['FuelType'].value_counts().index[0]
print(series)
print("---------------------------------")
series1=data["Age"].value_counts()
#print(series1.head(4))
#print("------------------------------")
#print(data["Age"])
#print(data['MetColor'].mode())
data2["MetColor"].fillna(data["MetColor"].mode()[0],inplace=True)
print(data.isnull().sum())