array = [
    [1, 2, 3, 4],
    [12,13,14, 5],
    [11,16,15, 6],
    [10, 9, 8, 7]
]

def spiral_traverse(array):
    new_array = []
    begining = True
    down = False
    for i in range(len(array)):
        for j in range(len(array[i])):
            if begining:
                new_array.append(array[i][j])
            else:
                new_array.append(array[i][j])
        if begining:
            begining = False 
        else:
            begining = True
    return new_array




print(spiral_traverse(array))