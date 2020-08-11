t = "aaaaaaaa"
s = "aaa"
#output = 4

def almostSubstring(t, s):
    num_of_times = 0
    for letter in t:
        if letter in s:
            print(letter)
            num_of_times += 1
                    
    return int(num_of_times/3)


print(almostSubstring(t,s))