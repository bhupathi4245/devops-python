# 
sample_str = "This is a string"
# Type conversion
# Converting string to list
str_to_list = list(sample_str)  # ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
print(f"String to list: {str_to_list}")
# Converting string to tuple
str_to_tuple = tuple(sample_str)  # ('T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
print(f"String to tuple: {str_to_tuple}")
# Converting string to set
str_to_set = set(sample_str)  # {'a', 's', 'i', 'h', 'n', 'g', 'T', 'r', ' '}
print(f"String to set: {str_to_set}")

# Accept user input and convert it to different types
user_input = input("Enter a number: ")  # User enters '42'
# Convert the input to an integer
try:
    user_input_int = int(user_input)  # 42
    print(f"User input as integer: {user_input_int}")
except ValueError:
    print("Invalid input for integer conversion.")
# Convert the input to a float
try:
    user_input_float = float(user_input)  # 42.0
    print(f"User input as float: {user_input_float}")
except ValueError:
    print("Invalid input for float conversion.")

# Converting list to string
sample_list = ['H', 'e', 'l', 'l', 'o']
list_to_str = "".join(sample_list)  # 'Hello'
print(f"List to string: {list_to_str}")

# splitting a string into a list
sample_str = "Hello, World!"
str_to_list = sample_str.split(", ")  # ['Hello', 'World!']
print(f"String to list using split: {str_to_list}")