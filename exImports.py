import pandas as pd

shipPassangers = pd.read_csv("test.csv")

print(shipPassangers.head(6))
print(shipPassangers.tail(4))