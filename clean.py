import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["distance"]
del df["star_name"]
del df["mass"]
del df["radius"]
print(df.shape)

df = df[df["Star_name"].notna()]
df = df[df["Distance"].notna()]
df = df[df["Mass"].notna()]
df = df[df["Radius"].notna()]

df.to_csv("main.csv")
