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