#Given the array nums, for each nums[i] find out 
#how many numbers in the array are smaller than it. 
#That is, for each nums[i] you have to count the number 
#of valid j's such that j != i and nums[j] < nums[i].
#Return the answer in an array.

nums = [8,1,2,2,3]
#Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

def how_many_smaller(nums):
    output_array = []
    for index in range(len(nums)):
        num = nums[index]
        new_arr = nums[:index] + nums[index+1:]
        new_num = rest_of_nums(new_arr, num)
        output_array.append(new_num)

    return output_array

def rest_of_nums(arr, num):
    count = 0
    for i in arr:
        if i < num:
            count += 1 
    
    return count 


print(how_many_smaller(nums))