# Abstract classes are typically used when you want to define a common interface
# or behavior that multiple derived classes should adhere to, while leaving the
# implementation details to the derived classes. They act as a contract,  
# that certain methods or attributes are present in the derived classes.ensuring

# In Python, you can create an abstract class using the abc module,
#  which provides the ABC (Abstract Base Class) and abstractmethod
#  decorators.


# @ are called decorators

#  @abstractmethod
#  @staticmethod  as ko hi use kar ka ham factory constructor call karta hain method call kar sakta hain
#  @classmethod
#  

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def display(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def display(self):
        print(f"Circle with radius {self.radius}")

# Attempting to create an instance of the abstract class (Shape)
shape = Shape()  # Output: TypeError: Can't instantiate abstract class Shape with abstract methods calculate_area, display

# Creating an instance of the derived class (Circle)
circle = Circle(5)
circle.calculate_area()   # Output: 78.5
circle.display()          # Output: Circle with radius 5
