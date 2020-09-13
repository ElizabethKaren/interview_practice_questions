words = ['cat', 'dog', 'bird', 'car', 'ax', 'baby']
string1 = 'tcabnihjs' #=> cat
string2 = 'tbcanihjs'#=> cat
string3 = 'baykkj1' #=> None
string4 = 'bbabylkkj' #=> baby


def find_word(words, string):
    possibles = {}
    for word in words:
        string1 = str(string)
        for letter in string1:
            if letter in word:
                string1 = string1.replace(letter, "")
                if word in possibles:
                    possibles[word] += 1
                else:
                    possibles[word] = 1
    
    all_values = possibles.values()
    number = max(all_values)
    print(number)

    for key in possibles:
        if possibles[key] == number and len(key) == number:
            return key
    
    return 'None'


print(find_word(words,string3))