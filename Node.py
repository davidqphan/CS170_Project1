goal = [
          1, 2, 3,
          4, 5, 6,
          7, 8, 0
         ]

# misplaced tile heuristic: add 1 for each misplaced tile
def misplaced_tile(state):
    misplaced_cnt = 0

    for i in range(0, 9, 1):
        if state[i] != goal[i]:
            misplaced_cnt = misplaced_cnt + 1
    return misplaced_cnt
# end def

# manhattan distance heuristic: dist b/t 2 points measured along axes
# at right angles
def manhattan_dist(state):
    mhd = 0
    for i in range(0, 9, 1):
        state_pos = state.index(i)
        goal_pos = goal.index(i)
        if state_pos == goal_pos:
            continue

        elif state_pos in range(0, 3, 1):
            if goal_pos in range(0, 3, 1):
                mhd += abs(state_pos - goal_pos)
            elif goal_pos in range(3, 6, 1):
                state_pos += 3
                mhd += abs(state_pos - goal_pos) + 1
            else:
                state_pos += 6
                mhd += abs(state_pos - goal_pos) + 2
        elif state_pos in range(3, 6, 1):
            if goal_pos in range(3, 6, 1):
                mhd += abs(state_pos - goal_pos)
            elif goal_pos in range(0, 3, 1):
                state_pos -= 3
                mhd += abs(state_pos - goal_pos) + 1
            else:
                state_pos += 3
                mhd += abs(state_pos - goal_pos) + 1
        elif state_pos in range(6, 9, 1):
            if goal_pos in range(6, 9, 1):
                mhd += abs(state_pos - goal_pos)
            elif goal_pos in range(3, 6, 1):
                state_pos -= 3
                mhd += abs(state_pos - goal_pos) + 1
            else:
                state_pos -= 6
                mhd += abs(state_pos - goal_pos) + 2
    return mhd
# end def

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.mpt = misplaced_tile(state)
        self.mhd = manhattan_dist(state)

        if parent is None:
            self.parent = None
            self.depth = 0
        else:
            self.state = state
            self.parent = parent
            self.depth = self.parent.depth + 1

    def __getitem__(self, item):
        return self.state[item]

    def __index__(self, item):
        return self.state.index(item)

    def swap(self, x, y):
        self.state[x], self.state[y] = self.state[y], self.state[x]
# end class