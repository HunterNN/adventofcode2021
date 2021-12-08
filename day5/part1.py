from vector2d import Vector2D

def printGrid(grid):
    print(" ")
    for line in zip(*grid):
        print(line)

def markRoundedPoint(grid, point):
    x = round(point.x)
    y = round(point.y)
    grid[x][y] += 1

def markLine(grid, line):
    v1 = Vector2D(line[0][0], line[0][1])
    v2 = Vector2D(line[1][0], line[1][1])
    direction = v2 - v1
    step = direction.getUnitVector()
    # only vertical and horizontal lines
    if v1.x != v2.x and v1.y != v2.y:
        return
    for i in range(round(v1.distanceTo(v2) / abs(step)) + 1):
        markRoundedPoint(grid, v1)
        v1 += step

with open("input.txt", "r") as f:
    lines = []
    numbers_x = []
    numbers_y = []
    lines_string = f.readlines()
    for line_string in lines_string:
        parts = line_string.split(" -> ")
        parts = list(map(lambda e1: list(map(lambda e2: int(e2), e1.replace("\n", "").split(","))), parts))
        lines.append(parts)
        numbers_x.append(parts[0][0])
        numbers_x.append(parts[1][0])
        numbers_y.append(parts[0][1])
        numbers_y.append(parts[1][1])
    numbers_x.sort(reverse=True)
    numbers_y.sort(reverse=True)
    grid = [ [0] * (numbers_y[0] + 1) for _ in range(numbers_x[0] + 1)]
    for line in lines:
        markLine(grid, line)

    count = 0
    for line in grid:
        for point in line:
            if point > 1:
                count += 1

    printGrid(grid)
    print(count)