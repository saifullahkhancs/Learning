
def pretty(func):
    def inner():
        print("adding something before function")

        func()

        print("adding  before function")
    return inner

def ordinary():
    print("i am calll inside the other function")

decorater = pretty(ordinary)

decorater()


# passing fiunction as a parameter
"""
def pretty(func):
   # def inner():
        print("adding something before function")

        func()

        print("adding after before function")
    #return inner


def ordinary():
    print("i am calll inside the other function")
    
pretty(ordinary)
#decorater = pretty(ordinary)

#decorater()

"""