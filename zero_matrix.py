matrix = [
    [10, 0, 13, 21, 22, 23],
    [14, 15, 16, 24, 25, 26],
    [17, 18, 19, 0, 27, 29],
    [37, 38, 39, 40, 47, 49],
]
# 4x6 matrix
​
# number of rows is n, number of columns is m
# time complexity
def zero_matrix(matrix):
    set_row = []
    set_col = []
    #Add  total time complexities
    #O(n*m)
    for row_count in range(len(matrix)): #O(n)
        row = matrix[row_count]
        for col_count in range(len(row)): #O(m)
            value = row[col_count]
            if value == 0:
                set_row.append(row_count)
                set_col.append(col_count)
​
    #O(nm)
    for row in set_row: #O(n)
        for col in range(len(matrix[row])): #O(m)
            matrix[row][col] = 0
​
    #O(nm)
    for col in set_col: #O(m)
      for row in range(len(matrix)): #O(n)
        matrix[row][col] = 0
​
    print(matrix)
​
zero_matrix(matrix)