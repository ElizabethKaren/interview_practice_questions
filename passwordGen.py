# Program to generate a random number between 0 and 9

# importing the random module
import random

def passwordGenerator():
    string = ''
    characters = ['a','b','c','d','e','f','g','!' ,'@','$','%','k','l', 'm', 'n','o','p','2','4','6','7','8','9', 'Q', 'R', 'S','T','U','V','W','X','Y', 'Z']
    length = random.randint(8,12)
    for count in range(length):
        randomChar = random.randint(0,len(characters)-1)
        string += characters[randomChar]

    return string 


print(passwordGenerator())

