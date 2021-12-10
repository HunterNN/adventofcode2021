with open("input.txt", "r") as f:
    lines = f.readlines()
    points = {'(' : 3, '[' : 57, '{' : 1197, '<' : 25137}
    pair = {')' : '(', ']' : '[', '}' : '{', '>': '<'}
    sum = 0
    for line in lines:
        counts = {'(' : 0, '[' : 0, '{' : 0, '<' : 0}
        order = []
        for part in line.replace("\n", ""):
            if part in counts:
                counts[part] += 1
                order.append(part)
            elif part in pair:
                counts[pair[part]] -= 1
                last = order.pop(-1)
                if last != pair[part]:
                    sum += points[pair[part]]
                    break
    print(sum)