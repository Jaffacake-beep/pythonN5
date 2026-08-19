score = 0
question_number = 1

print("What is the capital of Russia?")
answer = "Moscow"
user_answer = input("Your answer: ").strip()
if user_answer.lower() == answer.lower():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The capital of Russia is {answer}.")
print(f"Your score after question {question_number}: {score}/{question_number}")
question_number += 1

print("What is the capital of France?")
answer = "Paris"
user_answer = input("Your answer: ").strip()
if user_answer.lower() == answer.lower():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The capital of France is {answer}.")
print(f"Your score after question {question_number}: {score}/{question_number}")
question_number += 1

print("What is the capital of England?")
answer = "London"
user_answer = input("Your answer: ").strip()
if user_answer.lower() == answer.lower():
    print("Correct!")
    score += 1
else:
    print(f"Wrong! The capital of England is {answer}.")
print(f"Your score after question {question_number}: {score}/{question_number}")

# final total
print(f"Final score: {score}/{question_number}")
            