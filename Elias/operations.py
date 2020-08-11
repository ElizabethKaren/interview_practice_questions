#INSERT DELETE COPY PASTE UNDO(undos last successful insert, delete, or paste)
#you are giben operations, an array of strings where each is an opperation
# of one of the five types above. Your task is to find the resulting text after performing the operation
#note: an operation is considered successful if the text in editor is changed after the operation is completed 
#in particular, deleting the last character of an empty text and pasting an empry string are unsuccesfful operations

# operations = ['INSERT code', 'INSERT Signal', 'DELETE', 'UNDO'] #"CodeSignal" 
operations = ['INSERT Da', 'COPY 0', 'UNDO', 'PASTE', 'PASTE', 'COPY 2', 'PASTE', 'PASTE', 'DELTE', 'INSERT aaam']

def perform_operations(operation):
    return_arr = []
    last_string = ''
    copy_string = ''
    for i in range(len(operations)):
        print(return_arr)
        string = operations[i]
        prevStr = operations[i-1]
        if 'INSERT' in string:
            return_arr.append(string[7:])
            last_string = string[7:]
        elif 'COPY' in string:
            print(string)
            num = int(string[5:])
            copy_string = return_arr[num-1]
        elif 'PASTE' in string:
            return_arr.append(copy_string)
        elif 'DELETE' in string:
            last_string = return_arr[len(return_arr)-1]
            return_arr = return_arr[:len(return_arr)-1]
        elif 'UNDO' in string:
            ##seperate logic 
            if 'DELETE' in prevStr:
                return_arr.append(last_string)
            # elif 'COPY' in prevStr:
            #     copy_string = ''
            else:
                return_arr = return_arr[:len(return_arr)-1]
    
    return ''.join(return_arr)

print(perform_operations(operations))