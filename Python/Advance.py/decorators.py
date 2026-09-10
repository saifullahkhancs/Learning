# Decorators Defination
#                      In Python decorators are the     

# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice


# @do_twice
# def say_whee():
#   print("Whee!")


# say_whee()
# xyx = "hamza"

# def test(name):
  
#   def inside_test():
#     print(name)
#     print(xyx)
#   return inside_test

# test("ali")()

def do_one(func):
  print("executing one")
  def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
  return wrapper_do_twice
  

def do_twice(func):
    print("executing twice")
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

# it will look like this do_one(do_twice(say_whee(name)))

@do_one
@do_twice
def say_whee(name):
    print(name)


say_whee("ali")




def first(func):
    print("first is executed")
    func()
    print("first ended")


def secon(func):
    print("first is executed")
    func()
    print("first ended")