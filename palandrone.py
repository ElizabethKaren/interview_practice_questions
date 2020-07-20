string1 = 'waterbottle'
string2 = 'erbottlewat'

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

def is_rotation(string1, string2):
    d1 = create_diction(string1)
    d2 = create_diction(string2)
    count = 0
    while count < len(d1):
        if d1[count] != d2[count]:
            return False  
        count += 1 
    return True

    

def create_diction(string):
    d = []
    for letter in string:
        d.append(letter)
    
    d.sort()
    return d
    

def isSubstring(string1, string2):
    sub_string = ''
    for letter in string2:
        for letter2 in string1:
            if letter2 == letter:
                sub_string += letter2

    return len(sub_string) >= len(string2)



print(is_rotation(string1,string2))