# Association: Association represents a relationship between two or more classes, 
# where objects of one class are connected to objects of another class.
#  It is a general relationship and can be represented by a unidirectional 
#  or bidirectional association.

class Car:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print(f"The {self.name} car's engine has started.")
class Driver:
    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        print(f"{self.name} is driving the {car.name} car.")
        car.start_engine()

# Create instances of Car and Driver
my_car = Car("Tesla")
driver = Driver("John")
# Associate the Car instance with the Driver instance
driver.drive_car(my_car)

class Cars:
    def __init__(self, name):
        self.name = name
class Person:
    def __init__(self,name):
        self.name = name

    def belonging(self , car):
        print(f"{car.name} is belong to the {self.name}")

car  = Cars("marsedes")
person = Person("ali")
person.belonging(car)


def abc(a=[]):
    a.append(1)
    print(a)

abc()
abc()
abc()
