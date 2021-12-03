with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda e1: list(map(lambda e2: int(e2), e1.replace("\n", ""))), lines))
    # * -> https://www.python.org/dev/peps/pep-0448/#id6
    _sum = map(sum, zip(*lines))
    average_rounded = list(map(lambda e: str(round(e / len(lines))), _sum))
    gamma = int(''.join(average_rounded), 2)
    average_rounded_inverted = map(lambda e: "1" if e == "0" else "0", average_rounded)
    epsilon = int(''.join(average_rounded_inverted), 2)
    print(gamma * epsilon)