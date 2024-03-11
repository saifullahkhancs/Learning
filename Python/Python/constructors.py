# Default Constructor 
class Person:
    def __init__(self):
        self.name = "John Doe"
        self.age = 0

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object and invoking the default constructor
person = Person()
person.display_info() 





# parmetrize constructor....................

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object and invoking the constructor
person = Person("Alice", 25)
person.display_info()  



# constructor method ...................................

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2023
        age = current_year - birth_year
        return cls(name, age)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object using the class method as a constructor
person = Person.from_birth_year("Alice", 1998)
person.display_info()   # Output: Name: Alice, Age: 25





# factory methood ......................
# different from comstructor is that it is a static method isnide
# a class which intilize a obeject from the class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def create_person(name, age):
        # Additional setup or validation can be performed here
        return Person(name, age)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object using the factory method
person = Person.create_person("Alice", 25)
person.display_info()   # Output: Name: Alice, Age: 25

#copy constructor
import copy

class Vech:
    def __init__(self,name, speed):
        self.name= name
        self.speed = speed
    
    def disinfo(self):
        print("the",self.name,"has this speed",self.speed)

    def __copy__(self):
        cls = self.__class__
        new_obj = cls.__new__(cls)
        new_obj.name = self.name
        new_obj.speed = self.speed
        return new_obj
       

vech1 = Vech("bike" , 34)
vech1.disinfo()
vech2 = copy.copy(vech1)
vech2.disinfo() 

