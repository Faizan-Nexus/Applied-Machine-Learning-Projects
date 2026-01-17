from pyamaze import maze

m= maze(5,5)
m.CreateMaze()

print(m.rows)
print(m.cols)

print(m.maze_map)

print(m.grid)

m.run()


def heuristic(cell1, cell2):
    x1,y1 = cell1
    x2,y2 = cell2
    
    return abs(x1-x2) - abs(y1-y2)


