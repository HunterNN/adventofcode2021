from statistics import median

def getLittleGauss(number):
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum

def getDistanceAndFuel(number, position):
    distance = abs(position - number)
    return distance, getLittleGauss(distance)

def getLittleGaussDistanceRatio(numbers, position):
    pre = 0
    sur = 0
    for number in numbers:
        count = 0
        distance, fuel = getDistanceAndFuel(number, position)
        if distance != 0:
            count += fuel
        if number < position:
            pre += count
        else:
            sur += count

    return pre / sur

def doBisection(numbers, min, max):
    position = int((min + max) / 2)
    ratio = getLittleGaussDistanceRatio(numbers, position)
    if min == max:
        return position
    if ratio < 0.5:
        return doBisection(numbers, position, max)
    else:
        return doBisection(numbers, min, position)

with open("input.txt", "r") as f:
    line = f.readlines()
    numbers = list(map(lambda e: int(e), line[0].split(",")))
    numbers.sort()
    last_fuel = -1
    for i in range(numbers[-1]):
        fuel = 0
        for number in numbers:
            fuel += getDistanceAndFuel(number, i)[1]
        if last_fuel > 0 and last_fuel < fuel:
            print(last_fuel)
            break
        last_fuel = fuel
    ## There is an error in getLittleGaussDistanceRatio which doesn't represent the right "median" ratio
    # position = doBisection(numbers, numbers[0], numbers[-1])
    # fuel = 0
    # for number in numbers:
    #     fuel += getDistanceAndFuel(number, position)[1]
    # print(position, fuel)