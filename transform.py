import pandas as pd 
import pyreadr as rda 

result = rda.read_r('rda-data/player_meta.rda')

print(result.keys())
df1 = result["player_meta"]
df1.to_csv("csv/coba.csv")
print(df1)
