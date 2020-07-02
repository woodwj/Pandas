import pandas as pd

def sortGroupCountBy(df, cols, Pr = False):
    groupCounts = df.groupby(cols)['Name'].count()
    if Pr:
        print("\n")
        print("##########################")
        print(groupCounts)
        print("##########################")
        print("\n")
    else:   return(groupCounts)

def sortGroupBy(df, cols, Pr = False):
    group = df.sort_values(cols, ascending=True)
    if Pr:
        print("\n")
        print("##########################")
        print(group)
        print("##########################")
        print("\n")
    else:   return(group)


trainPassangers = pd.read_csv("train.csv")
# Display all male passengers grouped by Class
sortGroupBy(trainPassangers[trainPassangers["Sex"]=="male"], "Pclass", True)
# Display all passengers by grouped by Class and Sex
sortGroupBy(trainPassangers, ["Pclass","Sex"], True)
# Display all male passengers group by Embarked
sortGroupBy(trainPassangers[trainPassangers["Sex"]=="male"], "Embarked", True)

