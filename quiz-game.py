# Python Quiz Game

# A tuple containing each question
questions = (
    "What is the capital of France: ",
    "Which planet is known as the Red Planet: ",
    "Who wrote the play Romeo and Juliet: ",
    "How many continents are there on Earth: ",
    "Which ocean is the largest: ",
)

# 2d tuple containing options to the questions
options = (
    ("a. Berlin", "b. Madrid", "c. Paris", "d. Rome"),
    ("a. Venus", "b. Mars", "c. Jupiter", "d. Saturn"),
    (
        "a. William Wordsmith",
        "b. William Shakespeare",
        "c. Charles Dickens",
        "d. Jane Austen",
    ),
    ("a. 5", "b. 6", "c. 7", "d. 8"),
    ("a. Atlantic Ocean", "b. Indian Ocean", "c. Artic Ocean", "d. Pacific Ocean"),
)

# A tuple that contains the answers to each question
answers = ("c", "b", "b", "c", "d")
# an empty list to hold user input
guesses = []
# a variable to display the score
score = 0
# a variable to get the question number
question_num = 0

# a for loop that iterates over the questions and displays each one
for question in questions:
    print()
    print(question)
    # a nested for loop that iterates over each set of options and displays them according to index num
    for option in options[question_num]:
        print()
        print(option)

    # increment operator for the question num
    question_num += 1

    # allows user to choose an option for each question
    guess = input("Enter (a, b, c, d): ").lower()
    # adds options to empty list
    guesses.append(guess)
    # if statement to check if user input is the same as the answer
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer")

# for loop to print each answer
print("     RESULTS     ")
print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

# equation to calculate the score percentage
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
