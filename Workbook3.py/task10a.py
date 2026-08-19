# Ask five pupils for their daily calorie intake, validate numeric input, and print the average.
calories = []
for i in range(1, 6):
    intake  = input(f"Enter daily calorie intake for pupil {i}: ")
    while True:
        try:
            calories.append(float(intake))
            break
        except ValueError:
            intake = input("Invalid input. Please enter a numeric value: ")
            print ("Please enter a valid number for calories.")
average_calories = sum(calories) / len(calories) if calories else 0
print(f"Average calories eaten in a day: {average_calories}")