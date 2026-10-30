key = ["A", "B", "C", "D", "A"]

correct = 0
incorrect = 0
unanswered = 0

for i in range(5):
    answer = input("Enter answer: ").upper()

    if answer == "":
        unanswered = unanswered + 1
    elif answer == key[i]:
        correct = correct + 1
    else:
        incorrect = incorrect + 1

print("Correct Answers =", correct)
print("Incorrect Answers =", incorrect)
print("Unanswered =", unanswered)

score = correct - incorrect * 0.25

print("Final Score =", score)