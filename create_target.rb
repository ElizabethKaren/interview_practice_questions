#Given two arrays of integers nums and index. 
#Your task is to create target array under the 
#following rules:
#Initially target array is empty.
#From left to right read nums[i] and index[i], 
#insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read 
#in nums and index. Return the target array.
#It is guaranteed that the insertion operations will be valid.

# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
#Output: [0,4,1,3,2]

nums = [1,2,3,4,0]
index = [0,1,2,3,0]
#output: [0,1,2,3,4]

def create_target(nums,index)
    return_arr = []
    nums.each do |i|
        if return_arr.size < index[i]
            return_arr << nums[i]
        else
            return_arr.insert(index[i], nums[i])
        end
        p return_arr
    end
    p return_arr
end 


create_target(nums,index)