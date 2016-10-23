"""
    Name : David Phan
    Email : dphan015@ucr.edu
    Class : CS170
    Project : 1

    Exercise Description : Eight Puzzle AI

    This program will solve the Eight Puzzle using:

    - Uniform Cost Search
    - A* with the Misplaced Tile heuristic
    - A* with the Manhattan Distance heuristic

    I acknowledge all content contained herein, excluding template or example
    code, is my own original work.
"""

from Puzzle import Puzzle
import sys
import re

# 1. Define the Puzzle class: initial_state, successor_fct, goal_test
# 2. Define the Node class: state, parent, depth

default_puzzle = Puzzle([1, 2, 3,
                              4, 0, 5,
                              6, 7, 8])
user_puzzle = []

def parse_row(row):
    parsed_row = map(int, re.split(', | ', row))
    for tile in parsed_row:
        user_puzzle.append(tile)
# end def

def generate_puzzle():
    print("Enter your puzzle, use a zero to represent the blank")

    first_row = input("Enter the first row, use space or tabs between numbers ")
    parse_row(first_row)

    second_row = input("Enter the second row, use space or tabs between numbers ")
    parse_row(second_row)

    third_row = input("Enter the third row, use space or tabs between numbers ")
    parse_row(third_row)

    return Puzzle(user_puzzle)
# end def

def get_puzzle():
    print("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle.")

    user_input = input()

    if user_input == 1:
        return default_puzzle
    elif user_input == 2:
        return generate_puzzle()
    else:
        print("Puzzle is invalid, please try again.")
        return get_puzzle()
# end def


def main():
    print("Welcome to David Phan's 8-puzzle solver.")

    user_puzzle = get_puzzle()
# end main

