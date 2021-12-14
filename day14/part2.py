def enhance(sequence, pairs):
    new_sequence = sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i:i+2] in pairs:
            new_sequence += pairs[sequence[i:i+2]] + sequence[i+1]

    return new_sequence

def calculate(sequence):
    letter_counts = []
    for i in range(ord('A'), ord('Z') + 1):
        if chr(i) in sequence:
            count = sequence.count(chr(i))
            letter_counts.append([chr(i), count])
    letter_counts.sort(key=lambda e: e[1])
    value = letter_counts[-1][1] - letter_counts[0][1]
    return value


with open("test.txt", 'r') as f:
    lines = f.readlines()
    sequence = ""
    pairs = {}
    for i, line in enumerate(lines):
        line = line.replace("\n", "")
        if i == 0:
            sequence = line
        else:
            if "->" in line:
                parts = line.split(" -> ")
                pairs[parts[0]] = parts[1]
    
    for i in range(40):
        print(i)
        sequence = enhance(sequence, pairs)
    
    print(calculate(sequence))