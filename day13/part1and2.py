def printGrid(grid):
    for line in grid:
        for number in line:
            print(number, end="")
        print("")
    print("")

def fold(grid, fold):
    new_grid = []
    if fold[1]:
        length_x = fold[0]
        for y in range(len(grid)):
            grid_line = []
            for x in range(length_x):
                if grid[y][x] == '#' or (length_x * 2 - x) < len(grid[0]) and grid[y][length_x * 2 - x] == '#':
                    grid_line.append('#')
                else:
                    grid_line.append('.')
            new_grid.append(grid_line)
    else:
        length_y = fold[0]
        for y in range(length_y):
            grid_line = []
            for x in range(len(grid[0])):
                if grid[y][x] == '#' or (length_y * 2 - y) < len(grid) and grid[length_y * 2 - y][x] == '#':
                    grid_line.append('#')
                else:
                    grid_line.append('.')
            new_grid.append(grid_line)
    return new_grid


with open("input.txt", "r") as f:
    lines = f.readlines()
    numbers = []
    folds = []
    for line in lines:
        if "," in line:
            parts = line.replace("\n", "").split(",")
            parts = list(map(lambda e: int(e), parts))
            numbers.append(parts)
        if "fold" in line:
            parts = line.replace("\n", "").split("=")
            folds.append([int(parts[1]), "x" in parts[0]])

    length_x = sorted(numbers, key=lambda e: e[0], reverse=True)[0][0] + 1
    lenght_y = sorted(numbers, key=lambda e: e[1], reverse=True)[0][1] + 1
    
    grid = []
    for line in range(lenght_y):
        grid_line = []
        for part in range(length_x):
            grid_line.append('.')
        grid.append(grid_line)

    for pair in numbers:
        grid[pair[1]][pair[0]] = '#'

    print(folds[0])
    for fol in folds:
        grid = fold(grid, fol)
        count = 0
        for i in grid:
            for j in i:
                if j ==  '#':
                    count += 1
        print(count)

    printGrid(grid)

