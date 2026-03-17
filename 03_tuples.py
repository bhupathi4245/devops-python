# There are 2 methods to create a tuple:
# Method 1: Using parentheses
my_tuple = (1, 2, 3, "Hello", True)
sample_tuple = ("Ansible", "Terraform", "Jenkins", "Docker", "K8s") # my toolkit

sample_ele = sample_tuple[0]  # 'Ansible'
print(f"First element: {sample_ele}")

sample_slice = sample_tuple[1:4]  # ('Terraform', 'Jenkins', 'Docker')
print(f"Slice (1:4): {sample_slice}")

sliced_tuple_length = len(sample_slice)  # 3
print(f"Length of sliced tuple: {sliced_tuple_length}")

# sample_tuple[1] = "Puppet"  # This will raise an error because tuples are immutable
"""
Traceback (most recent call last):
  File "C:\devops\bhupathi4245\repos\devops-python\03_tuples.py", line 15, in <module>
    sample_tuple[1] = "Puppet"  # This will raise an error because tuples are immutable
    ~~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# Operations on tuples
res_tuple = sample_tuple + ("Git", "Ansible Tower")  # Concatenation
print(f"Concatenated tuple: {res_tuple}")

res_tuple = sample_tuple * 2  # Repetition
print(f"Repeated tuple: {res_tuple}")

# Methods
k8s_idx = sample_tuple.index("K8s")  # 4
print(f"Index of 'K8s': {k8s_idx}")
count_ansible = sample_tuple.count("Ansible")  # 1
print(f"Count of 'Ansible': {count_ansible}")   

# k8s_idx = sample_tuple.index("k8s")  # This will raise an error because 'k8s' is not in the tuple (case-sensitive)
"""
Traceback (most recent call last):
  File "C:\devops\bhupathi4245\repos\devops-python\03_tuples.py", line 37, in <module>
    k8s_idx = sample_tuple.index("k8s")  # This will raise an error because 'k8s' is not in the tuple (case-sensitive)
ValueError: tuple.index(x): x not found """

# Tuple unpacking
tool1, tool2, tool3, tool4, tool5 = sample_tuple
print(f"Unpacked tools: {tool1}, {tool2}, {tool3}, {tool4}, {tool5}")

# Method 2: Using the tuple() constructor