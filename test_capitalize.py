


# Import Modules

import pytest


# test_capitalize.py

# a function called capital_case which should take a string as its argument
# and should return a capitalized version of the string.

def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Provide string argument')
    return x.capitalize()

# Writing a test to ensure the function is doing what is says

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

# a test that defines if it's not a string

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError): # the function should raise a type error if there is no string
        capital_case(9)

# to see if the function and test works run 'pytest' in the terminal


