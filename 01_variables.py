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

# Operations on variables
# Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, 
# Floor Division, Assignment, Comparison, Logical, Identity, Membership Operators, 

# Add
x = 10
y = 5
add_result = x + y
print(f"Addition: {x} + {y} = {add_result}")

# Subtract
subtract_result = x - y 
print(f"Subtraction: {x} - {y} = {subtract_result}")

# Multiply
multiply_result = x * y
print(f"Multiplication: {x} * {y} = {multiply_result}")

# Divide
divide_result = x / y
print(f"Division: {x} / {y} = {divide_result}")

# Modulus
modulus_result = x % y 
print(f"Modulus: {x} % {y} = {modulus_result}")

# Exponentiation
exponentiation_result = x ** y
print(f"Exponentiation: {x} ** {y} = {exponentiation_result}")

# Floor Division
floor_division_result = x // y
print(f"Floor Division: {x} // {y} = {floor_division_result}")

# Assignment
z = 20 
print(f"Assignment: z = {z}")  

# Comparison
comparison_result = x > y 
print(f"Comparison: {x} > {y} = {comparison_result}")

# Logical
logical_result = (x > 5) and (y < 10)
print(f"Logical: (x > 5) and (y < 10) = {logical_result}")

# Identity
identity_result = (x is y)
print(f"Identity: (x is y) = {identity_result}")

# Membership
membership_result = 5 in [1, 2, 3, 4, 5]
print(f"Membership: 5 in [1, 2, 3, 4, 5] = {membership_result}")

# Power
power_result = x ** 2
print(f"Power: {x} ** 2 = {power_result}")

# Comparison operators
print(f"Is {x} equal to {y}? {x == y}")
print(f"Is {x} not equal to {y}? {x != y}")
print(f"Is {x} greater than {y}? {x > y}")
print(f"Is {x} less than {y}? {x < y}")
print(f"Is {x} greater than or equal to {y}? {x >= y}")
print(f"Is {x} less than or equal to {y}? {x <= y}")

# Logical operators AND, OR, NOT
a = True
b = False
print(f"Logical AND: {a} and {b} = {a and b}")
print(f"Logical OR: {a} or {b} = {a or b}")
print(f"Logical NOT: not {a} = {not a}")
print(f"Logical NOT: not {b} = {not b}")