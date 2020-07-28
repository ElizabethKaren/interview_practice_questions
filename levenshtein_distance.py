#write a function that takes two strings and returns
#the minimum number of edit operations
#that need to be performed on the first string
#to obtain the second string
#there are three operations: insertion of char,
#deletion of char, and subsitution of char for another.

str1= 'abc'
str2 = 'yabd'

def levenshtein_distance(str1,str2):
    sum = 0
    if len(str1) == len(str2):
        return possible_substitution_of_char(str1, str2, sum)
    elif len(str1) > len(str2):
        return deletion_or_substitution_of_char(str1,str2, sum)
    elif len(str2) > len(str1):
        return deletion_or_substitution_of_char(str2,str1, sum)


def possible_substitution_of_char(str1,str2, sum):
    count = 0
    while count < len(str1):
        if str1[count] != str2[count]:
            sum += 1 
        count += 1 
    return sum

def deletion_or_substitution_of_char(big,little, sum):
    for letter in big:
        for letter2 in little:
            if letter != letter2:
                sum += 1 
    return sum


print(levenshtein_distance(str1,str2))