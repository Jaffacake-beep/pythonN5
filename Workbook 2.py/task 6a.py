name= input ("What is your name?")
age= int(input ("What is your age?"))
if age < 12 and age > 3:
    print ("You are a child so you should be in primary school.")
elif age < 18 and age > 12:
    print ("You are a teenager so you should be in secondary school.")
else:
    print ("You are not in the age range for primary or secondary school.")
