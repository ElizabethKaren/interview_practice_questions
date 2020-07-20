# array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
array = [2,4,1,8]

def isMonotonic(array):
    first = 0
    last = len(array) - 1
    if abs(array[first]) > abs(array[last]):
        for i in range(len(array)-1):
            if abs(array[i]) < abs(array[i + 1]):
                return False
    elif abs(array[first]) < abs(array[last]):
        for i in range(len(array)-1):
            if abs(array[i]) > abs(array[i + 1]):
                return False  
    else:
        return False
    return True


print(isMonotonic(array))
