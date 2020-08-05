#Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is 
# equal to the product of all the elements of nums except nums[i].

array = [1,2,3,4]
# Output: [24,12,8,6]

# def product_except_self(array):
#     total = 1
#     for num in array:
#         total = total * num

#     for index in range(len(array)):
#         new_num = total/array[index]
#         array[index] = int(new_num)

#     return array

def product_except_self(array):
    return_array = []
    for index in range(len(array)):
        new_arr = array[:index] + array[index+1:]
        num = helper(new_arr)
        return_array.append(num)

    return return_array


def helper(new_arr):
    print(array)
    total = 1
    for num in new_arr:
        total = total * num

    return total


print(product_except_self(array))