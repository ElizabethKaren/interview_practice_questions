#given an array of strings, for each consecutive 
#pair of workds check
#if they start and end with the same character
#return a boolean array of lenght words where ith element is true if 
#workds[i] and words[i+1] start and end with the same 
#character, false otherwise 

words = ['abcd', 'abdd', 'da', 'dd'] # [true, false, false]
# words = ['a', 'a'] # [true]

def workds_car(words):
    returnArr = []
    for i in range(len(words)-1):
        if words[i][0] == words[i+1][0] and words[i][-1] == words[i + 1][-1]:
            returnArr.append(True)
        else:
            returnArr.append(False)

    return returnArr


print(workds_car(words))