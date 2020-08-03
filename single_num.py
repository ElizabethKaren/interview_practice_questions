# array = [2,2,1]
# Output: 1
# Example 2:

array = [4,1,2,1,2]
# Output: 4

def single_num(array):
    for index in range(len(array)):
        num = array[index]
        arr = array[:index] + array[index+1:]
        if num in arr:
            pass 
        else:
            return num



print(single_num(array))