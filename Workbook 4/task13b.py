# Collect 5 student names and their test scores (out of 150),
# then print whether each student passed (>= 70%) or failed.

NUM_STUDENTS = 5
MAX_SCORE = 150
PASS_MARK = 0.7 * MAX_SCORE  # 70% of 150 = 105

names = []
for i in range(NUM_STUDENTS):
	name = input(f"Enter the name of student {i + 1}: ").strip()
	names.append(name)

scores = []
for i in range(NUM_STUDENTS):
	while True:
		try:
			value = input(f"Enter the test score for {names[i]} (out of {MAX_SCORE}): ").strip()
			score = float(value)
			if 0 <= score <= MAX_SCORE:
				scores.append(score)
				break
			else:
				print(f"Please enter a score between 0 and {MAX_SCORE}.")
		except ValueError:
			print("Please enter a valid number for the score.")

print("\nResults:")
for name, score in zip(names, scores):
	status = "Passed" if score >= PASS_MARK else "Failed"
	print(f"{name}: {score:.1f}/{MAX_SCORE} - {status}")