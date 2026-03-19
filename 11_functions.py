def sample_func():
    print("This is a sample function.") 

sample_func()  # Calling the function to execute its code

# Function with parameters
def greet(name):    
    print(f"Hello, {name}!")
greet("Alice")  # Calling the function with an argument

# Function with return value
def add(a, b):
    return a + b
result = add(5, 3)  # Calling the function and storing the return value
print(f"The sum of 5 and 3 is: {result}")

# Function with default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Calling the function without an argument, will use default value
greet("Bob")  # Calling the function with an argument, will override default value

# Function with variable-length arguments
def sum_all(*args):
    total = sum(args)
    print(f"The sum of {args} is: {total}")
sum_all(1, 2, 3)  # Calling the function with multiple arguments
sum_all(4, 5)     # Calling the function with different number of arguments

# Function with keyword arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")
display_info(name="Charlie", age=25)  # Calling the function with keyword arguments
display_info(age=30, name="Dave")  # Calling the function with keyword arguments in different order

# lambda function
square = lambda x: x * x  # A simple lambda function to calculate the square of a number
print(f"The square of 5 is: {square(5)}")  # Calling the lambda function with an argument

# Recursive function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"The factorial of 5 is: {factorial(5)}")  # Calling the recursive function
