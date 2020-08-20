# Given an array nums of n integers 
#where n > 1,  return an array output such that output[i] 
#is equal to the product of all the elements of nums except 
#nums[i].

# nums = [1,2,3,4]
# Output: [24,12,8,6]
nums = [0,0]


def product(nums):
    return_arr = []
    for num in nums:
        new = helper_method(num, nums)
        return_arr.append(new)
       
    return return_arr

def helper_method(num, nums):
    product = 1
    for i in nums:
        if i != num:
            product = product * i

    return product 


print(product(nums))