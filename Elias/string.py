#you are running a classroom and suspect that some of your students
#are passing around the answers to multiple choice questions disguised
#as random strings

#your task is to write a function that, given a list of words and string
#finds and returns the word in the list that is scrambled up inside the string
#if any exitst There will be at most one matching word
#the letters dont need to be contigous

words = ['cat', 'dog', 'bird', 'car', 'ax', 'baby']
string1 = 'tcabnihjs'


def find_word(words, string1):
    possibles = {}
    for word in words:
        for letter in word:
            if letter in string1:
                if word in possibles:
                    possibles[word] += 1
                else:
                    possibles[word] = 1

    return possibles 


print(find_word(words,string1))