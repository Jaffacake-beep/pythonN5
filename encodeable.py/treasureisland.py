print("Welcome to Treasure Island, a choose-your-own-adventure game.")
print("Legend has it that there is some buried treasure on the island you are exploring… so you have decided to in search for it.")
def game():
    choice1 = input("You are at a crossroad. Where do you want to go? Type 'left' or 'right' ").strip().lower()
    if choice1 == "left":
        choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").strip().lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").strip().lower()
            if choice3 == "yellow":
                print("Congratulations! You found the treasure!")
            elif choice3 == "red":
                print("It's a room full of fire! Game Over.")
            elif choice3 == "blue":
                print("You enter a room of beasts! Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")

game()