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

# north east south west
def rotateRight(grid, row, column):
    grid[row][column] = [grid[row][column][3],grid[row][column][0],grid[row][column][1],grid[row][column][2]]


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

def printGrid(grid):
    # Build visual output 0 = block, 1 = in, 2 = out
    for row in grid:
        print("-------  -------  -------  -------")
        north = ""
        eastWest = ""
        south =""
        for j, col in enumerate(row):
            north += "|  " + str(col[0]) + "  |  "
        for j, col in enumerate(row):
            eastWest += "| " + str(col[3]) + " " + str(col[1]) + " |  "
        for j, col in enumerate(row):
            south += "|  " + str(col[2]) + "  |  "
        print(north)
        print(eastWest)
        print(south)
        print("-------  -------  -------  -------")



def main():

    grid = [
        [[1, 2, 0, 0], [1, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 0, 2], [1, 0, 0, 2], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [1, 2, 0, 0], [0, 2, 0, 1], [0, 0, 0, 1]],
    ]
    printGrid(grid)
    start = (0, 0)
    end = (9, 9)
    count = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            for y in range(4):
                if(checkField(grid, i, j) == True):
                    break
                else:
                    count += 1
                    if (col[0] + col[1] + col[2] + col[3]) >= 3:
                        rotateRight(grid, i, j)
                    else:
                        break
    print(count)

    printGrid(grid)




    #path = run(grid, start, end)

  

if __name__ == "__main__":
    main()
