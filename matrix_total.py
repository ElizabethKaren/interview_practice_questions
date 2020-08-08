matrix= [[1,1,1,0], 
        [0,5,0,1], 
        [2,1,3,10]]

def matrixElementsSum(matrix):
    total_sum = 0
    outter_count = 0
    while outter_count < len(matrix):
        inner_count = 0
        while inner_count < len(matrix[outter_count]):
            new_num = matrix[outter_count][inner_count]
            if outter_count + 1 < len(matrix): 
                possible_zero = matrix[outter_count+1][inner_count]
                if possible_zero != 0:
                    print(new_num)
                    total_sum += new_num
            inner_count += 1
        outter_count +=1
    
    return total_sum

print(matrixElementsSum(matrix))