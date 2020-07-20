#there are three types of edits that can be performed on strings 
#insert at character, remove a character, or replace a character
#given two strings write a function to check if they are one edit 
#or zero edits away 

# Remove a character
# At most, one character is different from the original string
# One less character in new string
# len(string1) == len(string2) + 1

string1 = 'pale'
string2 = 'ple' ### true 

# 3 types of edits, but you had one solution, need to break up each
# individual edit

# Replace a character
# pale => bale 
# pale => kyle
# At most, one character is different from the original string
# Both strings have the same length
string5 = 'pale'
string6 = 'kyle' ### true 


# Add a character
# At most, one character is different from the original string
# One more character in new string
# len(string4) == len(string(3)) + 1
string3 = 'pale'
string4 = 'pales'### true 



string7 = 'pale'
string8 = 'bake' ### false 

def one_away(string1, string2):
    if string1 == string2:
        return True
    elif len(string1) == len(string2):
        return replace_a_character_edit(string1, string2)
    elif len(string1) == len(string2) + 1:
        return add_or_subtract_a_character(string2, string1)
    elif len(string2) == len(string1) + 1:
        return add_or_subtract_a_character(string1, string2)
    else:
        return False 


def add_or_subtract_a_character(small, big):
    count = 0
    edit = 0
    while count < len(small):
        if small[count] != big[count] and small[count] != big[count +1]:
            edit += 1
        count += 1 
    return edit == 0

def replace_a_character_edit(string1, string2):
    count = 0
    edit = 0
    while count < len(string1):
        if string1[count] != string2[count]:
            edit += 1
        count += 1 
    return edit == 1



print(one_away(string1, string2))