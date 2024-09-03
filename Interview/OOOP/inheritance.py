class Vechicle:
    def __init__(self,type):
        self.type = type

    def type_info(self):
        print("the type  is" , self.type)

    def _pro_info(self):
        print("this is  my comapny")


class Car(Vechicle):
    def __init__(self,type,name):
        super().__init__(type)
        self.name=name

    def prod_info(self):
        print("the",self.name,"ia a",self.type)


car = Car("car", "123")

car.prod_info()
car.type_info()
car._pro_info()