import pandas as pd
trainDF = pd.read_csv("train.csv")

# mean age
sumAges = trainDF["Age"].sum()
numBorded = trainDF["Age"].count()
meanPassangerAge = sumAges//numBorded
print("The average passanger age is "+ str(meanPassangerAge))
print("\n")

# mean age
sumAges = trainDF["Age"].sum()
numBorded = trainDF["Age"].count()
meanPassangerAge = sumAges//numBorded
print("The average passanger age is "+ str(meanPassangerAge))
print("\n")
