from collections import namedtuple
#  operations on the name tuples
# 1:- creating the nametuple

# declaring the name tuple
Student = namedtuple('Student', ['name', 'age' , 'DOB'])

# Adding the values
S1 = Student(name='Ali-', age=18, DOB='1980-01-01')


#  2:- accessing the values
# By 3 differenet methods      1:- by index  2:- by keyname  3:- using getattr()

print(S1.name)
print(S1[2])
print(getattr(S1, 'age'))


# 3:- Convertions Operations

# Namedtuples provide a few useful conversion operations to work with other data types in Python. Below are the
# following conversion operations that is provided for namedtuples in Python:
#
# 1:- Using _make()     2:- Using _asdict()     3:- Using “**” (double star) operator


# Conversion Using _make()
# This function is used to return a namedtuple() from the iterable passed as argument. In this example, we are using
# _make() to convert the list “li” into namedtuple.


li = ['Zohaib'  , '23' , '11-12-2009']

S2 = Student._make(li)
print(S2)

# Conversion Operation Using _asdict()
# This function returns the OrderedDict() as constructed from the mapped values of namedtuple(). In this example, we are
# using _asdict() to convert the input list into namedtuple instance.


S3 =   S2._asdict()
print(S3)

# Using “**” (double star) operator
# This function is used to convert a dictionary into the namedtuple(). In this example, we are using “**” to convert the
# input list into namedtuple.

di = {'name' : "saif" , 'age': "25" , 'DOB': "04-07-2000"}
S4 = Student(**di)
print(S4)
print(S4.name)


# 4:- Additional Operations
# 1:- _fields   2:-_replace()   3:- __new__()   4:- __getnewargs__()


# _fields
# This data attribute is used to get all the keynames of the namespace declared. In this example, we are using _fields
# to get all the keynames of the namespace declared.

print(S4._fields)

# _replace()
# _replace() is like str.replace() but targets named fields( does not modify the original values). This just not modify
# the previous named tuple but create a new one

# ******************* imp note *******************************************
#    Named tuple is a tuple which is not mutable so when we replace instead of muting it creates another copy

S5 = S4._replace(name='Saifullah khan')

print(S5)

# __new__()
# This function returns a new instance of the Student class, by taking the values that we want to assign to the keys
# in the named tuple. In this example, we are using __new__() to return a new instance of the Student class.

S6 = Student.__new__(Student,'Himesh','19','26082003')
print(S6)

# __getnewargs__()
# This function returns the named tuple as a plain tuple.

print(S6.__getnewargs__())


# read further here


#  https://www.geeksforgeeks.org/namedtuple-in-python/