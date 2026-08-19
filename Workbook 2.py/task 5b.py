# here are some simple general knowledge questions that force retry until correct

# keep asking until the answer is "london"
while True:
    ask = input("What's the capital of England? ")
    if ask.strip().lower() == "london":
        print("Correct")
        break
    else:
        print("Incorrect, please try again.")

# keep asking until the answer is "25"
while True:
    ask = input("What's 5 * 5? ")
    if ask.strip() == "25":
        print("Correct")
        break
    else:
        print("Incorrect, please try again.")

# keep asking until the answer is "russia"
while True:
    ask = input("What's the biggest country? ")
    if ask.strip().lower() == "russia":
        print("Correct")
        break
    else:
        print("Incorrect, please try again.")
        # if you got 1/3 you get a c
        # if you got 2/3 you get a b
        # if you got 3/3 you get an a
        # if you got 0/3 you get a fail
        print("Note: The answer is not case sensitive, so 'Russia', 'russia', and 'RUSSIA' are all correct answers.")
        print ("Note: The answer is not case sensitive, so 'London', 'london', and 'LONDON' are all correct answers.")