#there are three types of edits that can be performed on strings 
#insert at character, remove a character, or replace a character
#given two strings write a function to check if they are one edit 
#or zero edits away 

string1 = 'pale'
string2 = 'ple' ### true 

string3 = 'pales'
string4 = 'pale' ### true 

string5 = 'pale'
string6 = 'bale' ### true 

string7 = 'pale'
string8 = 'bake' ### false 

def one_away(string1, string2):
    return string1 + string2


print(one_away(string1, string2))