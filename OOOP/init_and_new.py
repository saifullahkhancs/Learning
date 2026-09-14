class Person:
    def __new__(cls, name, age):
        print("1. __new__ called: Allocating memory for the object...")
        # Create and return the instance using the parent object class
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print("2. __init__ called: Initializing attributes on self...")
        self.name = name
        self.age = age

# Instantiating the object
p = Person(name="Alice", age=30)