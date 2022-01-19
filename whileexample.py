import os 
import pandas as pd
import numpy as np


os.chdir('E:\mynotes\datascience')
data_csv=pd.read_csv('Iris_data_sample.csv')
cars_data=pd.read_csv('Toyota.csv')
cars_data=pd.read_csv('Toyota.csv',index_col=0 )
cars_data1=pd.read_csv('Toyota.csv',index_col=0 )

i=0
while i<len(cars_data['Price']):
    if(cars_data['Price'][i]<=8450):
        (cars_data["Price"][i])="low"
        
    elif(cars_data['Price'][i]>11950):
             (cars_data["Price"][i])="High"
    else:
        cars_data['Price'][i]="Medium"
    
      
    i=i+1


print("---------------------------------------------")
print(cars_data.loc[:,'Price'])
print("_________________________________________")
print(cars_data.head(5))