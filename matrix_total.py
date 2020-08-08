matrix= [[1,1,1,0], 
        [0,5,0,1], 
        [2,1,3,10]]

def matrixElementsSum(m):
    r = len(m)
    c = len(m[0])
    total=0
    for j in range(c):
        for i in range(r):
            if m[i][j]!=0:
                total+=m[i][j]
            else:
                break
    return total

print(matrixElementsSum(matrix))