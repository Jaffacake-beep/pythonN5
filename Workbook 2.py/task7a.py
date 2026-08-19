try:
    exam_score = int(input("What did you get on your recent exam? "))
except ValueError:
    print("Please enter a valid integer score.")
else:
    if exam_score >= 90:
        print("You got an A!")
    elif exam_score >= 70:
        print("You got a B!")
    elif exam_score >= 50:
        print("You got a C!")
    elif exam_score >= 40:
        print("You got a D!")
    else:
        print("You got an F!")
        