array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

def add_sums_w_window(array,k):
    result = []
    window_start = 0
    while window_start < len(array)-k+1:
        new_array = array[window_start: window_start + k]
        num = sum(new_array)/k
        result.append(num)
        window_start += 1 
    return result

print(add_sums_w_window(array,k))