statues = [6, 2, 3, 8]
#solution 3

def makeArrayConsecutive2(statues):
    statues.sort()
    return_num = 0
    for num in range(len(statues)-1):
        difference = statues[num] - statues[num+1]
        if difference != 1:
            return_num += abs(difference) - 1
            
    return return_num


print(makeArrayConsecutive2(statues))