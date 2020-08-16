#wite a function that akes in an array of strings and groups anagrams together
#anagrams are strings made up of exactly same letters, where order
#doesnt matter. For example. 'cinema' and 'iceman' are anagrams; 
#similarly "foo" and "ofo" are anagrams. your function should
#return a list of anagram groups in no particular order

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

def group_anagrams(words):
    return_array = []
    right = 0
    left = len(words)-1
    while left > right:
        sub_array = [words[right]]
        if words[left][0] in words[right][0]:
            sub_array.append(words[left])
            left =- 1
        else:
            return_array.append(sub_array)
            right += 1 
            left = len(words)-1
        
    return return_array


print(group_anagrams(words))