#Polymorphism in object-oriented programming refers to the ability of objects to 
#exhibit different behaviors based on their specific class or type, allowing them 
#to be used interchangeably and providing code flexibility and reusability

  #POlymorphism basically refer to the methoid over laoding and overriding


class Animal:
    def sound(self):
        print("animal made some sound")

class cat(Animal):
    def sound(self):
        print("meowww")

class dog(Animal):
    def sound(self):
        print("bahu")

animal = Animal()
animal.sound()

catt = cat()
catt.sound()

dogg = dog()
dogg.sound()


class Car:
    def __init__(self, name , tyres):
        self.name = name
        self.tyres = tyres

    def tyre_info(self):
        print("the number of the tyres are ", self.tyres)

class Bike:
    def __init__(self, name , tyres):
        self.name = name
        self.tyres = tyres

    def tyre_info(self):
        print("the number of the tyres are ", self.tyres)

car = Car("suzuki" , 4)
car.tyre_info()

bike  = Bike("honda", 2)
bike.tyre_info()


class Calculator:
    def add(self,*args):
        if len(args)==2:
            d = args[0] + args[1]
            print("sum is eqaul to", d)
        else:
            d = args[0] + args[1] + args[2]
            print("sum is eqaul to", d)

# Usage
calculator = Calculator()
calculator.add(2, 3)     # Output: TypeError: add() missing 1 required positional argument: 'c'
calculator.add(2, 3, 4)