import pandas as pd


def duplicateOnTop(df):
    ret = df.append(df)
    return(ret)

def clearDuplicates(df):
    ret = df.drop_duplicates()
    return(ret)



shipPassangers = pd.read_csv("test.csv")
# styling
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)

# main
shipPassangers = duplicateOnTop(shipPassangers)
print(shipPassangers)
shipPassangers = clearDuplicates(shipPassangers)
print(shipPassangers)

