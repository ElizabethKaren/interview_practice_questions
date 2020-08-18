#balanced strings are those who have qual quantity of L and R characters
#given a balanced string s split it in the maximum amount of balanced strings
#return the max amount of splitted balanced strings 

s = 'RLRRLLRLRL'
#output: 4

#Explanation: s can be split into "RL", "RRLL", "RL", "RL", 
#each substring contains same number of 'L' and 'R'.

def balanced(string):
    num_of_strings = 0
    last_string = string[0]
    for count in range(1, len(string)):
        last_string += string[count]
        if equal_amount(last_string):
            num_of_strings += 1
            
    return num_of_strings 

def equal_amount(string):
    r = 0
    l = 0
    for i in string:
        if i == 'R':
            r += 1
        elif i == 'L':
            l += 1

    return r == l


print(balanced(s))
