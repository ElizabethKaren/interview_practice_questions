array = [3,5-4,8,11,1,-1,6]
target_sum = 10

def two_nums(array,target_sum):
    dictionary = {}
    for num in array:
        y = target_sum - num
        dictionary[y] = num
        if num in dictionary.keys():
            return [num, y]
    
    return []






print(two_nums(array,target_sum))