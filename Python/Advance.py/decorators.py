# Decorators Defination
#                      In Python decorators are the wrappers 

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

# def do_one(func):
#   print("executing one")
#   def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#   return wrapper_do_twice
  

# def do_twice(func):
#     print("executing twice")
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice

# # it will look like this do_one(do_twice(say_whee(name)))

# @do_one
# @do_twice
# def say_whee(name):
#     print(name)


# say_whee("ali")




# def first(func):
#     print("first is executed")
#     print("first ended")


# def second(func):
#     print("second  is executed")      
#     print("second ended")



# @first
# @second
# def third():
#     print("third is executed")

# third()


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

abc=return_greeting("Adam")

print(abc)

print(return_greeting.__name__)

# it will print 'wrapper_do_twice'

# Why we use wraps and functools??
#Ans:- It will preserve the information about the original function.

import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def say_whee():
    print("Whee!")

say_whee()

print(say_whee.__name__)


import time
import functools
    
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        """here is function wrapper function defination plus documentation """
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    """here is function documentation """
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


waste_some_time(1)
waste_some_time(999)

# testing functool and wraps
print(waste_some_time.__name__)
print(waste_some_time.__doc__)



def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    '''here is function documentation '''
    print(f"Hello {name}")

greet("World")

print(greet.__name__)
print(greet.__doc__)