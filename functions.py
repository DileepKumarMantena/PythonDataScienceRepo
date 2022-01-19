import os 
import pandas as pd
import numpy as np


os.chdir('E:\mynotes\datascience')
data_csv=pd.read_csv('Iris_data_sample.csv')
cars_data=pd.read_csv('Toyota.csv')
cars_data=pd.read_csv('Toyota.csv',index_col=0 )
cars_data1=pd.read_csv('Toyota.csv',index_col=0 )

print(cars_data.info())

a=(cars_data.loc[:,'Age'])
print("---------------------------------------")
#print(cars_data.head(a))
print(cars_data.head(5))
cars_data.insert(10,"Age_converted",0)
print(cars_data.info())
def convert(val):
    val_converted=val/12
    return val_converted
b=cars_data['Age_converted']=convert(cars_data['Age'])
print(b)
print(cars_data.loc[:,'Age_converted'])
print(cars_data.head(5))
print("______________________________________")
cars_data["Age_converted"]=round(cars_data["Age_converted"],1)
print(cars_data.loc[:,"Age_converted"])
print(cars_data.head(5))
cars_data.insert(11,'Km_per_month',0)
def convert(val1,val2):
    converted=val1/12
    ratio=val2/val1
    return[converted,ratio]
cars_data['Age_converted'],cars_data['Km_per_month']=(convert(cars_data["Age"],cars_data["KM"]))

print(cars_data.head(5))
    