import os 
import pandas as pd
import numpy as np

os.chdir('E:\mynotes\datascience')
data_csv=pd.read_csv('Iris_data_sample.csv')
cars_data=pd.read_csv('Toyota.csv')
cars_data=pd.read_csv('Toyota.csv',index_col=0 )
cars_data1=pd.read_csv('Toyota.csv',index_col=0 )
'''
print(cars_data1.index)

samp=cars_data
print(samp)
print("--------------------------------------------")

print(cars_data.columns)
print("---------------------------------------------")
print(cars_data.size)
print("----------------------------------------------")
print(cars_data.shape)
print("----------------------------------------------")
print(cars_data.memory_usage)
print("--------------------------------")
print(cars_data.ndim)
print("-------------------------------")
print(cars_data.head(6))
print("------------------------")
print(cars_data.tail(5))
print("----------------------------------")

print(cars_data.at[2,'MetColor'])
print("--------------------------------------")
print(cars_data.iat[4,5])
print("------------------------------------")
a=(cars_data.loc[:,'MetColor'])

print("-----------------------------------------")
print(cars_data.tail(8))
print("-----------------------------------------")
print(cars_data.dtypes)
print("--------------------------------------")
print("---------------------------------------------")
#print(cars_data.get_dtype_counts())
print("------------------------------------------")
print(cars_data.select_dtypes(exclude=[object]))
print("---------------------------------------------")
print(cars_data.info('Price'))   
print("--------------------------------")
print(np.unique(cars_data['KM']))
print("-----------------------------------")
#print(cars_data.columns('KM').dtypes)
print("-----------------------------------------------")
print(np.unique(cars_data['HP']))
print("--------------------------------")
print(np.unique(cars_data['MetColor']))
print("--------------------------------------")
print(np.unique(cars_data['Automatic']))
print("------------------------------")
print(np.unique(cars_data['Doors']))
print("----------------------------------------------")
cars_data=pd.read_csv('Toyota.csv',index_col    =0,na_values=["??","???"])
print("--------------------------------------------------------")
print(cars_data.info())
print("-------------------------------------------------")

a=cars_data['MetColor']=cars_data['MetColor'].astype('object')#to change the data type 
print(a)
print("----------------------------------------------------")
print(cars_data['FuelType'].nbytes)#to know how many bytes consumed by the coloum 
print("-------------------------------------------")
print(cars_data['FuelType'].astype('category').nbytes)#to print the that the fueltype and the category is of same type
print("--------------------------------------------")
print(cars_data.info())# to print all the datatypes  of the  dataframe
print("-------------------------------------------")
print(np.unique(cars_data['Doors']))# to print the unique values of the Doors
print("-------------------------------------------------------------")
print(cars_data['Doors'].replace('three',3,inplace=True))#to replace the coloum value 
print(cars_data['Doors'].replace('four',4,inplace=True))
print(cars_data['Doors'].replace('five',5,inplace=False))
print("_______________________________")
print(cars_data.info())
door = cars_data['Doors'].astype('int64').dtype
print(door)

print(cars_data.isnull().sum())#to print the count of no of missing values present in the each coloum
'''
print("----------------------------------------------------------")
print(cars_data.insert(10,"Price_Class",""))
