from node import Node

class Grid:
    """
    Represents the Grid to play the zenji game on it. The size stands for
    the number of rows and cols, nodes is an array of tiles.
    """
    def __init__(self, nodes=[]):
        self.size = len(nodes)
        self.nodes = []

        # add Nodes to the Grid
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Node(nodes[i][j]))
            self.nodes.append(row)
        
        # define goal state
        self.nodes[self.size-1][self.size-1].is_goal = True
            
    def print(self, title=""):
        """
        Prints the current Grid to the console.
        """
        print("\n" + title + ":\n")
        for row in self.nodes:
            output = ""
            print("-------  -------  -------  -------")
            for _j, node in enumerate(row):
                output += "|  " + str(node.north) + "  |  "
            output += '\n'
            for _j, node in enumerate(row):
                output += "|" + str(node.west) + "   " + str(node.east) + "|  "
            output += '\n'
            for _j, node in enumerate(row):
                output += "|  " + str(node.south) + "  |  "
            print(output)
            print("-------  -------  -------  -------")
