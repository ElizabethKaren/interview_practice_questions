#given a non empty string of lowercase letters and 
#non negative integer representing a key, write a function
#that returns a new string obtained by shifting ever
#letter in the input string by k positions in the 
#alphabet, where k is key

string = 'xyz'
key = 2

def ceaser_cipher_encriptor(string,key):
    new_letters = []
    new_key = key % 26
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))
    return "".join(new_letters)


def get_new_letter(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code % 26]


print(ceaser_cipher_encriptor(string,key))
