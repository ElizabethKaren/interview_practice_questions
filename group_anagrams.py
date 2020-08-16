#wite a function that akes in an array of strings and groups anagrams together
#anagrams are strings made up of exactly same letters, where order
#doesnt matter. For example. 'cinema' and 'iceman' are anagrams; 
#similarly "foo" and "ofo" are anagrams. your function should
#return a list of anagram groups in no particular order

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

def group_anagrams(words):
    return_array = []
    for i in words:
        word = sorted(i)
        sub_array = [i]
        for y in words:
            if i != y:
                word2 = sorted(y)
                if word == word2:
                    sub_array.append(y)
        return_array.append(sub_array)
        
    return return_array


print(group_anagrams(words))