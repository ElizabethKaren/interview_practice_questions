# Given an array nums of n integers 
#where n > 1,  return an array output such that output[i] 
#is equal to the product of all the elements of nums except 
#nums[i].

nums = [1,2,3,4]
# Output: [24,12,8,6]


def product(nums):
    return_arr = []
    product = 1
    for num in nums:
        product = product * num
    
    for num in nums:
        new_num = product/num
        return_arr.append(int(new_num))
    
    return return_arr



print(product(nums))