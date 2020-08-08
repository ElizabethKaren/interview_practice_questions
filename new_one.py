year = 1905
# the output should be
# centuryFromYear(year) = 20;
# year = 1700
#the output should be
# centuryFromYear(year) = 17.
# year = 200
# output = 2


def centuryFromYear(year):
    return (year -1 )//100 + 1
    
    

print(centuryFromYear(year))