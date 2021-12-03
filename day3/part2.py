def average_rounded(lines):
    _sum = map(sum, zip(*lines))
    # https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior
    return list(map(lambda e: round((e / len(lines)) + 0.00001), _sum))

def clean(lines, most):
    i = 0
    _lines = list(lines)
    while len(_lines) > 1:
        average = average_rounded(_lines)
        if most:
            _lines = list(filter(lambda e: e[i] == average[i], _lines))
        else: 
            _lines = list(filter(lambda e: e[i] != average[i], _lines))
        i += 1
    return _lines

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda e1: list(map(lambda e2: int(e2), e1.replace("\n", ""))), lines))
    # * -> https://www.python.org/dev/peps/pep-0448/#id6
    oxygen_bin = list(map(lambda e: str(e), *clean(lines, True)))
    co2_bin = list(map(lambda e: str(e), *clean(lines, False)))
    oxygen = int(''.join(oxygen_bin), 2)
    co2 = int(''.join(co2_bin), 2)
    print(oxygen, co2, oxygen * co2)
