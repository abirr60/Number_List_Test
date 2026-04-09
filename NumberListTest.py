# CSP1150 Assignment - Student Number List Test
# Author: Abur Mobin
# Student Number: 10714721
#
# Description:
# This program runs a number-list quiz using Easy, Medium, or Hard difficulty.
# It includes the two required functions:
#   1. random_list(quantity, minimum, maximum)
#   2. ask_question(question, answer)
#
# References:
# Python random module documentation:
# https://docs.python.org/3/library/random.html
# Python time module documentation:
# https://docs.python.org/3/library/time.html

import random
import time


def random_list(quantity, minimum, maximum):
    numbers = []

    for _ in range(quantity):
        numbers.append(random.randint(minimum, maximum))

    return numbers

def ask_question(question, answer):

    print(question)

    while True:
        user_input = input("> ")

        try:
            user_answer = int(user_input)
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    if user_answer == answer:
        print("Correct!")
        return True

    print(f"Incorrect! Correct answer was {answer}.")
    return False


# ---------------------------------
# Welcome message and difficulty
# ---------------------------------

print("Welcome to Abur Mobin (10714721) Number List Test!\n")

difficulty = ""

while difficulty not in ("e", "m", "h", "a"):
    difficulty = input(
        "Select a difficulty: [E]asy, [M]edium, [H]ard.\n"
        "> "
    ).strip().lower()

    if difficulty not in ("e", "m", "h", "a"):
        print("Invalid choice! Enter E, M or H.\n")

if difficulty == "a":
    print("Program aborted.")
else:
    # ---------------------------------
    # Difficulty settings
    # ---------------------------------

    if difficulty == "e":
        difficulty_name = "Easy"
        questions = 3
        quantity = 3
        minimum = 1
        maximum = 10

    elif difficulty == "m":
        difficulty_name = "Medium"
        questions = 5
        quantity = 4
        minimum = 5
        maximum = 15

    else:
        difficulty_name = "Hard"
        questions = 7
        quantity = 5
        minimum = 10
        maximum = 20

    print(f"{difficulty_name} difficulty selected!\n")
    print(
        f"Your test will have {questions} questions using lists of "
        f"{quantity} numbers between {minimum} and {maximum}."
    )
    print("The last question is a challenge question with twice as many numbers!\n")

    input("Press Enter to begin!\n")


   # ---------------------------------
    # Start test
    # ---------------------------------

    score = 0
    start_time = time.time()

    for question_number in range(1, questions + 1):
        if question_number == questions:
            print("[!!! Challenge Question !!!]")
            current_list = random_list(quantity * 2, minimum, maximum)
        else:
            current_list = random_list(quantity, minimum, maximum)

        elapsed_time = time.time() - start_time

        print(f"\nQuestion {question_number} of {questions}")
        print(current_list)

        question_type = random.randint(1, 4)

        if question_type == 1:
            correct_answer = sum(current_list)
            question_text = "What is the sum of the numbers in this list?"
            is_correct = ask_question(question_text, correct_answer)

        elif question_type == 2:
            correct_answer = max(current_list) - min(current_list)
            question_text = (
                "What is the difference between the minimum and maximum "
                "numbers in this list?"
            )
            is_correct = ask_question(question_text, correct_answer)

        elif question_type == 3:
            average_floor = sum(current_list) // len(current_list)
            count_higher = 0

            for number in current_list:
                if number > average_floor:
                    count_higher += 1

            question_text = (
                f"How many numbers in this list are higher than {average_floor}?"
            )
            is_correct = ask_question(question_text, count_higher)

        else:
            position_1 = random.randint(1, len(current_list))
            position_2 = random.randint(1, len(current_list))

            while position_2 == position_1:
                position_2 = random.randint(1, len(current_list))

            correct_answer = (
                current_list[position_1 - 1] * current_list[position_2 - 1]
            )

            question_text = (
                f"What is the product of the numbers in positions "
                f"{position_1} and {position_2} in this list?"
            )
            is_correct = ask_question(question_text, correct_answer)

        if is_correct:
            score += 1
        else:
            score -= 1
            if score < 0:
                score = 0


    # ---------------------------------
    # End of test
    # ---------------------------------

    end_time = time.time()
    total_time = end_time - start_time
    average_time = total_time / questions

    print(f"\nTest Complete! You took {total_time:.2f} seconds.")
    print(f"You scored {score}/{questions} question(s) correct.")
    print(f"Average of {average_time:.2f} seconds per question.")

    if score == questions:
        print("Perfect score, well done!")