import os
import pandas as pd

os.chdir('E:\mynotes\datascience')
data=pd.read_csv("Iris.csv",index_col=0,na_values=["??","?????"])

copy=data.copy()
table=pd.crosstab(index=data['SepalLengthCm'], columns='count',dropna=True)#prints the how many times does the value in that colum repeated
print(table)
                 