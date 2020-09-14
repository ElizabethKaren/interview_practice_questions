#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands 
#horizontally or vertically. You may assume all four edges of the grid are all 
#surrounded by water.

#Example 1:

grid = [
 ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
#Output: 1

def helper_method(row, column, grid):
    if row+1 < len(grid) and grid[row+1][column] == str(1):
        grid[row +1][column] = 2
        helper_method(row+1, column, grid)
        
    if column+1 < len(grid[row]) and grid[row][column+1] == str(1):
        grid[row][column+1] = 2
        helper_method(row, column+1, grid)
        
    if row-1 >= 0 and grid[row-1][column] == str(1):
        grid[row -1][column] = 2
        helper_method(row-1, column, grid)
        
    if column -1 >= 0 and grid[row][column-1] == str(1):
        grid[row][column-1] = 2
        helper_method(row, column-1, grid)


def find_islands(grid):
    num_of_islands = 0
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            num = grid[row][column]
            if num == str(1):
                num_of_islands += 1
                print(grid)
                helper_method(row, column, grid)

    return num_of_islands



    # def helper_method(row, column, grid, num_of_islands):
    #     if row+1 < len(grid) and grid[row+1][column] == str(1):
    #         grid[row +1][column] = 2
    #         helper_method(row+1, column, grid, num_of_islands)
        
    #     if column+1 < len(grid[row][column]) and grid[row][column+1] == str(1):
    #         grid[row][column+1] = 2
    #         helper_method(row, column +1, grid, num_of_islands)
        
    #     if row-1 > 0 and grid[row-1][column] == str(1):
    #         grid[row +1][column] = 2
    #         helper_method(row -1, column, grid, num_of_islands)
        
    #     if column -1 > 0 and grid[row][column-1] == str(1):
    #         grid[row][column-1] = 2
    #         helper_method(row, column - 1, grid, num_of_islands)

    #     else:
    #         find_islands(grid,num_of_islands)

print(find_islands(grid))