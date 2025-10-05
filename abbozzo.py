import pandas as pd

df = pd.read_csv("Viaggiatori stranieri - Spesa in Calabria.csv", encoding="latin1", sep=";")
df = df.iloc[:, 2]   
print(df)
lenght = len(df)
print(lenght)
print(df.describe())