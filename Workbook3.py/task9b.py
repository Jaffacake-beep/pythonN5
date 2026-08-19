target = 54
count = 0
while True:
    guess = int(input("Guess my number between 1 and 100: "))
    count += 1
    if guess == target:
        print("Correct")
        break
    else:
        print("Incorrect, please try again.")
        # the user won't be able to continue until they get the answer correct, so they will have to keep trying until they get it right. This is a simple way to test their knowledge and encourage them to learn.
print(f"You guessed the number in {count} tries!")
