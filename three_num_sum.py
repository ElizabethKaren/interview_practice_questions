array = [12,3,1,2,-6,5,-8,6]
target_sum = 0

def threeNumberSum(array, target_sum):
    array.sort()
    newarray = []
    count = 0 
    while count < len(array) - 2:
        cN = array[count]
        left = 0
        right = len(array) - 1
        cS = cN + array[left] + array[right]
        # print(cS)
        if cS == target_sum and array[left] != cN and array[right] != cN and array[left] != array[right]:
            newarray.append([array[right], array[left], cN])
        elif cS < target_sum and left < len(array):
            left += 1 
        elif cS > target_sum and right > -1:
            right -= 1
    count += 1 
        
    return newarray


def three_num_sum_for_loop(array, target_sum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        right = len(array) - 1 
        left = i + 1 
        while left < right: 
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([ array[i], array[left], array[right] ])
                left += 1 
                right += 1 
            elif current_sum > target_sum:
                right -= 1 
            elif current_sum < target_sum:
                left += 1 

    return triplets

print(three_num_sum_for_loop(array,target_sum))