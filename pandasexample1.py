import os 
import pandas as pd
import numpy as np

os.chdir('E:\mynotes\datascience')#changing the directory
data_csv=pd.read_csv('Iris_data_sample.csv')#reading the iris data sample.csv using the pandas 
cars_data=pd.read_csv('Toyota.csv')#reading the toyota.csv file using pandas
cars_data=pd.read_csv('Toyota.csv',index_col=0 )#assinging the  0 colum as the index colum
cars_data1=pd.read_csv('Toyota.csv',index_col=0 )#assinging the  0 colum as the index colum
'''
print(cars_data1.index)#printing the cars-data  index values 
samp=cars_data#creating an copy of the cars_data dataframe using samp object(shallow copy)
print(samp)
print("--------------------------------------------")

print(cars_data.columns)#printing all the avaliable colums in the cars_data dataframe
print("---------------------------------------------")
print(cars_data.size)#printing the size of the dataframe
print("----------------------------------------------")
print(cars_data.shape)#printing the shape of the dataframe
print("----------------------------------------------")
print(cars_data.memory_usage)#prints the memory used by the dataframe
print("--------------------------------")
print(cars_data.ndim)# prints the number of dimensions in the dataframe
'''
print("-------------------------------")
print(cars_data.head(6))# prints the first six values of the dataframe
print("------------------------")
'''
print(cars_data.tail(5))# prints the last 5 values of the dataframe
print("----------------------------------")
print(cars_data.at[2,'MetColor'])#to print a single value at the given index of the column name given(at is used when we know the colum name)
print("--------------------------------------")
print(cars_data.iat[4,5])#to print a single value at the given index of the column name given(iat is used when we know the colum not name)
print("------------------------------------")
a=(cars_data.loc[:,'MetColor'])#prints out all the colum values of the given colum name in the dataframe
print("-----------------------------------------")
print(cars_data.tail(8))#oprints the last 8 values of the dataframe
print("-----------------------------------------")
print(cars_data.dtypes)#prints out the all the data types of the colum names in the dataframe
print("--------------------------------------")
print("---------------------------------------------")
#print(cars_data.get_dtype_counts())
print("------------------------------------------")
print(cars_data.select_dtypes(exclude=[object]))#prints out all the selected data types in the dataframe excluding the object datatype
print("---------------------------------------------")
print(cars_data.info('Price'))#prints out all the information about the given colum name in the dataframe
print("--------------------------------")
print(np.unique(cars_data['KM']))#prints out all the unique elets of the given coloum name in the dataframe
print("-----------------------------------")
#print(cars_data.columns('KM').dtypes)
print("-----------------------------------------------")
print(np.unique(cars_data['HP']))#prints out all the unique elets of the given coloum name in the dataframe
print("--------------------------------")
print(np.unique(cars_data['MetColor']))#prints out all the unique elets of the given coloum name in the dataframe
print("--------------------------------------")
print(np.unique(cars_data['Automatic']))#prints out all the unique elets of the given coloum name in the dataframe
print("------------------------------")
print(np.unique(cars_data['Doors']))#prints out all the unique elets of the given coloum name in the dataframe
'''