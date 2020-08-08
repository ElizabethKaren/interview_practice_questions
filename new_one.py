# year = 1905
# the output should be
# centuryFromYear(year) = 20;
year = 1700
#the output should be
# centuryFromYear(year) = 17.
# year = 200
# output = 2


def centuryFromYear(year):
    time = str(year)
    if len(time) == 4:
        end_of_time = time[2:]
    else:
        end_of_time = time[1:]

    for num in end_of_time:
        if int(num) != 0:
           return how_many_digets(str(year), 1)

    return how_many_digets(str(year))
    
    

def how_many_digets(year, num=0):
    if len(year) == 4:
        return int(year[0] + year[1]) + num
    elif len(year) == 3:
        return int(year[0]) + num
    else:
        return 1

print(centuryFromYear(year))