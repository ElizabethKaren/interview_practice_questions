array = [2, 3, 4, 1, 5]
K = 2

def max_sum_subarray(arr, K):
    windowStart, windowSum = 0, 0.0
    maxSum = 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K-1:
            maxSum = max(windowSum, maxSum)
            windowSum -= arr[windowStart]
            windowStart +=1

    return maxSum


print(max_sum_subarray(array, K))