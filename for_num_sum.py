array = [7,6,4,-1,1,2]
targetSum = 16

def fourNumberSum(array, targetSum):
    new_ar = []
    d = {}
    for num1 in range(len(array)):
        x = array[num1]
        for num2 in range(len(array)):
            if num1 != num2:
                y = array[num2]
                key = targetSum - (abs(x)+abs(y))
                d[key] = [x,y]
        for key1 in d:
            print(key1)
            for key2 in d:
                print(key2)
                if (key1 + key2) == targetSum:
                    inner_ar = [d[key1], d[key2]]
                    new_ar.append(inner_ar)

    return new_ar


print(fourNumberSum(array, targetSum))
		
