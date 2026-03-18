# How to create a list

sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"] # list() # empty list

# Indexing and slicing
sample_ele = sample_list[1]  # 'Terraform'
print(f"Element of index: {sample_ele}")

sample_ele = sample_list[-1]  # 'K8s'
print(f"Last element using index: {sample_ele}")

sample_ele = sample_list[len(sample_list) - 1]  # 'K8s'
print(f"Last element using length: {sample_ele}")

# Error handling for index out of range
try:
    out_of_range_ele = sample_list[10]  # This will raise an error 
except IndexError as e:
    print(f"Error: {e}")

# Slicing in lists
sliced_list = sample_list[1:4]  # ('Terraform', 'Jenkins', 'Docker')
print(f"Slice (1:4): {sliced_list}")

sliced_list_len = len(sample_list)  # 3
print(f"Length of sliced tuple: {sliced_list_len}")

# List mutability  where as tuples are immutable, lists are mutable, 
# which means you can change their content without changing their identity. 
# You can add, remove, or modify elements in a list after it has been created.
sample_list[0] = "Puppet"  # This will work because lists are mutable
print(f"Modified list: {sample_list}")

# Append and extend
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
sample_list.append("Git")  # Adds 'Git' to the end of the list
print(f"List after append: {sample_list}")

sample_list.extend(["Ansible Tower", "GitHub Actions"])  # Adds multiple elements to the end of the list
print(f"List after extend: {sample_list}")
sample_list.append(sample_list[2])  # Adds the list itself as an element (creating a nested list)
print(f"List after appending itself: {sample_list}")

# Insert
sample_list.insert(2, "Puppet")  # Inserts 'Puppet' at index 2
print(f"List after insert: {sample_list}") 

# Remove and pop
sample_list.remove("Docker")  # Removes the first occurrence of 'Docker'
print(f"List after remove: {sample_list}")