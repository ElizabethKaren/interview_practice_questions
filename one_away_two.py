def one_away(string1, string2):
    if string1 == string2:
        return True
    elif len(string1) == len(string2):
        return replaced_string(string1, string2)
    elif len(string1) == len(string2) + 1:
        return insert(string1, string2)
    elif len(string2) == len(string1) + 1:
        return insert(string2, string1)

def insert(big, small):
    j = 0
    i = 0
    inserted = False

    while(i < len(small)):
        if big[j] != small[i]:
            if inserted:
                return False
            else:
                inserted = True
                i -= 1
        i += 1
        j += 1
        print("i: ", i,"j: ", j, big[j], small[i], inserted)
    return True


def replaced_string(string1, string2):
    replaced = False
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            if (replaced):
                return False
            else:
                replaced = True
    return True


print(one_away("Elias", "Elit"))
