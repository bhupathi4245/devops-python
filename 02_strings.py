sample_str = "This is a sample string."

# Accessing characters
first_char = sample_str[0]  # 'T'
last_char = sample_str[-1]  # '.'
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

# Slicing
substring = sample_str[5:7]  # 'is'
print(f"Substring (5:7): {substring}")

# String methods    
upper_str = sample_str.upper()  # 'THIS IS A SAMPLE STRING.'
lower_str = sample_str.lower()  # 'this is a sample string.'
print(f"Uppercase: {upper_str}")
print(f"Lowercase: {lower_str}")

# String concatenation
greeting = "Hello, "
name = "Alice"
full_greeting = greeting + name  # 'Hello, Alice'
print(full_greeting)

# String formatting
age = 30
formatted_str = f"{name} is {age} years old."  # 'Alice is 30 years old.'
print(formatted_str)

# String methods for searching
index_of_sample = sample_str.find("sample")  # 10
print(f"Index of 'sample': {index_of_sample}")

# String methods for replacing
replaced_str = sample_str.replace("sample", "example")  # 'This is a example string.'
print(replaced_str)

# String methods for splitting
words = sample_str.split()  # ['This', 'is', 'a', 'sample', 'string.']
print(f"Words in the string: {words}") 

# String slicing with step == This is a sample string.
every_second_char = sample_str[::2]  # 'Ti sasml tig'
print(f"Every second character: {every_second_char}")

# String length
length_of_str = len(sample_str)  # 27
print(f"Length of the string: {length_of_str}")

# String methods for joining
joined_str = " ".join(words)  # 'This is a sample string.'  
print(f"Joined string: {joined_str}")

# String reversal
reversed_str = sample_str[::-1]  # '.gnirts elpmas a si sihT'
print(f"Reversed string: {reversed_str}")   

# String immutability
try:
    sample_str[0] = 't'  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")
"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/02_strings.py", line 52, in <module>
    sample_str[-1] = 'G'
TypeError: 'str' object does not support item assignment
"""