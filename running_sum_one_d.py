# nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running 
# sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 
def running_sum(array):
    sum = 0
    for num in range(len(array)):
        sum += nums[num]
        nums[num] = sum

    return array


print(running_sum(nums))