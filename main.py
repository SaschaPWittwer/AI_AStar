from grid import Grid
from node import Node

def run(grid, start, goal):
    start_node = Node(None, start)
    goal_node = Node(None, goal)

    open_nodes = []
    closed_nodes = []

    open_nodes.append(start_node)

    while len(open_nodes) > 0:
        node = open_nodes[0]
        node_index = 0

        for index, item in enumerate(open_nodes):
            if item.f < node.f:
                node = item
                node_index = index

        open_nodes.pop(node_index)
        closed_nodes.append(node)

        if node == goal_node:
            path = []
            current = node
            while current is not None:
                path.append(current.position)
                current = current.parent

            # Reverse path
            return path[::-1]

        childs = []
        for new_position in [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),
        ]:
            node_position = (
                node.position[0] + new_position[0],
                node.position[1] + new_position[1],
            )

            # Check grid boundaries
            if (
                node_position[0] > (len(grid) - 1)
                or node_position[0] < 0
                or node_position[1] > (len(grid[len(grid) - 1]) - 1)
                or node_position[1] < 0
            ):
                continue

            # Check that this path is walkable
            if grid[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(node, node_position)
            childs.append(new_node)

        for child in childs:

            # Check if child is already closed
            child_is_closed = False
            for closed_node in closed_nodes:
                if child == closed_node:
                    child_is_closed = True

            if child_is_closed:
                continue

            # Calculate new child value
            child.g = node.g + 1
            child.h = ((child.position[0] - goal_node.position[0]) ** 2) + (
                (child.position[1] - goal_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            # Check if child is open and has a greater distance
            child_is_open_and_further_away = False
            for open_node in open_nodes:
                if child == open_node and child.g > open_node.g:
                    child_is_open_and_further_away = True

            if child_is_open_and_further_away:
                continue

            open_nodes.append(child)

# field [0,1] 
def checkField(grid, row, column):
    if row == 0 and column == 0:
        if grid[row][column][0] == 1 and (grid[row][column][1] == 2 or grid[row][column][2] == 2):
            return True
        elif grid[row][column][3] == 1 and (grid[row][column][1] == 2 or grid[row][column][2] == 2):
            return True
        else:
            return False
    elif row-1 < 0 and column-1 >= 0:
        if grid[row][column][3] == 1 and grid[row][column-1][1] == 2:
            return True
        else:
            return False
    elif row-1 >= 0 and column-1 < 0:
        if grid[row][column][0] == 1 and grid[row-1][column][2] == 2:
            return True
        else:
            return False
    elif (grid[row][column][0] == 1 and grid[row-1][column][2] == 2) or (grid[row][column][3] == 1 and grid[row][column-1][1] == 2):
        return True
    else:
        return False

def rotate(grid, position):
    """
    Rotate a single tile clockwise.
    """
    row = position[0]
    col = position[1]
    grid.nodes[row][col] = Node([
        grid.nodes[row][col].west,
        grid.nodes[row][col].north,
        grid.nodes[row][col].east,
        grid.nodes[row][col].south
    ], grid.nodes[row][col].is_goal)

def depth_search(origin, pos, grid):
    """
    Approach to solve the zenji puzzle with a recursive depth search.
    """
    # check goal state
    #if (pos[0] == grid.size-1 and pos[1] == grid.size-1):
        #return 1
    
    # check borders
    if (pos[0] == grid.size or pos[1] == grid.size):
        print('outside')
        return -1

    node = grid.nodes[pos[0]][pos[1]]

    # rotate max 3 times
    for _i in range(4):
        node = grid.nodes[pos[0]][pos[1]]
        # if water input is at right place
        if node.values[origin] == 1:
            # check goal state
            if node.is_goal == True:
                print('goal')
                return 1
            if node.east == 2:
                # go right
                print('right')
                x = depth_search(3, (pos[0], pos[1]+1), grid)
                if x == 1: return 1
            if node.south == 2:
                # go down
                print('down')
                x = depth_search(0, (pos[0]+1, pos[1]), grid)
                if x == 1: return 1
        else:
            print('rotate')
            rotate(grid, pos)

    # this node is a dead end
    print('dead end' + str(node.values))
    return -1

def main():

    _grid = Grid([
        [[1,2,2,0], [2,1,0,0]],
        [[1,2,1,2], [0,0,1,0]]
    ])

    grid = Grid([
        [[1, 0, 2, 0], [1, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 1, 2], [0, 1, 0, 2], [1, 0, 0, 2], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 2, 0, 0], [0, 2, 0, 1], [0, 0, 0, 1]]
    ])

    grid.print("Initial State")

    # solve the riddle
    solution = depth_search(3, (0,0), grid)
    
    grid.print("Goal State")

    if solution != 1: print('The solution was not found!')

if __name__ == "__main__":
    main()