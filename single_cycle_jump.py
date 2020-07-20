array = [2,3,1,-4,-4,2]

def array_jumps(array):
    count = 0
    for i in range(len(array)):
        num = array[i]
        newNum = i + num 
        print(newNum)


print(array_jumps(array))
