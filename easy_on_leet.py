# Given a string s and an integer array indices of the same length.
# The string s will be shuffled such that the character 
#at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

def shuffle_string(s, indices):
    arr = [char for char in s]
    index = 0
    while index < len(indices)-1:
        if indices[index] > indices[index+1]:
            indices[index], indices[index+1] = indices[index+1], indices[index]
            arr[index], arr[index +1] = arr[index+1], arr[index]
            index = 0
        else:
            index += 1

    return ''.join(arr)






print(shuffle_string(s,indices))
 