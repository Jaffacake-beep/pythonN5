#task11e
print("Options: A) 100 B) 90 C) 110")
answer = input(" 56+44 = ?")
if answer == "A":
    print("Correct!")
else:
    print("Incorrect.")
    repeat = input("Would you like to try again? (Y/N) ")
    if repeat.lower() == "y":
        answer = input(" 56+44 = ?")
        if answer == "A":
            print("Correct!")
        else:
            print("Incorrect. The correct answer is A) 100.")