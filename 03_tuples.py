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

sample_tuple[1] = "Puppet"  # This will raise an error because tuples are immutable


# Operations on tuples
res_tuple = sample_tuple + ("Git", "Ansible Tower")  # Concatenation
print(f"Concatenated tuple: {res_tuple}")

res_tuple = sample_tuple * 2  # Repetition
print(f"Repeated tuple: {res_tuple}")
# Method 2: Using the tuple() constructor