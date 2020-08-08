inputString = 'aabaa'

def checkPalindrome(inputString):
    result = ''
    for letter in inputString:
        result = letter + result 
    
    return result == inputString


print(checkPalindrome(inputString))