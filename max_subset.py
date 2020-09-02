#write a function that takes an array of positive integers
#and returns the max sum of non adjacent elements in
#the array if the sum cant be generated, the function
#should return zero

array = [75, 105, 120,75,90, 135]

#output 330 

#so confused
def max_subset_sum_no_adjacent(array):
    sum = 0
    for index in range(len(array)-1):
        if array[index] > array[index+1]:
            sum += array[index]
            sum -= array[index-1]
        else:
            sum += array[index+1]
    
    return sum


print(max_subset_sum_no_adjacent(array))