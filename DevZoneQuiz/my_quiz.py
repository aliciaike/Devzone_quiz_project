import time
print("WELCOME TO DEVZONE PYTHON QUIZ:\n"
      "PROJECT BY: ALICIA IKE\n"
      "NOTE: Timer is set to '30 SEC' for Quiz ")
time.sleep(3)
def quiz_game():
    timer_duration = 30

    questions = [
        {
            "Question": "2. Which type of Programming does Python support?",
            "Choices": ["a. object-oriented programming ", "b. structured programming","c. functional programming ", "d. all of the mentioned",
                        ],
            "Correct_answer": "d"
        },
        {
            "Question": "Which of the following is the correct extension of the Python file?",
            "Choices": ["a. .python", "b. .pl ", "c. .p ", "d. .py"],
            "Correct_answer": "d"
        },
        {
            "Question": " Which of the following is used to define a block of code in Python language?",
            "Choices": ["a. Indentation", "b. Key ", "c. Brackets", "d. None"],
            "Correct_answer": "a"
        }
        ,
        {
            "Question": " Which of the following character is used to give single-line comments in Python?",
            "Choices": ["a. // ", "b. /* ", "c. # ", "d. !"],
            "Correct_answer": "c"
        },
        {
            "Question": "What is the order of precedence in python?",
            "Choices": ["a. Exponential, Parentheses, Multiplication, Division, Addition, Subtraction",
                        "b. Exponential, Parentheses, Division, Multiplication, Addition, Subtraction ",
                        "c. Parentheses, Exponential, Multiplication, Division, Subtraction, Addition",
                        "d. Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
            "Correct_answer": "d"
        },
        {
            "Question": " What does pip stand for python?",
            "Choices": ["a.Pip Installs Python",
                        "b.Pip Installs Packages",
                        "c.Preferred Installer Program ",
                        "d.None of the above"],
            "Correct_answer": "c"
        }
    ]


    score = 0
    start_time = time.time()

    for i, question in enumerate(questions):
        print("Question", i+1, ":", question["Question"])
        for choice in question["Choices"]:
            print(choice)
        user_answer = input("Your answer: Enter (a , b , c, or d ) >>> ")

        if user_answer.lower() == question["Correct_answer"]:
            score += 1

        elapsed_time = time.time() - start_time
        if elapsed_time >= timer_duration:
            print("Your Time's up!")
            break


    print("QUIZ ENDED!")
    print(f"YOU SCORED: {score} OUT OF 6 WELL DONE")
    print("THANK YOU FOR PLAYING")


quiz_game()
