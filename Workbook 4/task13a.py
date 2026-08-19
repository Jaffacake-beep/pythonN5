array = []
for i in range(5):
    number = int(input("Enter a number: "))
    array.append(number)
    
print("Your numbers:", ' '.join(str(n) for n in array))
# add the five numbers together and print the total
total = sum(array)
print("The total is:", total)