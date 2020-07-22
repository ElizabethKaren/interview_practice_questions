#returns permutaions of an array in no particular order 
array = [1,2,3]

def find_permutations_long_way(array):
    length_of_array = len(array) -1 
    array_of_perms = []
    count = 0
    while count < len(array):
        sub_array = []
        sub_array.append(array[count])
        sub_array.append(array[count - length_of_array])
        sub_array.append(array[count - length_of_array + 1])
        array_of_perms.append(sub_array)
        second_sub_array = []
        second_sub_array.append(array[count])
        second_sub_array.append(array[count - length_of_array + 1])
        second_sub_array.append(array[count - length_of_array])
        array_of_perms.append(second_sub_array)

        count += 1

    return array_of_perms

def find_permutations(array):
    permutations = []
    permutationsHepler(array, [], permutations)
    return permutations

def permutationsHepler(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i+1:]
            print(new_array)
            new_permutation = currentPermutation + [array[i]]
            permutationsHepler(new_array, new_permutation, permutations)



print(find_permutations(array))