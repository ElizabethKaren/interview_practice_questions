# Program to generate a random number between 0 and 9

# importing the random module
import random

def passwordGenerator():
    string = ''
    array = ['a','b','c','d','e','f','g','h','i','j','k','l', 'm', 'n','o','p','2','4','6','7','8','9']
    count = 0
    num = random.randint(8,12)
    while count < num:
        num2 = random.randint(0,len(array)-1)
        string = string + array[num2]
        count += 1 
    return string 


print(passwordGenerator())


