import os
import numpy as np
import pandas as pd
os.chdir('E:\mynotes\datascience')
data=pd.read_csv('Toyota.csv',index_col=0)
print(data)
plot=data.select_dtypes(exclude=[object])
(data.shape())
corr=plot.corr()
print(corr)