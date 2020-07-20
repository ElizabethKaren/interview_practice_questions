#given a string write a function to check if it is a permutation of a palindrome


input = 'Tact Coa' ##true
input2 = 'eloxi'

#o(n)
def is_palindrome_permutation(input):
    dictionary = {}
    for i in range(len(input)):
        key = input[i]
        if key == ' ':
            pass
        elif key in dictionary.keys():
            dictionary[key] += 1 
        else:
            dictionary[key] = 1

    for key in dictionary:
        if dictionary[key] % 2 == 0:
            return True
    
    return False



print(is_palindrome_permutation(input2))