def enhance(sequence, pairs):
    new_sequence = []
    for seq in sequence:
        if seq[0] in pairs:
            new_sequence.append([seq[0][0]+pairs[seq[0]], seq[1]])
            new_sequence.append([pairs[seq[0]]+seq[0][1], seq[1]])
        else:
            new_sequence.append(seq)

    return new_sequence

def calculate(sequence):
    letter_counts = {}
    for i in range(ord('A'), ord('Z') + 1):
        letter_counts[chr(i)] = 0
    for i in range(ord('A'), ord('Z') + 1):
        for part in sequence:
            if chr(i) in part[0]:
                letter_counts[chr(i)] += part[1]
    print(letter_counts)
    letter_counts.sort(key=lambda e: e[1])
    value = letter_counts[-1][1] - letter_counts[0][1]
    return value

def createSequenceFromString(string):
    sequence = []
    for i in range(len(string) - 1):
        sequence.append([string[i:i+2], 1])
    return sequence

def shrinkSequence(sequence):
    new_sequence = []
    sequence.sort(key=lambda e: e[0])
    for i in range(len(sequence) - 1):
        if sequence[i][0] != sequence[i + 1][0]:
            new_sequence.append(sequence[i])
        else:
            sequence[i + 1][1] +=  sequence[i][1]
        
    return new_sequence

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
    
    sequence = createSequenceFromString(sequence)
    for i in range(10):
        sequence = enhance(sequence, pairs)
        sequence = shrinkSequence(sequence)

    print(sequence)
    # for i in range(3):
    #     print(i)
    #     sequence = enhance(sequence, pairs)
    
    print(calculate(sequence))