def minimumHours(rows, columns, grid):
    # WRITE YOUR CODE HERE
    count = 0
    new = grid[:][:]

    while any(0 in x for x in board):
        for i in range(rows):
            for j in range(columns):
                count = count + 1
                if j == 0 && i == 0:
                    if grid[i][j + 1] == 1 || grid[i + 1][j] == 1:
                        new[i][j] = 1 
                elif i == row - 1 && j == colums - 1:
                    if grid[i][j - 1] == 1 || grid[i - 1][j] == 1:
                        new[i][j] = 1
                elif 0 < i < row - 1 && 0 < j < columns:
                        if grid[i][j - 1] == 1 || grid[i][j +1]:
                            new[i][j] = 1 
                        elif grid[i - 1][j] == 1 || grid[i + 1][j]:
                            new[i][j] = 1
     return count
