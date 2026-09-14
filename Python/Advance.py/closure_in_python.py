# ==============================================================================
# DEFINITION: Python Closures & Enclosing Scope
# ==============================================================================
#
# A CLOSURE is an inner function that retains access to variables from its
# enclosing (outer) scope, even after the outer function has finished executing.
#
# Three conditions must be met to form a closure:
# 1. There must be a nested function (a function inside a function).
# 2. The nested function must refer to a variable defined in the enclosing scope.
# 3. The enclosing function must return the nested function object.
#
# Closures allow functions to carry state with them without using global variables
# or full class structures.
# ==============================================================================


def power_factory(exponent):
    """Enclosing function that accepts an exponent and returns a closure."""
    def power(base):
        # 'exponent' is captured from the enclosing scope
        return base ** exponent
    
    # Returning the inner function object without calling it
    return power


# ==============================================================================
# EXECUTION & DEMONSTRATION
# ==============================================================================
if __name__ == "__main__":
    # Create a 'square' function (exponent = 2)
    square = power_factory(2)
    
    # Create a 'cube' function (exponent = 3)
    cube = power_factory(3)

    # Calling the closures with different bases
    res1 = square(10)  # 10 ** 2 = 100
    res2 = cube(10)    # 10 ** 3 = 1000
    res3 = cube(5)     # 5 ** 3 = 125
    res4 = square(15)  # 15 ** 2 = 225

    # Print results
    print(f"square(10) -> {res1}")
    print(f"cube(10)   -> {res2}")
    print(f"cube(5)    -> {res3}")
    print(f"square(15) -> {res4}")
    
    # Inspecting free variables stored in the closure's cell environment
    print(f"\nCaptured variable value in 'square': {square.__closure__[0].cell_contents}")
    print(f"Captured variable value in 'cube':   {cube.__closure__[0].cell_contents}")