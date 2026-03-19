# For loop
sample_list = ["Ansible", "Terraform", "Jenkins", "Docker", "K8s"]
print("Using for loop to iterate over the list:")
for tool in sample_list:
    print(tool, len(tool))

for idx, tool in enumerate(sample_list):
    print(f"Index: {idx}, Tool: {tool}")

# While loop
print("\nUsing while loop to iterate over the list:")
idx = 0
while idx < len(sample_list):
    print(sample_list[idx])
    idx += 1

for idx in range(0, len(sample_list)):
    print(f"Index: {idx}, Tool: {sample_list[idx]}")

for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Jenkins":
        print(f"Found Jenkins at index: {sample_list(idx)}")
        break

for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Jenkins":
        print(f"Found Jenkins at index {idx}: {sample_list(idx)}")
        continue
    print(f"Index: {idx}, Tool: {sample_list[idx]}")

for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Jenkins":
        pass  # This will do nothing and continue to the next iteration
        print(f"Found Jenkins at index {idx}: {sample_list(idx)}")
        break

# exit code
for idx in range(0, len(sample_list)):
    if sample_list[idx] == "Jenkins":
        print(f"Found Jenkins at index {idx}: {sample_list(idx)}")
        exit(0)  # Exit the program with a success code
    print(f"Index: {idx}, Tool: {sample_list[idx]}")

sample_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("\nIterating over dictionary items:")
for key, value in sample_dict.items():
    print(f"{key}: {value}") 
