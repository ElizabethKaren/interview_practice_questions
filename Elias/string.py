
words = ['cat', 'dog', 'bird', 'car', 'ax', 'baby']
string1 = 'tcabnihjs' #=> cat
string2 = 'tbcanihjs'#=> cat
string3 = 'baykkj1' #=> None
string4 = 'bbabylkkj' #=> baby


def find_word(words, string1):
    possibles = {}
    for word in words:
        for letter in word:
            if letter in string1:
                if word in possibles:
                    possibles[word] += 1
                else:
                    possibles[word] = 1
    
    all_values = possibles.values()
    print(all_values)
    number = max(all_values)
    print(number)

    for key in possibles:
        print(key)
        if possibles[key] == number:
            return key
    
    
    return 'None'


print(find_word(words,string3))