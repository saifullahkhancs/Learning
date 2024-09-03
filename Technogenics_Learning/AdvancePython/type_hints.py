#  Type Hints
'''
python has support for optional "type hints" (also called "type annotations").
These "type hints" or annotations are a special syntax that allow declaring the type of a variable.
By declaring types for your variables, editors and tools can give you better support. 
'''

def get_full_name_with_no_suggestion(first_name, last_name):
    '''
    used to check that when we do not define the type the code will not \n
    give the suggestions '''
    full_name = first_name.title() + " " + last_name.title()
    return full_name



print(get_full_name_with_no_suggestion("john", "doe"))


def get_full_name_with_suggestion(first_name : str, last_name : str):
    '''
    used to check that when we defione  the type the code will \n
    give the suggestions '''
    full_name = first_name.capitalize() + " " + last_name.title()
    return full_name



print(get_full_name_with_suggestion("john", "doe"))
