import pandas as pd

def colsLower(df):
    cols = list(df.columns)
    correct = [x.lower() for x in cols]
    replace = {}
    for index in range(0,len(correct)):
        replace[cols[index]] = (correct[index])
    shipPassangers.rename(columns = replace, inplace = True)

shipPassangers = pd.read_csv("test.csv")

print(shipPassangers.columns)
colsLower(shipPassangers)
print(shipPassangers.columns)

