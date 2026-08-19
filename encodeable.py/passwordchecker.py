# A program to check if a user's password matches the default password
# ----------------
# Constants
# ----------------
PASSWORD = "LetMeIn"
# ----------------
# Subprograms
# ----------------
# ----------------
# Main program
# ----------------
user_password = input("Enter your password: ")
if user_password == PASSWORD:
  print("Password correct!")
else:
  print("Password incorrect!")