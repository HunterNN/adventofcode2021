from statistics import median

with open("input.txt", "r") as f:
    line = f.readlines()
    numbers = list(map(lambda e: int(e), line[0].split(",")))
    median_number = median(numbers)
    sum = 0
    for number in numbers:
        sum += abs(median_number - number)
    print(sum)