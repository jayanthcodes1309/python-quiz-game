# Python quiz

questions = ("What is the biggest dinosour?: ",
             "Name of the galaxy we live in?:",
             "How many elements are in the periodic table?: ",
             "Which is the Indian national animal?:",
             "how many alphabets are there in english?:",
             "what are endangered species?:")

options = (("A. Terx", "B. Rhino", "C. Plato", "D. Gyro "),
           ("A. Galaxy-191", "B. blueway galaxy", "C. milkiway galaxy", "D. gaurdians of galaxy"),
           ("A. 112", "B. 145", "C. 118", "D. 115"),
           ("A. Peacock", "B. Tiger", "C. Lion", "D.There is no national animal."),
           ("A. 32", "B. 28", "C. 24", "D. 26"),
           ("A. Animals which live now", "B. Animals which got extinct", "C. Animals which eat grass", "D. Animals which eat Other animals"))

answers = ("A", "C", "C", "D", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
 
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("-----------------------")
print("        RESULT         ")
print("-----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"You got {score}%. ")