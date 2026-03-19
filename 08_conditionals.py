# Calculate wheather conditions based on temperature and humidity
temperature = int(input("Enter todays temperature range 10 to 60: "))  # 30
# humidity =  int(input("Enter todays humidity range 30 to 100: "))  # 70
""" if temperature > 25 and humidity > 60:
    print("It's hot and humid.")
elif temperature > 25 and humidity <= 60:
    print("It's hot but not humid.")
elif temperature <= 25 and humidity > 60:
    print("It's not hot but it's humid.")
else:
    print("It's not hot and not humid.") """

if 10 <= temperature <= 60:
    humidity =  int(input("Enter todays humidity range 30 to 100: "))  # 70
    if 30 <= humidity <= 100:
        if temperature > 25 and humidity > 60:
            print("It's hot and humid.")
        elif temperature > 25 and humidity <= 60:
            print("It's hot but not humid.")
        elif temperature <= 25 and humidity > 60:
            print("It's not hot but it's humid.")
        else:
            print("It's not hot and not humid.")
    else:
        print("Humidity is out of the expected range.")
       # break
else:
    print("Temperature is out of the expected range.")
    breakpoint