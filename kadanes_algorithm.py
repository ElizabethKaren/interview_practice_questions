#write a function that takes a non empty array of integers and returns the max
#sum that can be obstained bu summing all of the integers in a non 
#empty subarray of the input array. subarray must only contain 
# adjacent numbers

array = [3,5,-9,1,3-2,3,4,7,2,-9,6,3,1,-5,4]

def kadanes_algorithm(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for i in range(1, len(array)):
        num = array[i]
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far



print(kadanes_algorithm(array))