class Node:
    """
    A node represents a tile in the zenji game. Each direction can have
    an entry (1) or an exit (2). There exists a single node on the grid,
    which is the goal state. The position is represented by a tuple.
    """
    def __init__(self, state=[], is_goal=False):
        self.values = state
        self.north = state[0]
        self.east  = state[1]
        self.south = state[2]
        self.west  = state[3]
        self.is_goal = is_goal
    