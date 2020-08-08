# year = 1905
# the output should be
# centuryFromYear(year) = 20;
year = 1700
#the output should be
# centuryFromYear(year) = 17.


def centuryFromYear(year):
    time = str(year)
    print(time[3])
    if int(time[2]) == 0 and int(time[3]) == 0:
        return time[0] + time[1]
    else:
        return int(time[0] + time[1]) + 1


print(centuryFromYear(year))