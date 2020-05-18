import pandas as pd 
df = pd.read_csv("diamonds.csv")
print(df.groupby('cut').price.agg(['count','min','max']))