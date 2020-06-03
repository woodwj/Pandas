import pandas as pd
pd.set_option('max_colwidth',10)
pd.options.display.max_columns = 2
pd.options.display.max_rows = 6

indexi = ["Bob", "Karen", "James Bond", "Bleep", "Bloop", "Jesus Christ", "Gary", "Susan", "Harry", "Mom"]

drinks = {
    'Diet Coke' : [0,0,2,1,1,4,5,6,2,3],
    'Orange Juice' : [0,4,1,1,0,0,2,3,0,1]
}

orders = pd.DataFrame(drinks, index=indexi)

print(orders)