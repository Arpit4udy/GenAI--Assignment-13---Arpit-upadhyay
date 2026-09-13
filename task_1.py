import pandas as pd

df=pd.read_csv('online food delivery dataset.csv')
print(df.shape)
print(df.columns)
print(df.head(5))