smallest_count = -1

def printGrid(grid):
    for line in grid:
        for number in line:
            if number >= 0:
                print(" " + str(number), end="")
            else:
                print(str(number), end="")
        print("")
    print("")

def isPossibleMove(grid, x, y, direction):
    if direction == "up":
        return y > 0
    if direction == "down":
        return y < len(grid) - 1
    if direction == "right":
        return x < len(grid[0]) - 1
    if direction == "left":
        return x > 0

def move(grid, x, y, count):
    global smallest_count
    count += grid[y][x][0]
    distance = len(grid) - y + len(grid[0]) - x
    if count > smallest_count - distance:
        return
    if y == len(grid) - 1 and x == len(grid[0]) - 1:
        smallest_count = count
        print(count)
        return
    if grid[y][x][1] > 0:
        count += grid[y][x][1]
        if smallest_count == -1 or count < smallest_count:
            smallest_count = count
            print(count)
        return
    else:
        if isPossibleMove(grid, x, y, "down"):
            move(grid, x, y + 1, count)
        if isPossibleMove(grid, x, y, "right"):
            move(grid, x + 1, y, count)
        # Those aren't needed. See explanation at the bottom.
        # if isPossibleMove(grid, x, y, "up"):
        #     move(grid, x, y - 1, count)
        # if isPossibleMove(grid, x, y, "left"):
        #     move(grid, x - 1, y, count)

with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid_line = []
        for number in line.replace("\n", ""):
            grid_line.append([int(number), 0])
        grid.append(grid_line)

    for y in range(len(grid) - 1, -1, -1):
        for x in range(len(grid[0]) - 1, -1, -1):
            if x == len(grid[0]) - 1 and y == len(grid) - 1:
                continue
            smallest_count = (len(grid[0]) - x + len(grid) - y) * 9
            move(grid, x, y, 0 - grid[y][x][0])
            grid[y][x][1] = smallest_count
    print(grid[0][0][1] - grid[0][0][0])

# Sub squars from the end to the beginning:

# 1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521 <-
# 2311944581 <-

# 81

# 1
# 1

# 21  <- The path on number 2 has to go right or down, because all other paths lead again to the 1, 8 or 2
# 81