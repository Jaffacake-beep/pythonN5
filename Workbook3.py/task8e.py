ask = input("10 pupils test scores? ")
scores = ask.split()
total = 0
for score in scores:
    total += float(score)
print(f"Total: {total}")
print(f"Average: {total / len(scores)}")
ask = input("How many times do you want to display the average? ")
for _ in range(int(ask)):
    print(f"Average: {total / len(scores)}")
    ask = input("How much people passed? ")
    print(f"Pass percentage: {(float(ask) / len(scores)) * 100}%")
    