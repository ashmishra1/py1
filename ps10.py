import pandas as pd 
df = pd.read_csv("diamonds.csv")
print(len(df.index))
#print(df.isnull().sum().sum())
df.dropna()
#print(len(df.index))