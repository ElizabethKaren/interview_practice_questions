array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3]

# array = [3,1,2,3,4,3]

def find_largest_peak(array):
    largest_peak = []
    for num in range(1,len(array)-1):
        if array[num-1] < array[num] and array[num+1] < array[num]:
            new_peak = find_peak(num-1, num, num+1, array)
            if len(new_peak) > len(largest_peak):
                largest_peak = new_peak

    return len(largest_peak)

def find_peak(begining, peak, end, array):
    new_end = end+1
    new_beginning = begining-1
    if end +1 == len(array) or array[end] < array[new_end]:
        new_end = end
    if begining -1 == -1 or array[begining] < array[new_beginning]:
        new_beginning = begining
    if new_end == end and new_beginning == begining:
        return array[begining:end+1]
    return find_peak(new_beginning, peak, new_end, array)
    
    #first time will call find_peak on 2,3,4, array
    #second time call find_peak on 1,3,4, array
    #third time call find_peak on 0,3,4, array
    #third time will return array[0:4]

    #input is find_peak a,b,c, array

    # new_end = array[end+1]
    # if new_end > array[end]:
    #     find_peak(begining, peak, end+1, array)


    # if array[begining-1] < array[peak] and array[end+1] < array[peak]:
    #     return find_peak(begining-1, peak, end+1, array)
    # elif array[begining] < array[peak] and array[end+1] < array[peak]:
    #     return find_peak(begining, peak, end+1, array)
    # elif array[begining-1] < array[peak] and array[end] < array[peak]:
    #     return find_peak(begining -1, peak, end, array)
    # else:
    #     return array[begining:end+1]

print(find_largest_peak(array))