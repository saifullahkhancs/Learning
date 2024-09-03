# The four pillars of object oriented programing is 

# 1:- Abstraction
# 2:- Encapsulation 
# 3:- Inhertiance
# 4:- Polymorphism 

# Data Abstraction 
# it is the process of hiding unnecessary details of an object's internal structure. 
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
# 1:- Occurs between a parent and child class.
# 2:- Involves a method in the child class with the same name and parameters as a method 
#     in the parent class.
# 3:- Decision is made at runtime(dynamic binding)
# 4:- The return type must be the same or subtype in the child class.
# 5:- Requires an inheritance relationship between the parent and child classes.
# 6:- Overriding allows child classes to provide specific implementations for inherited methods.
# 7:- Method parameter must have the same type , order and number in both parent and child classes.
# 8:- Method overriding is achieved by using the @Override annotation in the child class.
# 9:- Overriding is a form of runtime polumorphism.
# 10:- Overriding methods must have the same or higher access modifier in the child class.


# Q:- What is the difference between the static and class methods?
# Ans:- A class method can access or modify the class state while a static method can't access or modify it. I
# n general, static methods know nothing about the class state. They are utility-type methods that take some parameters
#  and work upon those parameters. On the other hand class methods must have class as a parameter.


# Q1:- What is OOP?
# OOP is a programing language that uses objects to represent 
# the real_world entities . In python oops is implemented through classses 
# and objects . Classes are blueprint for creating object , and objects are
# the instances of the classes.


# Q2:- What is diamond problem?
# It is an ambiguity that rises when two classes C and B inherit from A
# and class D inherit from both the class B and C .
# If there is a method in A that B an C overridden and D doesnot override it
# then which version of the method does D inherit, That of B or that of C.

# Q3:- How to  solve the diamond problem?
# First of all the python does not have this problem as it contains 
# method resolution order(MRO) , 

# Method Resolution Order (MRO)
# When you inhert from the multiple classes , if their method name
# conflict , the first one named takes presedence. for example if we specified 
# or defined D(B,C). B method is called before the C.

# the __init__ method is often refered to as double undersore  intit 
#  or "" dunder intit"" for it has two underscores  on each side of its name.

# *********** dunder methods like  __init__ ,___new__  ****************

# these double underscore on both sides  of init imply that the method is 
# invoked and used internally in Python , without being required called explicitly


# There are mainly three types of Python __init__ constructors:

# Default __init__ constructor
        #    it does not accept any parameters, except for the self parameter
class Default():    
    def __init__(self):    #defining default constructor
        self.var1 = 56
        self.var2 = 27       
    def add(self):      
        print("Sum is ", self.var1 + self.var2)
obj = Default()     # since default constructor doesn’t take any argument
obj.add()



# Parameterised __init__ Constructor
        #    it accepts one or more than one argument other than the self 
class Default():
    def __init__(self, n1, n2):    #defining parameterised constructor
        self.var1 = n1
        self.var2 = n2
    def add(self):
        print("Sum is ", self.var1 + self.var2)
obj = Default(121, 136)              #Creating object for a class with parameterised init
obj.add()



# __init__ With Default Parameters
        #    it only accept the default parameter that is passed in the argument 

class Teacher:
    # definition for init method or constructor with default argument
    def __init__(self, name = "Preeti Srivastava"):
        self.name = name
    def show(self):
        print(self.name, " is the name of the teacher.")
        
t1 = Teacher()                             #name is initialised with the default value of the argument
t2 = Teacher('Chhavi Pathak')    #name is initialised with the passed value of the argument
t1.show()
t2.show()

# ******************* Class and instance variable **************

# Class variables are usefull for storing values that are constant across
# all instances of a class, while instance variable are usefull for storing 
# unique values for each object created from the class.

# a class variable is defined within a class and outside of any class method.

class Employee:
    office_name = "XYZ Private Limited"

    def __init__(self):
        print(Employee.office_name)

my_instance = Employee()

class Employee:
    office_name  = "XYZ Private Limited"

    def __init__(self , employee_name , employee_id):
        self.employee_name = employee_name
        self.employee_id = employee_id

    def show(self):
        print("Name:" , self.employee_name)
        print("ID:" , self.employee_id)
        print("Office name:" , Employee.office_name)

e1= Employee("saif" , "176")
e1.show()

Employee.office_name = "pqr privat limited"
# Class variables can be initialized 
# either inside the class definition or outside the class definition
e1.show()

