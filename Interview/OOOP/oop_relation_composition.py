# Composition: Composition is a strong form of aggregation where the part class 
# is tightly coupled to the whole class. The part class cannot exist without the
# whole class. It is represented by a filled diamond-shaped arrow pointing from 
# the part class to the whole class.

# Inheritance: Inheritance represents an "is-a" relationship, where one class 
# inherits the properties and behaviors of another class. The class that inherits 
# is called the subclass or derived class, and the class being inherited from is 
# called the superclass or base class


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.engine = Engine(capacity)

    def start_engine(self):
        self.engine.start()
        print(f"{self.brand} car's engine started.")

my_car = Car("Tesla", 1000)
my_car.start_engine()
