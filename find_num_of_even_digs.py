#Given an array nums of integers, return how 
#many of them contain an even number of digits.

nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

def find_num_even_digs(nums):
    how_many = 0
    for num in nums:
        the_num = str(num)
        if len(the_num) % 2 == 0:
            how_many += 1 
            
    return how_many


print(find_num_even_digs(nums))