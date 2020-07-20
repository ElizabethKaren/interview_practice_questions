array = [9,4,2,6,8,1,10]

def bubbleSort(array):
    index = 0 
    while index < len(array) -1:
        for count in range(index + 1, len(array)):
            if array[count] < array[index]:
                swap(count, index, array)
                index = 0
            else:
                index +=1 
    return array 


def swap(i, j, array):
	array[i], array[j] = array[j], array[i]


print(bubbleSort(array))
