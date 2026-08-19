# A program to check if the user is old enough to vote in the UK
# ----------------
# Subprograms
# ----------------
def check_age(age):
    if age >= 18:
        print("You are old enough to vote!")
# ----------------
# Main program
# ----------------
user_age = int(input("How old are you? "))
check_age(user_age)
if user_age < 18:
    print("You are not old enough to vote.")
    if user_age < 15:
        print("You are not old enough to vote.")