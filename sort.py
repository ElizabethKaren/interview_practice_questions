array = [8,5,2,9,5,6,3]

def selectionSort(array):
    count = 0
    while count < len(array) - 1:
        smallestIndx = count
        for i in range(count +1, len(array)):
            if array[smallestIndx] > array[i]:
                smallestIndx = i
        swap(count, smallestIndx, array)
        count += 1 
    return array

def swap(j,i,array):
	array[i], array[j] = array[j], array[i]


print(selectionSort(array))