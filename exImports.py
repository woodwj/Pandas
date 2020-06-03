import pandas as pd

shipPassangers = pd.read_csv("test.csv")

print(shipPassangers.head())
print(shipPassangers.tail())
print(shipPassangers.head(8))
print(shipPassangers.tail(6))