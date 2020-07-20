string1 = 'elizabkienji'
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
    sub_string = ''
    for letter in string2:
        for letter2 in string1:
            if letter2 == letter:
                sub_string += letter2

    return len(sub_string) >= len(string2)



print(isSubstring(string1,string2))