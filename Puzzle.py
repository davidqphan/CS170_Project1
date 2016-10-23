from math import sqrt
from Node import Node

move_cost = 1

goal = [
          1,2,3,
          4,5,6,
          7,8,0
         ]

def test_goal(state):
    return 1 if state == goal else 0
# end def

def move_left(state, pos):
    # TODO
# end def

def move_right(state, pos):
    # TODO
# end def

def move_up(state, pos):
    # TODO
# end def

def move_down(state, pos):
    # TODO
# end def

class Puzzle(object):
    def __init__(self,initial_state):
        self.initial_state = Node(initial_state)
        self.actions = [move_left, move_right, move_up, move_down]
        self.goal_test = test_goal
    # end def
# end class