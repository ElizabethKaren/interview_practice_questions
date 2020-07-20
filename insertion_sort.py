array = [8,5,2,9,5,6,3]

def insertion_sort(array):
    count = 0
    while count < len(array) -1:
        if array[count] > array[count+1]:
            swap(count+1, count,array)
            count = 0
        else:
            count += 1 

    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]


print(insertion_sort(array))