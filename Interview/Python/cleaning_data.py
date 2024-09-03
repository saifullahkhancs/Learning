import pandas as pd
# Data cleaning means fixing bad data in your data set.

# Bad data could be:

# Empty cells
# Data in wrong format
# Wrong data
# Duplicates

#   **** Empty Cells *****
# Empty cells can potentially give you a wrong result when you analyze data.

#    &&&&&  Remove Rows &&&&&
# One way to deal with empty cells is to remove rows that contain empty cells.

df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df.to_string()) # drop the values which are containg a NaN

#   000000   imp imp imp imp 00000

# If you want to change the original DataFrame, use the inplace = True argument:
#df.dropna(inplace=True)
#print(df.to_string())

# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.
# This way you do not have to delete entire rows just because of some empty cells.
# The fillna() method allows us to replace empty cells with a value:

#df["Calories"].fillna(130, inplace = True)

fill_null_value = df["Calories"].fillna(130)

# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
# Pandas uses the mean() median() and mode()

# mean :- average
# median :- medium/ middle num 
# mode :- most occcuring data/ num
# range:- maximum num - minimum num

x = df["Calories"].mean()

replace_with_mean = df["Calories"].fillna(x)
print(replace_with_mean)


#   ************** Data of Wrong Format ***************
# Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

# To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

# converting the data into the correct form

# it will only convert it into the correct form doesnot fill the empty value

# df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# print(df.to_string())

# Remove rows with a NULL value in the "Date" column:

# df.dropna(subset=['Date'], inplace = True) # used only to remove null rows with respect to specific
                                            # column

#    ********** Wrong Data ****************
# "Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong,
# like if someone registered "199" instead of "1.99".

df = pd.read_csv('data.csv')
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

for y in df.index:
    if df.loc[y,"Pulse"] > 110:
        df.loc[y,"Pulse"] = 110


# To discover duplicates, we can use the duplicated() method.

# The duplicated() method returns a Boolean values for each row:

# ExampleGet your own Python Server
# Returns True for every row that is a duplicate, otherwise False:

print(df.duplicated().to_string())


df.drop_duplicates(inplace = True)
# Remember: The (inplace = True) will make sure that the method 
# does NOT return a new DataFrame, but it will remove all duplicates 
# from the original DataFrame.


# Finding Relationships
# A great aspect of the Pandas module is the corr() method.

# The corr() method calculates the relationship between each column in your data set.

print(df.corr())