ask = input("Whats your name? ")
print(f"Hello, {ask}!")
ask2= input( "How much times do you want your name to be displayed on the screen? ")
for _ in range(int(ask2)):
    print(ask)