# The four pillars of object oriented programing is 

# 1:- Abstraction
# 2:- Encapsulation 
# 3:- Inhertiance
# 4:- Polymorphism 

# Data Abstraction 
# it is the processof hiding unnecessary details of an object's internal stricture. 
# By abstracting the an objects data, its structure and behavior can be kept separate and more easily understood 

# Encapsulation 
# it is the process of wraping the data nad related function into a single unit
# Object .It limits the access to the object data and methods , preveneting 
# their misuse and ensuring their propar functioning.

# Inhertiance
# It is the ability to create a new class (child class) from an existing one(parent class).
# The child class typically inherits the attributes (members and methods) of the parent class
# and also it can redefined them,

# Polymorphism
# it is the abolity of an object to make multiple forms. This allows objects of different classes 
# to be used interchangeably, as long as they implement a certain interface (have methods of the same name)



# OverLoading                                                  
# 1:- Occurs within a single class.
# 2:- Involves multiles methods with the same name but different parameters.
# 3:- Decision is made at compile_time(static binding)
# 4:- The return type can be the same or different.
# 5:- No relationship required between the overloaded methods.
# 6:- Overloading allows methods with different functionalitity to have the same name.
# 7:- Method parameter vary in type , order or number.
# 8:- Method overloading can be archieved within the single class by changing the method signature.
# 9:- Overloading is a form of compile-time polymorphism.
# 10:- Overloaded methods can have different access modifiers


# Overriding                                                 
# 1:- Occurs betwenn a parent and child class.
# 2:- Involves a method in the child class with the same name and parameters as a method 
#     in the parent class.
# 3:- Decision is made at runtime(dynamic binding)
# 4:- The return type must be the same or subtype in the child class.
# 5:- Requires an inheritance relationship betwenn the parent and child classes.
# 6:- Overriding allows child classes to provide specific implementations for inherited methods.
# 7:- Method parameter must have the same type , order and number in both parent and child classes.
# 8:- Method overriding is achieved by using the @Override annotation in the child class.
# 9:- Overriding is a form of runtime polumorphism.
# 10:- Overriding methods must have the same or higher access modifier in the child class.