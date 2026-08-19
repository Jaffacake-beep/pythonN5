# Task 11a 
valid = False 
while valid == False: 
    print("What age are you? ") 
    age = int(input())
    if age < 0 or age > 120:
        print("Age invalid")
    else: 
        valid = True    
        print ( "Input is valid" )
print("Hey jake")