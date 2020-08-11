# For text = "Hello, this is CodeSignal!" and letters = ['e', 'i', 'h', 'l', 'o', 's']
#the output should be brokenKeyboard(text, letters) = 2.

letters = ['e', 'i', 'h', 'l', 'o', 's']
text = "Hello, this is CodeSignal!"

def broken_keyboard(letter, text):
    num_of_words = 0
    text_array = text.split(' ')
    for word in text_array:
        for letter in word:
            print(letter)
            num_of_letters = 0
            if letter in letters or letter in ['!',',','?','.']:
                num_of_letters += 1
                if num_of_letters == len(word)-1:
                    num_of_words += 1

    return num_of_words


print(broken_keyboard(letters, text))

