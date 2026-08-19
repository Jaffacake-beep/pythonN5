import random

#task12d
numbers = random.sample(range(1, 60), 6)
numbers.sort()

print("  6 numbers between 1-59")
print(" do not repeat any numbers")
print(" This is your lotto lucky dip")
print("Your numbers:", ' '.join(str(n) for n in numbers))

