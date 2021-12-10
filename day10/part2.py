with open("input.txt", "r") as f:
    lines = f.readlines()
    points = {'(' : 1, '[' : 2, '{' : 3, '<' : 4}
    pair = {')' : '(', ']' : '[', '}' : '{', '>': '<'}
    sums = []
    for line in lines:
        sum = 0
        counts = {'(' : 0, '[' : 0, '{' : 0, '<' : 0}
        order = []
        error_line = False
        for part in line.replace("\n", ""):
            if part in counts:
                counts[part] += 1
                order.append(part)
            elif part in pair:
                counts[pair[part]] -= 1
                last = order.pop(-1)
                if last != pair[part]:
                    error_line = True
                    break
        if error_line:
            continue
        order.reverse()
        for part in order:
            sum *= 5
            sum += points[part]
        sums.append(sum)
    sums.sort()
    print(sums[int(len(sums)/2)])