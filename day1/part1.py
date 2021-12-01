with open("input1.txt", "r") as f:
    lines = f.readlines()
    last_value = -1
    count = 0
    for line in lines:
        line = int(line)
        if last_value == -1:
            last_value = line
            continue
        if line > last_value:
            count = count + 1

        last_value = line
        
    print(count)