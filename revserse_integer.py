#num = 123
# Output: 321

num = -123
# Output: -321

# num = 120
# Output: 21

def reverse_int(num):
    neg = False
    new_num = ''
    old_num = str(num)
    if old_num[0] == '-':
        old_num = old_num[1:]
        neg = True
    for i in old_num:
        new_num = i + new_num
    
    if neg:
        new_num = '-' + new_num

    return int(new_num)


print(reverse_int(num))