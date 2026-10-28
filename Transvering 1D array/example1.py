#308c Transversing 1D array
total = 0
items = [4.9, 6,13] # <-- array
for index in range(len(items)): # < -- fixed loop,len 
    total = total + items[index] # <-- adds current item to total
     
print(total)