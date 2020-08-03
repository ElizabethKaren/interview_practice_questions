# # array = [2,2,1]
# # Output: 1
# # Example 2:

# array = [4,1,2,1,2]
# # Output: 4

# def single_num(array):
#     for index in range(len(array)):
#         num = array[index]
#         arr = array[:index] + array[index+1:]
#         if num not in arr:
#             return num

# array = [2,2,3,2]
# Output: 3

array = [0,1,0,1,0,1,99]
# Output: 99

def single_num(array):
    d = {}
    for num in array:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    for key in d:
        if d[key] == 1:
            return key



print(single_num(array))