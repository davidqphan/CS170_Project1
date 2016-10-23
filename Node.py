class Node(object):
    def __init__(self, state, parent=None):
        self.state = state
        # TODO: misplaced tile
        # TODO: manhattan

        if parent is None:
            self.parent = None
            self.depth = 0
        else:
            self.state = state
            self.parent = parent
            self.depth = (self.parent).depth+1
    # end def

    def __index__(self, item):
        return (self.state).index(item)
    # end def

    def __getitem__(self, item):
        return self.state[item]
    # end def

    def swap(self, x, y):
        self.state[x] = self.state[y]
        self.state[y] = self.state[x]
    # end def
# end class
