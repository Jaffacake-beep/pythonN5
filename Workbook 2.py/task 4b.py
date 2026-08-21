# Simple IF/Else statement
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age input.")
else:
    if age > 18:
        print("You are old enough to drink !")
    else:
        print("You are not old enough to drink.")