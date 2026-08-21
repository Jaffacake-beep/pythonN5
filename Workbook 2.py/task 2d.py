# Simple IF/Else statement
ask = input("What did you get out of 70 in your test? ")
calculation = (float(ask) / 70) * 100

if calculation >= 50:
    print("You passed!")
else:
    print("You failed.")