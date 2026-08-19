first_score = int(input("What is your score on the first test? "))
second_score = int(input("What is your score on the second test? "))
# both tests are out of 100
if first_score > 60 and second_score > 50:
    print("You are eligible to take the third test.")
else: 
    print("You are not eligible to take the third test.")
