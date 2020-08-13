#On a plane there are n points with integer coordinates 
#points[i] = [xi, yi]. Your task is to find the minimum
#time in seconds to visit all points.
#You can move according to the next rules:
#In one second always you can either move vertically, 
#horizontally by one unit or diagonally (it means to 
#move one unit vertically and one unit horizontally in one second).
#You have to visit the points in the same order as they appear in the array.

points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds

# points = [[3,2],
#          [-2,2]]
# Output: 5

def min_time_to_visit_all_points(points):
    jumps = 0
    for index in range(len(points)-1):
        next_to = points[index + 1][0] - points[index][0]
        accross = points[index + 1][1] - points[index][1]
        if next_to == accross:
            move = next_to
        else:
            move = next_to + accross
        jumps += abs(move)

    return jumps
        



print(min_time_to_visit_all_points(points))