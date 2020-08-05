#Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is 
# equal to the product of all the elements of nums except nums[i].

array = [1,2,3,4]
# Output: [24,12,8,6]

def product_except_self(array):
    total = sum(array)
    for index in range(len(array)):
        new_num = total - array[index]
        array[index] = new_num

    return array


print(product_except_self(array))