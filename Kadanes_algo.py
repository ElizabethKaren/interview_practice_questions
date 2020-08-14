#write a function that takes a non empty array of integers
#and returns the maximum sum that can be obtained by 
#summing up all of the integers in a non empty
#subarray fo the input array. a subarray must
#only contain adgacent numbers 


array = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
#19


def kadanes_algo(array):
    max_ending_here = array[0]
    max_so_far = array[0]
    for i in range(1,len(array)):
        num = array[i]
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


print(kadanes_algo(array))