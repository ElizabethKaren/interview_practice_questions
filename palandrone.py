string = 'grapefruit'

def isPalindrome(string):
    newString = ''
    for i in reversed(range(len(string))):
        newString += string[i]

    return newString

print(isPalindrome(string))