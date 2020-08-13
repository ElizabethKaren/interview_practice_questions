#Given two integer arrays startTime and 
#endTime and given an integer queryTime.
#The ith student started doing their homework 
#at the time startTime[i] and finished it at time endTime[i].
#Return the number of students doing their homework 
#at time queryTime. More formally, return the number 
#of students where queryTime lays in the interval 
#[startTime[i], endTime[i]] inclusive.

startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5


def students_working(startTime, endTime, queryTime):
    how_many_students = 0
    for count in range(len(startTime)):
        if queryTime >= startTime[count] and queryTime <= endTime[count]:
            how_many_students += 1

    return how_many_students


print(students_working(startTime,endTime,queryTime))