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


def main():

    grid = [
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    ]

    start = (0, 0)
    end = (9, 9)

    path = run(grid, start, end)

    # Build visual output
    output = ""
    for i, row in enumerate(grid):
        if i > 0:
            output += "\n"
        for j, col in enumerate(row):
            if any(step[0] == i and step[1] == j for step in path):
                output += "X "
            else:
                output += str(col) + " "

    print(output)


if __name__ == "__main__":
    main()
