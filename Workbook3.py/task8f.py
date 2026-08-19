for counter in range(100, 0, -1):
    print(counter)
    next_count = counter - 1
    next_bottles = "bottle" if next_count == 1 else "bottles"
    current_bottles = "bottle" if counter == 1 else "bottles"
    print(f" {counter} {current_bottles} of beer on the wall, {counter} {current_bottles} of beer. Take one down and pass it around, {next_count} {next_bottles} of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 100 bottles of beer on the wall.")