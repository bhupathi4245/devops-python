# This is a single line comment

""" 
    This is a multi-line comment
    that spans multiple lines
 """

a = 42
print(a)

"""
- Boolean values: True, False
- Strings: "Hello", 'World'
"""

# Floating-point numbers: 3.14, -0.001
b = 3.14
print(b)

# boolean value.. Pythons is case senstive True and true are different
c = True
print(c)

# Strings
d = "Hello, World!"
e = 'Python is great!'
print(d)
print(e)

# Todays weather is nice, but tomorrow it will be rainy.
f = 'Today\'s weather is nice, but tomorrow it will be rainy.'
print(f)

"""
- Lists: [1, 2, 3], ['apple', 'banana', 'cherry']
- Tuples: (1, 2, 3), ('apple', 'banana', 'cherry')
- Dictionaries: {'name': 'Alice', 'age': 30}    
- Sets: {1, 2, 3}, {'apple', 'banana', 'cherry'}    
- None: Represents the absence of a value
- Complex numbers: 1 + 2j
"""

# type() function is used to check the data type of a variable
test_list = [1, 2, 3], ['apple', 'banana', 'cherry']
print(f"test_list: {test_list} is a data type of {type(test_list)}.")

test_tuple = (1, 2, 3), ('apple', 'banana', 'cherry')
print(f"test_tuple: {test_tuple} is a data type of {type(test_tuple)}.")

test_dictionary = {'name': 'Alice', 'age': 30}
print(f"test_dict: {test_dictionary} is a data type of {type(test_dictionary)}.")

test_set = {1, 2, 3}, {'apple', 'banana', 'cherry'}
print(f"test_set: {test_set} is a data type of {type(test_set)}.")

test_none = None
print(f"test_none: {test_none} is a data type of {type(test_none)}.")

test_complex = 1 + 2j
print(f"test_complex: {test_complex} is a data type of {type(test_complex)}.")