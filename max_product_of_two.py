#Given the array of integers nums
#you will choose two different indices 
#i and j of that array. Return the maximum
#value of (nums[i]-1)*(nums[j]-1).

nums = [3,4,5,2]
#Output: 12 
#Explanation: If you choose the indices i=1
#and j=2 (indexed from 0), you will get the 
#maximum value, that is, 
#(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

def max_product_of_two(nums):
    largest_num = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            new_sum = (nums[i]-1)*(nums[j]-1)
            if new_sum > largest_num and i != j:
                largest_num = new_sum
    return largest_num


print(max_product_of_two(nums))