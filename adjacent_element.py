inputArray = [3, 6, -2, -5, 7, 3]

def adjacentElementsProduct(inputArray):
    largest_num = 0
    for num in range(len(inputArray)-1):
        new_sum = inputArray[num] * inputArray[num +1]
        if new_sum > largest_num:
            largest_num = new_sum
    
    return largest_num


print(adjacentElementsProduct(inputArray))