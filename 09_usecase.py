# login System
username = "ec2-user"
password = "DevOps321"

input_username = input("Enter username: ")
input_password = input("Enter password: ") 

if input_username == username and input_password == password:
    print("Login successful!")
else:
    print("Invalid username or password.")