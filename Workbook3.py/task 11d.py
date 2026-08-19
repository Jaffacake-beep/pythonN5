name = input("What is your name? ")
gender = input("What is your gender? ")
if gender == "male" or gender == "female":
    print("Gender accepted")
else:
    print("Gender invalid")
print("What age are you? ") 
age = int(input())
if age < 0 or age > 120:
        print("Age invalid")
else: 
        valid = True  