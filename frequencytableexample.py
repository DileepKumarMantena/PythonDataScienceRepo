import pandas as pd
#create data
df = pd.DataFrame({'Grade': ['A','A','A','B','B', 'B', 'B', 'C', 'D', 'D'],
                   'Age': [18, 18, 18, 19, 19, 20, 18, 18, 19, 19],
                   'Gender': ['M','M', 'F', 'F', 'F', 'M', 'M', 'F', 'M', 'F']})


#find frequency of each letter grade
count=pd.crosstab(index=df['Grade'], columns='count')

df.insert(3,"class","third")
count1=pd.crosstab(index=df['Grade'], columns=df['class'],dropna=True)
(count1)
(df.head(3))
count2=pd.crosstab(index=df['class'], columns=df['class'],dropna=True)
(count2)
(df.info())
(df)
count3=pd.crosstab(index=df['Grade'], columns=df['class'],dropna=True,normalize=True)

count4=pd.crosstab(index=df['Grade'], columns=df['class'],dropna=True,normalize=True,margins=True)
(count4)

count5=pd.crosstab(index=df['Age'], columns=df['class'],dropna=True,normalize='index',margins=True)
(count5)
print("--------------------------------------------------------------")
count6=pd.crosstab(index=df['Age'], columns=df["class"],dropna=True,normalize='columns',margins=True)
(count6)
plot=df.select_dtypes(exclude=[object])
(df.shape())
corr=plot.corr()
print(corr)