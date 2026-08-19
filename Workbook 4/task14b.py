first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
year_of_birth = int(input("What year were you born? "))
current_year = 2026

# create a suggested username from first name, last name and year of birth
suggest_a_username = f"{first_name.lower()}.{last_name.lower()}{year_of_birth}"

print("Suggested username:", suggest_a_username)