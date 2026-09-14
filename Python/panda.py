
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


# ==============================================================================
# DEFINITIONS: pandas DataFrame Creation
# ==============================================================================
#
# A pandas DataFrame is a 2-dimensional labeled data structure with columns 
# of potentially different types (similar to a spreadsheet or SQL table).
#
# 1. CREATING FROM A DICTIONARY:
#    - Dictionary of Lists (Column-Oriented): Keys become column names, and 
#      list values become column rows.
#    - List of Dictionaries (Row-Oriented): Each dictionary represents a single 
#      row where keys are column names.
#
# 2. CREATING FROM A LIST:
#    - 1D List: Produces a single-column DataFrame.
#    - 2D List (List of Lists): Produces rows and columns. Column names can 
#      be provided explicitly via the `columns` argument.
# ==============================================================================

import pandas as pd


# ------------------------------------------------------------------------------
# 1. DATAFRAME FROM DICTIONARIES
# ------------------------------------------------------------------------------
def create_from_dict():
    print("=== 1. DATAFRAME FROM DICTIONARY ===")

    # A. Dictionary of Lists (Column-Oriented)
    dict_column_wise = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "London", "Tokyo"]
    }
    df_col = pd.DataFrame(dict_column_wise)
    print("--- From Dict of Lists (Column-Oriented) ---")
    print(df_col)

    # B. List of Dictionaries (Row-Oriented)
    list_of_dicts = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "London"},
        {"Name": "Charlie", "Age": 35, "City": "Tokyo"}
    ]
    df_row = pd.DataFrame(list_of_dicts)
    print("\n--- From List of Dicts (Row-Oriented) ---")
    print(df_row)


# ------------------------------------------------------------------------------
# 2. DATAFRAME FROM LISTS
# ------------------------------------------------------------------------------
def create_from_list():
    print("\n=== 2. DATAFRAME FROM LIST ===")

    # A. 1D List (Single Column)
    single_list = ["Python", "Java", "C++", "JavaScript"]
    df_1d = pd.DataFrame(single_list, columns=["Language"])
    print("--- From 1D List ---")
    print(df_1d)

    # B. 2D List (List of Lists - Rows and Columns)
    data_2d = [
        ["Alice", 25, "New York"],
        ["Bob", 30, "London"],
        ["Charlie", 35, "Tokyo"]
    ]
    df_2d = pd.DataFrame(data_2d, columns=["Name", "Age", "City"])
    print("\n--- From 2D List (List of Lists) ---")
    print(df_2d)


# ==============================================================================
# EXECUTION
# ==============================================================================
if __name__ == "__main__":
    create_from_dict()
    create_from_list()