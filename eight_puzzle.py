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

import Puzzle
import re
import search


# 1. Define the Puzzle class: initial_state, successor_fct, goal_test
# 2. Define the Node class: state, parent, depth

default_puzzle = Puzzle.Puzzle([1, 2, 3,
                                       4, 0, 5,
                                       6, 7, 8])

goal = Puzzle.Puzzle([ 1, 2, 3,
                           4, 5, 6,
                           7, 8, 0])

user_puzzle = []

def parse_row(row):
    parsed_row = map(int, re.split(', | ', row))
    for tile in parsed_row:
        user_puzzle.append(tile)
# end def

def generate_puzzle():
    print("    Enter your puzzle, use a zero to represent the blank")

    first_row = raw_input("    Enter the first row, use space or tabs between numbers ")
    parse_row(first_row)

    second_row = raw_input("    Enter the second row, use space or tabs between numbers ")
    parse_row(second_row)

    third_row = raw_input("    Enter the third row, use space or tabs between numbers ")
    parse_row(third_row)

    return Puzzle.Puzzle(user_puzzle)
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

def get_strategy(your_puzzle):
    print("     Enter your choice of algorithm")
    print("     1.  Uniform Cost Search")
    print("     2.  A* with the Misplaced Tile heuristic")
    print("     3.  A* with the Manhattan distance heuristic \n")

    choice = input('         ')
    if not Puzzle.solvable(your_puzzle.initial_state.state):
        print("Puzzle is not solvable")
        exit(0)

    if not(choice > 3) and not(choice < 1):
        return search.general_search(your_puzzle, choice)
    else:
        print("Invalid choice, please try again.")
        return get_strategy()

def main():
    print("Welcome to David Phan's 8-puzzle solver.")
    your_puzzle = get_puzzle()

    search.print_puzzle(your_puzzle.initial_state)
    result, expanded_nodes, max_nodes = get_strategy(your_puzzle)

    print("\n\nGoal!!")
    print("\nTo solve this problem the search algorithm expanded a total number of %d nodes.") % expanded_nodes
    print("The maximum number of nodes in the queue at any one time was %d") % max_nodes
    print("The depth of the goal node was %d") % result.depth

# end main

main()