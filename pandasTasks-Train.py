import pandas as pd

def sortGroupBy(df, cols, Pr = False):
    groupCounts = df.groupby(cols)['Name'].count()
    if Pr:
        print("\n")
        print("##########################")
        print(groupCounts)
        print("##########################")
        print("\n")
    else:   return(groupCounts)


trainPassangers = pd.read_csv("train.csv")
# Display number of passengers per Class
sortGroupBy(trainPassangers, "Pclass", True)
# Display number of passengers by Class and Sex
sortGroupBy(trainPassangers, ["Pclass", "Sex"], True)
# Display number of passengers by Class, Sex and Age
sortGroupBy(trainPassangers, ["Pclass", "Sex", "Age"], True)
# Display number of passengers in Class 1 by Sex and Age
sortGroupBy(trainPassangers[trainPassangers["Pclass"] == 1], ["Sex","Age"], True)
# Display bumber of all female passangers by Class
sortGroupBy(trainPassangers[trainPassangers["Sex"] == "female"], "Pclass",True)

