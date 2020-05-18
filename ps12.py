import pandas as pd 
df = pd.read_csv("diamonds.csv")
result = df.sample(frac=0.75, random_state=99)
print(result)
print(df.loc[~df.index.isin(result.index), :])