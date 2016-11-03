from math import sqrt
from Node import Node

goal = [
          1,2,3,
          4,5,6,
          7,8,0
         ]

# checks if a 3 x 3 puzzle is solvable using number of inversions
def solvable(puzzle):
    inv_cnt = 0

    temp = list(puzzle)
    temp.remove(0)

    for i in range(0, len(temp), 1):
        for j in range(i, len(temp), 1):
            if temp[i] > temp[j]:
                inv_cnt = inv_cnt + 1

    return not(inv_cnt % 2)
# end def

def test_goal(state):
    return 1 if state == goal else 0
# end def

def move_left(state, position):
    if position in [0, 3, 6]:
        return 0
    else:
        child = Node(list(state), state)
        child.swap(position, position-1)
        return child
# end def

def move_right(state, position):
    if position in [2, 5, 8]:
        return 0
    else:
        child = Node(list(state), state)
        child.swap(position, position+1)
        return child
# end def

def move_up(state, position):
    if position in [0, 1, 2]:
        return 0
    else:
        child = Node(list(state), state)
        child.swap(position, position-3)
        return child
# end def

def move_down(state, position):
    if position in [6, 7, 8]:
        return 0
    else:
        child = Node(list(state), state)
        child.swap(position, position+3)
        return child
# end def

class Puzzle:
    def __init__(self, init):
        self.initial_state = Node(init)
        self.actions = [move_left, move_right, move_up, move_down]
        self.goal_test = test_goal
# end class