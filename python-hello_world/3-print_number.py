#!/usr/bin/python3
number = 5  # You can change this to test different values

if isinstance(number, int):
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print(f"{number} is zero")
    else:
        print(f"{number} is negative")
else:
    print("Wrong type")
