
import os 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir('E:\mynotes\datascience')#changing the directory

data=pd.read_csv('Toyota.csv')#reading the toyota.csv file using pandas
data=pd.read_csv('Toyota.csv',index_col=0 )#assinging the  0 colum as the index colum
data=pd.read_csv('Toyota.csv',index_col=0 )#assinging the  0 colum as the index colum


data=pd.read_csv('Toyota.csv',index_col=0,na_values=['??','????']


#data.dropna(axis=0,inplace=True)


plt.scatter(data['Age'],data['Price'],c='blue')
plt.title('scatter plot of price vs age of cars')
plt.xlabel('Age(months)')
plt.xlabel('price(euros)')
plt.show()