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
null=data.isna().sum()
#print(null)
missing=data[data2.isnull().any(axis=1)]
#print(missing)
#print(data2.describe())
mean=data['Age'].mean()
print(mean)