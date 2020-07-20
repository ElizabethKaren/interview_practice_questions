# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. (can you do this in place?)
# Hints: #51, #100
​
# 3 arr, append
#r0, c0 => r0, c2 /// chg = +0r, +2c
#r0, c1 => r1, c2 /// chg = +1r, +1c
#r0, c2 => r2, c2 /// chg = +2r, +0c
#r1, c0 => r0, c1 /// chg = -1r, +1c
#r1, c1 => r1, c1 /// chg = +0r, +0c
#r1, c2 => r2, c1 /// chg = +1r, -1c
#r2, c0 => r0, c0 /// chg = -2r, +0c
#r2, c1 => r1, c0 /// chg = -1r, -1c
#r2, c2 => r2, c0 /// chg = +0r, -2c
​
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
​
rotated_90_matrix = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
​
​
return_matrix = []
for orig_col in range(len(matrix)):
    print(list(range(len(matrix))))
    column = orig_col
    new_row = []
    row = len(matrix) - 1
    while row > -1:
       num =  matrix[row][column]
       new_row.append(num)
       row -= 1
    return_matrix.append(new_row)
​
print(return_matrix)
​
​
# def rotate_90_degrees(matrix):
#     ret_matrix = []
#     for row in matrix:
#         ret_matrix.append([0] * len(row))
#     print(ret_matrix)
#     for i in range(len(matrix)):
#         row = matrix[i]
#         # for j in row:
#     print(len(matrix))
#     print(len(matrix[0]))
#
# rotate_90_degrees(matrix)
