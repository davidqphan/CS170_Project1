import Puzzle
from heapq import heappop, heappush

def print_puzzle(state):
    for i in range(0, 3):
        print('      '),
        for j in range(0, 3):
            if j < 3:
                print(state[j + 3 * i]),
        if i == 2:
            print("  Expanding this node...")
        else:
            print("")
# end def

def expand(node, actions):
    children = []
    blank = node.state.index(0)

    for action in actions:
        child = action(node, blank)
        if child:
            children.append(child)
    return children
# end def

def general_search(problem, strategy):
    expanded = 0
    queue_size = 0

    if problem.goal_test(problem.initial_state):
        print("\n The puzzle is already solved.\n")
        return problem.initial_state, expanded, queue_size

    nodes = []
    fringe = []

    # push a tuple of cost and the state to the priority queue: nodes
    heappush(nodes,[float('inf'),problem.initial_state])

    while True:
        if not nodes:
            return 0, 0, 0

        queue_size = max(queue_size, len(nodes) )

        # pop the tuple from the priority queue, and store each cost and state to cost, node
        cost, node = heappop(nodes)
        fringe.append(node.state)

        print("The best state to expand with a"),
        if strategy == 1:
            print("g(n) = %d and h(n) = %d is ") % (node.depth, 0)
        elif strategy == 2:
            print("g(n) = %d and h(n) = %d is ") % (node.depth, node.mpt)
        else:
            print("g(n) = %d and h(n) = %d is ") % (node.depth, node.mhd)
        print_puzzle(node.state)

        for child in expand(node, problem.actions):
            if child.state not in fringe:
                if strategy is 1:
                    heappush(nodes, [child.depth, child])
                elif strategy is 2:
                    heappush(nodes, [child.mpt + child.depth, child])
                else:
                    heappush(nodes, [child.mhd + child.depth, child])
                expanded += 1

            if problem.goal_test(child.state):
                return child, expanded, queue_size