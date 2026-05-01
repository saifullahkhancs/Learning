import pandas as pd

# Load the CSV into a DataFrame:
df = pd.read_csv("data.csv")# A simple way to store big data sets is to use CSV files (comma separated files).
print(df.to_string()) # to show complete data
print(df) # to show only first 5 and last 5

print(df.head()) # print the above 5 lines
print(df.head(10)) # print the head and above 10 records
print(df.tail()) # print the last 5 rown

# The DataFrames object has a method called info(), that gives you more information about the data set.

print(df.info())


#         ***** Read JSON *****
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known 
# in the world of programming, including Pandas.

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 



# Empty values, or Null values, can be bad when analyzing data, 
# and you should consider removing rows with empty values. This is a 
# step towards what is called cleaning data,