#given two non empty arrays of integers, write a function that determines 
#whether the second array is a subsequence of the first 
array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]

def validate(array,sequence):
    count = 0
    sequence_count = 0
    while count < len(array):
        if array[count] == sequence[sequence_count]:
            sequence_count += 1
        count += 1

    return sequence_count == len(sequence)



print(validate(array, sequence))