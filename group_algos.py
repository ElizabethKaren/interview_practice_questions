words = ['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp']

word = 'atc'


def group_algorithms(words):
    if len(words) == 0:
        return []
    return_array = []
    for word in words:
        word_array = find_matching_word(word, words)
        if word_array != None:
            return_array.append(word_array)

    return return_array

def find_matching_word(word, words):
    first_dictionary = create_dictionary(word)
    for searching_word in words:
        if searching_word == word:
            return None
        second_dictionary = create_dictionary(searching_word)
        if len(second_dictionary) == len(first_dictionary):
            count = 0
            while count < len(first_dictionary):
                words_match = True
                if first_dictionary[count] != second_dictionary[count]:
                    words_match = False
                count += 1
                if words_match:
                    return [searching_word, word]

        

def create_dictionary(word):
    d = []
    for letter in word:
        d.append(letter)
    d.sort()
    return d



print(group_algorithms(words))