depth = 0
horizontal = 0
aim = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        value = int(line.split(" ")[-1])
        if "forward" in line:
            horizontal += value
            depth += aim * value
        elif "up" in line:
            aim -= value
        elif "down" in line:
            aim += value
    print(depth*horizontal)