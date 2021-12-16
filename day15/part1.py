from rich import print

smallest_count = -1
smallest_position = None

def printGrid(grid):
    next = [0,0]
    count = 0
    for i, line in enumerate(grid):
        for j, number in enumerate(line):
            space = " " * (3 - len(str(number[0])+str(number[1])))
            if i == next[1] and j == next[0]:
                if len(grid[i][j]) > 2:
                    next = grid[i][j][2]
                print(f"[red]{str(number[0])}[/red][gray]({str(number[1])})[/gray]{space}", end="")
            else:
                print(f"{str(number[0])}[gray]({str(number[1])})[/gray]{space}", end="")
            #     print(f"[red]{str(number[0])}[/red]", end="")
            #     count += number[0]
            # else:
            #     print(f"{str(number[0])}[gray]", end="")
        print("")
    print("")
    print(count)

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
    global smallest_count, smallest_position
    count += grid[y][x][0]
    if count > smallest_count:
        return False
    if y == len(grid) - 1 and x == len(grid[0]) - 1:
        smallest_count = count
        smallest_position = [x, y]
        return True
    if grid[y][x][1] > 0:
        count += grid[y][x][1]
        if count < smallest_count:
            smallest_count = count
            smallest_position = [x, y]
        return True
    result_1 = False
    result_2 = False
    if isPossibleMove(grid, x, y, "down"):
        result_1 = move(grid, x, y + 1, count)
    if isPossibleMove(grid, x, y, "right"):
        result_2 = move(grid, x + 1, y, count)
    return result_1 or result_2

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
            worst_case = (len(grid[0]) - x + len(grid) - y) * 9
            smallest_count = worst_case
            if move(grid, x, y, 0 - grid[y][x][0]):
                grid[y][x][1] = smallest_count
                grid[y][x].append(smallest_position)
            else:
                grid[y][x][1] = worst_case
    print(grid[0][0][1])
    printGrid(grid)