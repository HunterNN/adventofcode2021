with open("input1.txt", "r") as f:
    lines = f.readlines()
    count = 0
    lines = list(map(lambda e: int(e), lines))
    for i in range(len(lines) - 3):
        sum1 = lines[i] + lines[i+1] + lines[i+2]
        sum2 = lines[i+1] + lines[i+2] + lines[i+3]
        if sum2 > sum1:
            count = count + 1
        
    print(count)