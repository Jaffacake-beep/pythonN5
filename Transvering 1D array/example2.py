#308c Transversing 1D array
# WE DONT NEED TO KNOW ThIS FOR NAT5

target = 8
position = -1
items = [4.9, 6, 13]
for index in range(len(items)):
      if target == items[index]:
          print("FOUND IT")  
          position = index
          
if position  < 0:
    print("Item not found")