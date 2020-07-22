array = [3,5-4,8,11,1,-1,6]
target_sum = 10

def two_nums_n_squared(array,target_sum):
    dictionary = {}
    for num in array:
        y = target_sum - num
        dictionary[y] = num
        if num in dictionary.keys():
            return [num, y]
    
    return []


def two_nums(array,target_sum):
    array.sort()
    left = 0
    right = len(array)-1
    while right > left:
        currentSum = array[right] + array[left]
        if currentSum == target_sum:
            return [array[right], array[left]]
        elif currentSum < target_sum:
            left += 1 
        elif currentSum > target_sum:
            right -= 1
    return []





print(two_nums(array,target_sum))