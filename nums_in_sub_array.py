#find hte average of all contigous subarrays of 
#size 5 in the given array
#lets solve this 

array = [1,3,2,6,-1,4,1,8,2]
k = 5 
#output [2.2, 2.8, 2.4, 3.6, 2.8]

def subarrays_divided_by_k(array,k):
    return_array = []
    for num in range(len(array)-(k-1)):
        new_num = plus_and_divided_by_k(array[num:],k)
        return_array.append(new_num)

    return return_array

def plus_and_divided_by_k(array,k):
    return_num = 0
    count = 0 
    while count < k:
        return_num += array[count]
        count += 1

    return return_num/k

print(subarrays_divided_by_k(array,k))