depth = 0
horizontal = 0
with open("input.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        value = int(line.split(" ")[-1])
        if "forward" in line:
            horizontal += value
        elif "up" in line:
            depth -= value
        elif "down" in line:
            depth += value
    print(depth*horizontal)