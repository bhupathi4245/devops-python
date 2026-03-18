# A set can contain mixed data types and prints unique set and in ordered manner. 
# A set is an unordered collection of unique elements. 
# It is defined using curly braces {} or the set() constructor.
# Sets are mutable, which means you can add or remove elements from a set after -
# it has been created. However, the elements themselves must be immutable -
# (like numbers, strings, or tuples) because sets use hashing to store their elements.
# It is defined using curly braces {} or the set() constructor. 
# set functions doesn't support indexing and slicing because sets are unordered -
# collections. 

sample_set = {1, 2, 3, "Hello", True}  
print(f"Sample set: {sample_set}")

# Adding elements to a set
sample_set.add("World")  # Adds 'World' to the set
print(f"Set after adding 'World': {sample_set}")

# Removing elements from a set
sample_set.remove(2)  # Removes the element 2 from the set
print(f"Set after removing 2: {sample_set}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union_set = set_a.union(set_b)  # {1, 2, 3, 4, 5, 6}
print(f"Union of set_a and set_b: {union_set}") 

intersection_set = set_a.intersection(set_b)  # {3, 4}
print(f"Intersection of set_a and set_b: {intersection_set}")

difference_set = set_a.difference(set_b)  # {1, 2}
print(f"Difference of set_a and set_b: {difference_set}")