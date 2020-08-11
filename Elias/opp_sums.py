#consider a function rev which reverses the digits of an integer
#given an array of non negative integers arr, your task is to count the number of pairs 
#(i,j) such that i =< j and arra[i] + rev(arr[j]) = arr[j] + rev(arr[i])

arr = [1,20,2,11] #7

#examples (i,j) = (0,0) equality holds: 1+1 = 1+1

def opp_sums(arr):
    sum = 0
    i = 0
    while i < len(arr):
        for j in range(i, len(arr)):
            if i <= j and arr[i] + rev(arr[j]) == arr[j] + rev(arr[i]):
                sum += 1
        i += 1
    return sum

def rev(num):
    old_num = str(num)
    new_num = ''
    for i in old_num:
        new_num = i + new_num

    return int(new_num)


# def add_ints(num):
#     nums = str(num)
#     return sum([int(char) for char in nums])

# print(add_ints(num))
print(opp_sums(arr))