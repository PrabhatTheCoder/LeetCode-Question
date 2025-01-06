class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # making 1st column all 1's
        for i in range(len(grid)):
            if grid[i][0] == 0:
                for j in range(len(grid[0])):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0


        # find no of zeros and one's if zeros > ones then flip the column
        for j in range(len(grid[0])):
            zeros = 0
            ones = 0

            for i in range(len(grid)):
                if grid[i][j] == 0:
                    zeros += 1
                else:
                    ones += 1
            
            if zeros > ones:
                for i in range(len(grid)):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0

        # Calculating Matrix Score   8 4 2 1
        score = 0
        for i in range(len(grid)):
            x = 1
            for j in range(len(grid[0])-1,-1,-1):
                score += grid[i][j]*x
                x *= 2
        return score

        
        