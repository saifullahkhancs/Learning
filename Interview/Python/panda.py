
import pandas as pd

pandas_seeries = pd.Series([1,2,3])
print(pandas_seeries)
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#      ******  Labels   ***********
# If nothing else is specified, the values are labeled with their index number. 
# First value has index 0, second value has index 1 etc.

myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
# The keys of the dictionary become the labels.

#                ******   DataFrames  *****
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array,
#  or a table with rows and columns.

data = {
    "calories": [20, 30 ,49],
    "day": [1,2,3]
}
df = pd.DataFrame(data)
print(df)

# Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
print(df.loc[[0, 1]])

# When using [], the result is a Pandas DataFrame.

# With the index argument, you can name your own indexes.

df_index = pd.DataFrame(data, index = ["day1" , "day2" , "day3" ])
print(df_index)
print(df_index)

# i started leraning git and this is a commit changes practice for the commit.