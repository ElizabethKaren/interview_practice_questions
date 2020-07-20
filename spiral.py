array = [
    [1,2,3,4],
    [12,11,10,9],
    [16,15,14,13],
    [10,9,8,7]
]


def spiralTraverse(array):
    new_array = []
    outter_index = 0
    while outter_index < len(array):
        inner_array = array[outter_index]
        if outter_index % 2 == 0:
            for i in inner_array:
                new_array.append(i)
        else:
            for i in reversed(inner_array):
                new_array.append(i)
        outter_index += 1 
    return new_array

print(spiralTraverse(array))
