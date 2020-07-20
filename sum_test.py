#write a function that takes in an array of positive integers 
#and returns the maximum sum of non-adjacent elements in the array
#if sum cant be generated the function should return 0 

array = [75, 105, 120, 75, 90, 135]


def max_sum_not_adjacent(array):
    max_sum_of_odd = 0 
    max_sum_of_even = 0 
    count = 0 
    while count < len(array):
        if count % 2 == 0:
           max_sum_of_even += array[count]
           count += 1 
        else:
            max_sum_of_odd += array[count]
            count += 1 
    
    if max_sum_of_even > max_sum_of_odd:
        return max_sum_of_even
    else:
        return max_sum_of_odd



print(max_sum_not_adjacent(array))