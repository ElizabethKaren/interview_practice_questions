string = 'axyzzyxf'

def isPlal(string):
    return_string = ''
    firstIndex = 0 
    lastIndex = len(string) - 1 
    while firstIndex < lastIndex:
        if string[firstIndex] == string[lastIndex]:
            return_string = string[firstIndex] + return_string + string[lastIndex]
        firstIndex += 1 
        lastIndex -= 1
    return return_string

def longest_pal_sub_w_lam(string):
    current_longest = [0,1]
    for i in range(1, len(string)):
        odd = getLongestPalendromeFrom(string, i -1, i+1)
        even = getLongestPalendromeFrom(string, i-1, i)
        longest = max(odd, even, key = lambda x: x[1] - x[0])
        current_longest = max(longest, current_longest, key = lambda x: x[1]-x[0])
    return string[current_longest[0]: current_longest[1]]


def getLongestPalendromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx +1 , rightIdx]
    


def longest_pal_jumbled(string):
    new_string = ''
    dictionary = {}
    for letter in string:
        if letter in dictionary.keys():
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    for key in dictionary:
            times = int(dictionary[key] / 2)
            for i in range(times):
                new_string += key
                new_string = key + new_string

    return new_string


def longest_pal_sub(string):
    longest = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i : j +1]
            if len(substring) > len(longest) and isPalandrome(substring):
                longest = substring
    return longest

def isPalandrome(string):
    leftIndx = 0
    rightIdx = len(string)-1
    while leftIndx < rightIdx:
        if string[leftIndx] != string[rightIdx]:
            return False
        leftIndx += 1
        rightIdx -= 1
    return True


print(longest_pal_sub(string))
