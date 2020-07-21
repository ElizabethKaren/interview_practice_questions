array = [2,3,1,-4,-4,2]

## NOT SOLVED

def array_jumps(array):
    clone_array = []
    for i in array:
        if i == len(array) -1:
            i = -1
        num = array[i]
        print(num)
        newIndex = i + num 
        clone_array.append(newIndex)


    return clone_array


print(array_jumps(array)) 
