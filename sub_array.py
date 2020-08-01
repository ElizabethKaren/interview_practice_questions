#given an array of positive numbers and positive number 'k'
#find the max sum of any contiguous subarray of size 'k'

array = [2,1,5,1,3,2] #max sum is [5,1,3]
k = 3

array2 = [2,3,4,1,5] #max sum is [3,4]
y = 2 

def max_sum_sub_array(array,k):
    max_sum = 0 
    sub_array = []
    for num in array:
        new_array = count_sub_array(array[num:], k)
        if new_array.sum() > max_sum:
            sub_array = new_array
            max_sum = new_array.sum()

    return sub_array

def count_sub_array(array, k):
    print(array)



print(max_sum_sub_array(array,k))