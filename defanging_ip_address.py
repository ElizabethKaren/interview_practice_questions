address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

def defanging_ip(address):
    arr = [char for char in address]
    for index in range(len(arr)):
        if arr[index] == ".":
            arr[index] = "[.]"

    return ''.join(arr)



print(defanging_ip(address))