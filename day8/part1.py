def getNumberPattern(part):
    pattern = [0] * 10
    part = part.split(" ")
    part = list(map(lambda e: ''.join(sorted(list(e))), part))
    part.sort(key=lambda e: len(e))
    pattern[1] = part[0]
    pattern[4] = part[2]
    pattern[7] = part[1]
    pattern[8] = part[9]
    # 2, 3, 5 -> 5
    # 0, 6, 9 -> 6
    return pattern

def countNumberWithPattern(pattern, part):
    count = 0
    part = part.replace("\n", "")
    part = part.split(" ")
    part = list(map(lambda e: ''.join(sorted(list(e))), part))
    part.sort(key=lambda e: len(e))
    for p in part:
        if p in pattern:
            count += 1
    return count

with open("input.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        parts = line.split(" | ")
        pattern = getNumberPattern(parts[0])
        count += countNumberWithPattern(pattern, parts[1])
    print(count)