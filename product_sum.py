array = [5, 2, [7,-1], 3, [6,[-13, 8],4] ]

def product_sum(array, multiplier = 1):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) is int:
            sum += array[i]
        else:
            num = product_sum(array[i], multiplier + 1)
            sum += num
    return sum * multiplier



print(product_sum(array))