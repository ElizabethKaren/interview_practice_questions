array = [7,10,12,7,9,14]

def max_subset_sum_no_adjacent(array):
    d = {}
    higest_num = 0
    for i in range(len(array)-1):
        num = find_highest_num(array[i], array[i-2], array[i-4])
        d[num] = [array[i], array[i-2], array[i-4]]

    for key in d:
        if key > higest_num:
            higest_num = key

    return higest_num


def find_highest_num(num1, num2=0, num3=0):
    sum = num1 + num2 + num3 
    return sum


print(max_subset_sum_no_adjacent(array))