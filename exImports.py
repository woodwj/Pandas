import pandas as pd

def colsLowerCase(df):
    cols = list(df.columns)
    correct = [x.lower() for x in cols]
    replace = {}
    for index in range(0,len(correct)):
        replace[cols[index]] = (correct[index])
    shipPassangers.rename(columns = replace, inplace = True)        

def findFirstClass(df, Pr = False):
    condition = df[df['Pclass']==1]
    if Pr:
        print("\n#########################")
        print("First Class Passangers \n")
        print(condition.head())
    else:   return(condition)
    
def findSecondClass(df, Pr = False):
    condition = df[df['Pclass']==2]
    if Pr:
        print("\n#########################")
        print("Second Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def findThirdClass(df, Pr = False):
    condition = df[df['Pclass']==3]
    if Pr:
        print("\n#########################")
        print("Third Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def findMales(df, Pr = False):
    condition = df[df['Sex']=="male"]
    if Pr:
        print("\n#########################")
        print("Male Passangers \n")
        print(condition.head())
    else:   return(condition)

def findFemales(df, Pr = False):
    condition = df[df['Sex']=="female"]
    if Pr:
        print("\n#########################")
        print("First Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def findFemSecClass(df, Pr = False):
    females = findFemales(df)
    condition = findSecondClass(females)
    if Pr:
        print("\n#########################")
        print("First Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def findFirstOrThird(df, Pr = False):
    firsts = findFirstClass(df)
    thirds = findThirdClass(df)
    condition = pd.concat([firsts,thirds])
    if Pr:
        print("\n#########################")
        print("First or Third Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def findYoungThirdClass(df, Pr = False):
    thirds = findThirdClass(df)
    condition = thirds[thirds['Age'] < 25]
    if Pr:
        print("\n#########################")
        print("Young Third Class Passangers \n")
        print(condition.head())
    else:   return(condition)

def find910s(df, Pr = False):
    condition = df[(df['PassengerId'] >= 900)&(df['PassengerId'] <= 910)]
    if Pr:
        print("\n#########################")
        print("Passengers 900-910 \n")
        print(condition.head())
    else:   return(condition)

def findMothers(df, Pr = False):
    females = findFemales(df)
    highClassLadies = findFirstClass(females)
    condition = highClassLadies[highClassLadies['Age'] >= 45]
    if Pr:
        print("\n#########################")
        print("Mothers \n")
        print(condition.head())
    else:   return(condition)


shipPassangers = pd.read_csv("test.csv")
#
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Show all passengers in First Class
findFirstClass(shipPassangers, True)
# Show all passengers who are female and in Second Class
findFemSecClass(shipPassangers,True)
# Show all passengers who are in First Class and in Third Class
findFirstOrThird(shipPassangers, True)
# Show all passengers who are in Third Class under the age of 25
findYoungThirdClass(shipPassangers, True)
# Show all passangers with a Passanger ID between 900 and 910 inclusive
find910s(shipPassangers, True)
# Show all passengers in First Class - Female, 1st Class and over 45
findMothers(shipPassangers, True)



