n = 6 

def last_two_in_fib(n):
    last_two = [0,1]
    counter = 3 
    while counter <= n:
        new_num = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = new_num
        counter += 1 

    return last_two[1] if n > 1 else last_two[0]


print(last_two_in_fib(n))