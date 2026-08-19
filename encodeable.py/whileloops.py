# A program which constantly asks "Are we nearly there yet?"

# ----------------
# Subprograms
# ----------------
def ask_if_nearly_there():
  arrived = False
  while not arrived:
    input("Are we nearly there yet?")
  
# ----------------
# Main program
# ----------------
ask_if_nearly_there()
arrived = False
while not arrived:
	answer = input("Are we nearly there yet?")
	if answer == "yes":
		arrived = True
print("Yay!")