def enhance(sequence, pairs, counts):
    new_sequence = []
    for seq in sequence:
        if seq[0] in pairs:
            new_sequence.append([seq[0][0]+pairs[seq[0]], seq[1]])
            new_sequence.append([pairs[seq[0]]+seq[0][1], seq[1]])
            counts[pairs[seq[0]]] += seq[1]
        else:
            new_sequence.append(seq)

    return new_sequence

def calculate(counts):

    s = sorted(list(counts.items()), key=lambda e: e[1])
    count = []
    for pair in s:
        if pair[1] > 0:
            count.append(pair)
    print(count)
    value = count[-1][1] - count[0][1]
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

        if i == len(sequence) - 2:
            new_sequence.append(sequence[-1])
        
    return new_sequence

with open("input.txt", 'r') as f:
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
    letter_counts = {}
    for i in range(ord('A'), ord('Z') + 1):
        letter_counts[chr(i)] = 0
    
    for i in sequence:
        letter_counts[i] +=1

    sequence = createSequenceFromString(sequence)
    for i in range(40):
        sequence = enhance(sequence, pairs, letter_counts)
        sequence = shrinkSequence(sequence)

    print(sequence)
    print(calculate(letter_counts))