# Given an array of integers nums.
# A pair (i,j) is called good if 
#nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

nums = [1,2,3]
# Output: 0

def num_of_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i > j and nums[i] == nums[j]:
                count += 1
    return count


print(num_of_pairs(nums))