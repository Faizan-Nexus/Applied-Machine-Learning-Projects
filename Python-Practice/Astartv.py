from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

# Heuristic function: calculates the Manhattan distance between two cells
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

# A* search algorithm to find the shortest path in the maze
def aStar(m):
    start = (m.rows, m.cols)  # Start at the bottom-right corner
    goal = (1,1)              # Goal is at the top-left corner
    open_set = PriorityQueue()  # Priority queue to select the next cell to explore
    open_set.put((0, start))    # Add the start cell with priority 0

    # Initialize the cost from start to every cell as infinity
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0  # Cost to reach start is 0

    # Estimated total cost from start to goal through each cell
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, goal)  # Heuristic estimate for start

    came_from = {}  # To reconstruct the path

    while not open_set.empty():
        current = open_set.get()[1]  # Get the cell with the lowest f_score

        if current == goal:  # If goal is reached, stop searching
            break

        # Explore neighbors in all four directions
        for d in 'ESNW':
            if m.maze_map[current][d] == 1:  # If path exists in this direction
                if d == 'E':
                    neighbor = (current[0], current[1]+1)
                if d == 'W':
                    neighbor = (current[0], current[1]-1)
                if d == 'N':
                    neighbor = (current[0]-1, current[1])
                if d == 'S':
                    neighbor = (current[0]+1, current[1])

                temp_g_score = g_score[current] + 1  # Cost to reach neighbor

                # If this path to neighbor is better, record it
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor))

    # Reconstruct the path from goal to start
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[came_from[cell]] = cell
        cell = came_from[cell]
    return fwdPath

if __name__ == '__main__':
    m = maze(8)  # Create a 5x5 maze
    m.CreateMaze()  # Generate the maze layout
    path = aStar(m)  # Find the shortest path using A*
    a = agent(m, footprints=True, color=COLOR.blue)  # Create an agent to follow the path
    m.tracePath({a: path})  # Show the path in the maze
    l1 = textLabel(m,"A* Search path", len(path))
    m.run()  # Run the maze animation
