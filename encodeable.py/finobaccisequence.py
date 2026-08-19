# A program to display terms of the fibonacci sequence

# ----------------
# Subprograms
# ----------------

# ----------------
# Main program
# ----------------
print("Welcome to the Fibonacci sequence generator!")
num_terms = int(input("How many terms of the Fibonacci sequence would you like to see? "))  
def generate_next_term(first_term, second_term):
  next_term = first_term + second_term
  return next_term
print("Welcome to the Fibonacci Sequence generator!")
number_of_terms = int(input("How many terms would you like? "))
first_term = 0
second_term = 1
number_of_terms_generated = 0
while number_of_terms_generated < number_of_terms:
  print(first_term) 
  next_term = generate_next_term(first_term, second_term)
  first_term = second_term
  second_term = next_term
  number_of_terms_generated += 1