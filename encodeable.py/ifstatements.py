if 6 < 7:
    print("Wow")
    print("6 is less than 7")

def how_are_you():
    feeling = input("How are you?")
    if feeling == "good":
        print("So am I!")
        how_are_you()

    elif feeling == "bad":
        print("Sorry to hear that.")