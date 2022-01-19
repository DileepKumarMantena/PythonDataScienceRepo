
import os 
import pandas as pd
import numpy as np

os.chdir('E:\mynotes\datascience')
data_csv=pd.read_csv('Iris_data_sample.csv')
cars_data=pd.read_csv('Toyota.csv')
cars_data=pd.read_csv('Toyota.csv',index_col=0 )
cars_data1=pd.read_csv('Toyota.csv',index_col=0 )
print(cars_data.insert(10,"Price_Class",""))

for i in range(0,len(cars_data["Price"]),1):
    if(cars_data['Price'][i]<=8450):
        print("low")
        cars_data['Price_Class'][i]="low"
    elif((cars_data['Price'][i]>11950)):
        print("High")
        cars_data['Price_Class'][i]="high"
    else:
        print("medium")
        cars_data['Price_Class'][i]="medium"

print("---------------------------------------------")
print(len(cars_data['Price']))
print("----------------------------------------------")
for i in cars_data["Price"]:
    print(i)
