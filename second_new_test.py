#write a function that takes in an array of integers 
#and returns the length of the longest peak in the array 
#a peak is defined as adjacent integers in the array 
#that are strickly increasing until they reach a tip (the highest 
# value in the peak), at which point they become stricktly decreasing. 
#At least three integers are required to form a peak

array = [5, 4, 3, 2, 1, 2, 10, 12]


def longest_peak(array):
    key = 0
    peaks = {key: []}
    last_num = 0
    for num in array:
        if num >= last_num:
            peaks[key].append(num)
            last_num = num
        else:
            peaks[key].append(num)
            key += 1 
            peaks[key] = [num]
            last_num = num
    peaks[key] = []
    largest_key = []
    for key in peaks:
        if len(peaks[key]) > len(largest_key):
            largest_key = peaks[key]

    if len(largest_key) < 3:
        return 0
    return largest_key


print(longest_peak(array))