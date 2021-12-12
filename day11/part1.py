def printGrid(grid):
    for line in grid:
        for number in line:
            if number >= 0:
                print(" " + str(number), end="")
            else:
                print(str(number), end="")
        print("")
    print("")

def increaseField(grid, x, y):
    if grid[y][x] != -1: 
        grid[y][x] += 1 

def flash(grid):
    for y, line in enumerate(grid):
        for x, part in enumerate(line):
                increaseField(grid, x, y)
    flashed = True
    while flashed:
        flashed = False
        for y, line in enumerate(grid):
            for x, part in enumerate(line):
                    if grid[y][x] > 9:
                        flashed = True
                        grid[y][x] = -1
                        if y > 0:
                            increaseField(grid, x, y - 1)
                            if x > 0:
                                increaseField(grid, x - 1, y - 1)
                            if x < len(grid[0]) - 1:
                                increaseField(grid, x + 1, y - 1)
                        if y < len(grid) - 1:
                            increaseField(grid, x, y + 1)
                            if x > 0:
                                increaseField(grid, x - 1, y + 1)
                            if x < len(grid[0]) - 1:
                                increaseField(grid, x + 1, y + 1)
                        if x > 0:
                            increaseField(grid, x - 1, y)
                        if x < len(grid[0]) - 1:
                            increaseField(grid, x + 1, y)
    count = 0
    for y, line in enumerate(grid):
        for x, part in enumerate(line):
                if grid[y][x] == -1:
                    grid[y][x] = 0
                    count += 1
    return count


with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append(list(map(lambda e: int(e), line.replace("\n", ""))))
    count = 0
    for i in range(100):
        count += flash(grid)
        # print("Step: ", i + 1)      
        # printGrid(grid)
    print(count)