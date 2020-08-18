#balanced strings are those who have qual quantity of L and R characters
#given a balanced string s split it in the maximum amount of balanced strings
#return the max amount of splitted balanced strings 

s = 'RLRRLLRLRL'
#output: 4

#Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
#each substring contains same number of 'L' and 'R'.

def balanced(string):
    count = 0
    for index in range(len(string)-1):
        i = string[index]
        y = string[index + 1]
        if i != y:
            pass 
        else:
            count += 1
    
    return count 


print(balanced(s))
