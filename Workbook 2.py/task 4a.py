# Simple IF/Else statement
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid integer for age.")
else:
    if age > 17:
        print("You are young enough to drive!")
    else:
        print("You are too young to drive.")