# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

def sorted_squares(arr):
    n = len(arr)
    squares = []

    for i in range(n):
        squares.append(0)

    highestIdx = n-1
    left, right = 0, n-1

    while left < right:
        left_sq = arr[left] * arr[left]
        right_sq = arr[right] * arr[right]
        if left_sq > right_sq:
            squares[highestIdx] = left_sq
            left += 1
        else:
            squares[highestIdx] = right_sq
            right -= 1
        highestIdx -= 1
        
    return squares


print(sorted_squares([-2, -1, 0, 2, 3]))