sample_dict = {1:1, 2:4, 3:9, 4:16, 5:25}  # Dictionary with integer keys and values (squares)
print(f"Sample dictionary: {sample_dict}")

# Accessing values using keys
value_of_3 = sample_dict[3]  # 9
print(f"Value of key 3: {value_of_3}")

# Adding a new key-value pair
sample_dict[6] = 36  # Adding key 6 with value 36
print(f"Dictionary after adding new key-value pair: {sample_dict}")

# Modifying an existing value
sample_dict[2] = 8  # Modifying the value of key 2 to 8
print(f"Dictionary after modifying value of key 2: {sample_dict}")

# Removing a key-value pair
del sample_dict[4]  # Removing the key-value pair with key 4
print(f"Dictionary after removing key 4: {sample_dict}")

# Dictionary methods
keys = sample_dict.keys()  # dict_keys([1, 2, 3, 5, 6])
print(f"Keys in the dictionary: {keys}")
values = sample_dict.values()  # dict_values([1, 8, 9, 25, 36])
print(f"Values in the dictionary: {values}")
items = sample_dict.items()  # dict_items([(1, 1), (2, 8), (3, 9), (5, 25), (6, 36)])
print(f"Key-value pairs in the dictionary: {items}")

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}  # Creates a dictionary of numbers and their squares
print(f"Squared dictionary: {squared_dict}")

# What happens if you access a key that is not present inside a dict
sample_dict = {"1": 1, 2: 4, 3: 9}
print(sample_dict.get("1")) # 1
print(sample_dict.get(1)) # None
# print(sample_dict[1]) # Error

sample_dict = {1: 1, 2: 4, 3: 9}
sample_dict[4] = 16
print(sample_dict)