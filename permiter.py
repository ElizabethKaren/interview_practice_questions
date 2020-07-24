Input = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
 ]

#Output: 16

def islandPerimeter(grid):
        perimeter = 0
        row = 0
        while row < len(grid):
            inner_array = grid[row]
            col = 0
            while col < len(inner_array):
                if grid[row][col] == 1:
                   perimeter += 4
                   
                   if grid[row+1][col] == 1:
                       perimeter -= 1

                   if grid[row][col -1] == 1:
                       perimeter -= 1

                   if grid[row -1][col] == 1:
                       perimeter -= 1

                   if grid[row][col +1] == 1:
                        perimeter -= 1
               
                col += 1
            row += 1

        return perimeter
        
        #grid[0] = row
        #grid[0][0] = row, col, specific value

print(islandPerimeter(Input))