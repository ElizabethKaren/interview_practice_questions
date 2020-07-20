# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, # 11 0

# aabcccccaaa
# current variable, when the value switches, reset count
# add current and current count to an empty string
# aabcccccaaa
# current = a, a a, b, add a and its count to a string, reset count
# current = b, add b and its count to the string, reset count
# current = c, add one to count, c add one to count, ... x5 c add one to count, reach a, add c and its count to string, reset count
# current = a, a, a, a, reach end of length of string, add a and its count to the string
#compare lengths, and the str that is shorter will be returned

def string_compression(string):
    i = 0
    current_count = 0
    checked_against = ""
    return_string = ''
    while i<len(string):
        current = string[i]
        if current != checked_against:
            if current_count != 0:
                return_string += checked_against + str(current_count)
            checked_against = current
            current_count = 0
        current_count += 1
        i += 1
        print(current, return_string, checked_against)

    return_string += checked_against + str(current_count)
    print(return_string)

string_compression("aabcccccaaa")
