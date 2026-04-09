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
