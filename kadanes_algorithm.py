#write a function that takes a non empty array of integers and returns the max
#sum that can be obstained bu summing all of the integers in a non 
#empty subarray of the input array. subarray must only contain 
# adjacent numbers

array = [3,5,-9,1,3-2,3,4,7,2,-9,6,3,1,-5,4]

def kadanes_algorithm(array):
    total = 0
    new_total = 0
    for num in array:
        new_total = total + num
        if new_total > total:
            total = new_total
    return total



print(kadanes_algorithm(array))