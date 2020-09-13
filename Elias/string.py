words = ['cat', 'dog', 'bird', 'car', 'ax', 'baby']
string1 = 'tcabnihjs' #=> cat
string2 = 'tbcanihjs'#=> cat
string3 = 'baykkj1' #=> None
string4 = 'bbabylkkj' #=> baby


def find_word(words,string):

    string_dictionary = {}
    for letter in string:
        if letter in string_dictionary:
            string_dictionary[letter] += 1
        else:
            string_dictionary[letter] = 1

    for word in words:
        dictionary_new = dict(string_dictionary)
        return_string = ''
        for letter in word:
            if letter in dictionary_new:
                return_string += letter 
                dictionary_new[letter] =- 1
                if dictionary_new[letter] == 0:
                    del dictionary_new[letter]
            if return_string in words:
                return return_string
    
    return None


print(find_word(words,string3))

# def find_word(words, string):
#     possibles = {}
#     for word in words:
#         string1 = str(string)
#         for letter in string1:
#             if letter in word:
#                 string1 = string1.replace(letter, "")
#                 if word in possibles:
#                     possibles[word] += 1
#                 else:
#                     possibles[word] = 1
    
#     all_values = possibles.values()
#     number = max(all_values)

#     for key in possibles:
#         if possibles[key] == number and len(key) == number:
#             return key
    
#     return 'None'

