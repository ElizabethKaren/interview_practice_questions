sequence = [1, 3, 2, 1] #false


def almostIncreasingSequence(sequence):
    c = 0
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]: c += 1
        if i+2 < len(sequence) and sequence[i] >= sequence[i+2]: c += 1
    return c < 3



print(almostIncreasingSequence(sequence))