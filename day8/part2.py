def substractLetters(string, letters):
    string = list(string)
    for letter in letters:
        string.remove(letter)
    return ''.join(string)

def isLettersInString(letters, string):
    for letter in letters:
        if not letter in string:
            return False
    return True

def getNumberPattern(part):
    pattern = [0] * 10
    part = part.split(" ")
    part = list(map(lambda e: ''.join(sorted(list(e))), part))
    part.sort(key=lambda e: len(e))
    pattern[1] = part[0]
    pattern[4] = part[2]
    pattern[7] = part[1]
    pattern[8] = part[9]
    part.remove(pattern[1])
    part.remove(pattern[4])
    part.remove(pattern[7])
    part.remove(pattern[8])
    # 2, 3, 5 -> 5
    # finding 3
    for p in part:
        if len(p) == 5 and isLettersInString(pattern[1], p):
            pattern[3] = p
            part.remove(pattern[3])
            break
    # 0, 6, 9 -> 6
    # finding 9
    for p in part:
        if len(p) == 6 and isLettersInString(pattern[4], p):
            pattern[9] = p
            part.remove(pattern[9])
            break
    # finding 0
    for p in part:
        if len(p) == 6 and isLettersInString(pattern[1], p):
            pattern[0] = p
            part.remove(pattern[0])
            break
    # finding 6
    for p in part:
        if len(p) == 6:
            pattern[6] = p
            part.remove(pattern[6])
            break
    # finding 2
    two_pattern = substractLetters(pattern[8], pattern[6])
    for p in part:
        if len(p) == 5 and isLettersInString(two_pattern, p):
            pattern[2] = p
            part.remove(pattern[2])
            break
    # finding 5
    pattern[5] = part[0]
    return pattern

def getNumberWithPattern(pattern, part):
    part = part.replace("\n", "")
    part = part.split(" ")
    part = list(map(lambda e: ''.join(sorted(list(e))), part))
    number = 0
    for p in part:
        number *= 10
        number += pattern.index(p)
    return number

with open("input.txt", "r") as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        parts = line.split(" | ")
        pattern = getNumberPattern(parts[0])
        count += getNumberWithPattern(pattern, parts[1])
    print(count)