import pandas as pd

df= pd.read_csv("data/raw/sales.csv")

print(df.head())

print(df.shape)

print(df.columns)
print(df.dtypes)
df.info()
print(df.isnull().sum())
print(df.describe())