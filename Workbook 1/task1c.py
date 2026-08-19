choice = input("Would you like to greet someone? (yes/no): ")
if choice == "yes":
    name = input("What is your name? ")
    hello = "Hello, " + name + "!"
    print(hello)
else:
    print("Okay, maybe next time!")