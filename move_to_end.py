array = [2,1,2,2,2,3,4,5,6,2]
to_move = 2 

def move_to_end(array,to_move):
    j = len(array) - 1
    i = 0
    while i < len(array) - j and j > i:
        if array[j] == to_move:
            j -= 1
        if array[i] == to_move:
            swap(i, j, array)
            i += 1 
            j -= 1
            
        else:
            i += 1

    return array


def swap(i,j,array):
    array[i], array[j] = array[j], array[i]



print(move_to_end(array,to_move))