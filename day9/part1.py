def printGrid(grid):
    for line in grid:
        for number in line:
            print(number, end="")
        print("")

def flow(grid, position):
    x, y = position
    neightbors = []
    if x < len(grid[0]) - 1:
        neightbors.append(grid[y][x + 1])
    else:
        neightbors.append([10, 0])
    if x > 0:
        neightbors.append(grid[y][x - 1])
    else:
        neightbors.append([10, 0])
    if y < len(grid) - 1:
        neightbors.append(grid[y + 1][x])
    else:
        neightbors.append([10, 0])
    if y > 0:
        neightbors.append(grid[y - 1][x])
    else:
        neightbors.append([10, 0])

    smallest = sorted(neightbors, key=lambda e: e[0])[0]
    if smallest > grid[y][x]:
        return position

    i = neightbors.index(sorted(neightbors)[0])
    if i == 0:
        new_position = x + 1, y
    if i == 1:
        new_position = x - 1, y
    if i == 2:
        new_position = x, y + 1
    if i == 3:
        new_position = x, y - 1
    return flow(grid, new_position)

with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid_line = []
        for number in line.replace("\n", ""):
            number = int(number)
            grid_line.append([number, 0])
        grid.append(grid_line)
    for y, line in enumerate(grid):
        for x, part in enumerate(line):
            xl, yl = flow(grid, [x, y])
            grid[yl][xl][1] += 1

    count = 0
    for y, line in enumerate(grid):
        for x, part in enumerate(line):
            if grid[y][x][1] > 0:
                count += 1 + grid[y][x][0] 
    printGrid(grid)
    print(count)