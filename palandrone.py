string1 = 'elizabeth'
string2 = 'liz'

def isPalindrome(string):
    d = {}
    for letter in string:
        if letter in d.keys():
            d[letter] += 1
        else:
            d[letter] = 1
    
    for key in d:
        if d[key] % 2 == 0:
            return True
    
    return False

def isSubstring(string1, string2):


print(isSubstring(string1,string2))