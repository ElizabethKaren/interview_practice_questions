#lets define the reverse of an integger 
#as the number obtained by reversing hte order of the digits as X 
#and then moving anuy leanding zeros to the end of the sulting number 
#given an array of integers arr, your takse is to calulate the sum of reverse numbers 
#of the elements of arr 

arr = [7, 234, 58100] #18939
# arr = [0, 100, 220] #320

def reverseArr(arr):
    for i in range(len(arr)):
        new_num = revser_num(arr[i])
        arr[i] = new_num

    return sum(arr)

#100 rev 100

def revser_num(num):
    add_a_zero = ''
    old_num = str(num)
    new_num = ''
    for i in old_num:
        if i == '0':
            add_a_zero += str(0)
        else:
            new_num = i + new_num

    return int(new_num + add_a_zero) 

print(reverseArr(arr))

