#Given an integer number n
#return the difference between 
#the product of its digits and the sum of its digits.

n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def subtract_product_sum(num):
    sum = find_sum(num)
    product_sum = find_product(num)
    print(product_sum)
    return abs(sum - product_sum)


def find_sum(num):
    old_num = str(num)
    return_num = 0
    for i in old_num:
        return_num += int(i)

    return return_num

def find_product(num):
    old_num = str(num)
    return_num = 1
    for i in old_num:
        return_num = return_num * int(i)

    return return_num


print(subtract_product_sum(n))