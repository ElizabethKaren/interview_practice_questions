array = [0,1,21,33,45,45,61,71,72,73]
target_num = 33

def binary_search(array, target_sum):
    left = 0 
    right = len(array)-1
    while left <= right:
        middle = (left+right)//2
        num = array[middle]
        if num == target_num:
            return middle
        elif num > target_num:
            right = middle -1
        elif num < target_num:
            left = middle + 1
    return -1

    



print(binary_search(array, target_num))