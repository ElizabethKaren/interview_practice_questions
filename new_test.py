#write a function that takes in two nonempty arrays of integers 
#find the pair of numbers (one from each array)
#whose absolute difference is closest to zero 
#return an array containining these two numbers 
#the number from the first array in the first position 

array_one = [-1, 5,10,20,28,3]

array_two = [26,134,135,15,17]

#O(n2)
def smallest_difference(array_one, array_two):
    differnce_counter = {}
    for num1 in array_one:
        for num2 in array_two:
                num = abs(num1 - num2)
                differnce_counter[num] = [num1, num2]
    
    min = 999999
    for difference in differnce_counter:
        if difference < min:
            min = difference
        
    return differnce_counter[min]

#have a pointer for each array
#compare two elements at pointer 
#incriment pointer on smaller element 

#nlogn + nlogn + n + n 
def more_eph(array_one, array_two):
    array_one.sort()
    array_two.sort()
    i = 0 
    j = 0
    minimum = 99999
    min_elements = []
    while i < len(array_one) and j < len(array_two):
        elemnt1 = array_one[i]
        elemnt2 = array_two[j]
        difference = abs(elemnt1 - elemnt2)
        if difference < minimum:
            minimum = difference
            min_elements = [elemnt1, elemnt2]
        if elemnt1 < elemnt2:
            i += 1
        else: 
            j += 1

    return min_elements

# [4, 15, 26]
# [-3, 25, 300]
        


print(more_eph(array_one, array_two))