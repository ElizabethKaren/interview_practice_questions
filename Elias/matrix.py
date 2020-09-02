#Given an N by N matrix, the matrix has numbers from 1 to N, where the numbers
#in a row or column cannot repeat, return "VALID" if the matrix is valid, 
#return "INVALID" if the matrix is invalid

matrix = [[ 1,2,3 ], 
          [ 2,3,1 ], 
          [ 3,1,2 ]]
# matrix = [[1,2,3], 
#           [1,2,3], 
#           [1,2,3]]


def function(matrix):
    size = len(matrix)
    for row in range(size):
        d = {}
        for column in range(size):
            num = matrix[row][column]
            if num < 1 and num > size:
                return 'INVALID'
            if num in d:
                return 'INVALID'
            else:
                d[num] = True
        
        for column in range(size):
            d = {}
            for row in range(size):
                num = matrix[row][column]
                if num in d:
                    return 'INVALD'
                else:
                    d[num] = True
    
    return 'VALID'


# def repeat(theNum, array):
#     appearence = 0
#     for num in array:
#         if theNum == num:
#             appearence += 1

#     return appearence == 1



    # outter = 0
    # while outter < len(matrix):
    #     inner = 0
    #     firstNum = matrix[outter][inner]
    #     for num in range(inner,len(matrix)):
    #         print(num, firstNum)
    #         if firstNum == matrix[outter][num]:
    #             return 'INVALID'
    #     outter += 1

    # return 'VALID'

print(function(matrix))