array = [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first two elements after removing the duplicates will be [2, 11].

def remove_dups(array):
    index = 0 
    for fast_index in range(len(array)):
        if array[index] != array[fast_index]:
            array[index+1] = array[fast_index]
            index +=1 

    return index + 1


print(remove_dups(array))