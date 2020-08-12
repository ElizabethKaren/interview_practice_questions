# Given an array of integers arr, and three integers a, b 
#and c. You need to find the number of good triplets.
# A triplet (arr[i], arr[j], arr[k]) is good if the 
#following conditions are true:
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
# Return the number of good triplets.

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
# Output: 4
# Explanation: There are 4 good 
#triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

def count_good_triplets(arr,a,b,c):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j, len(arr)):
                if arr[i] - arr[j] <= a and arr[j] - arr[k] <= b and arr[i] - arr[k] <= c:
                    count += 1
    return count 

print(count_good_triplets(arr, a,b,c))