'''
1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:
- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.  
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold.

Submitted on 5-14-23
'''

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        direct = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()

        def dfs(r, c):
            countingsum = grid[r][c] 
            for dr, dc in direct:
                if (r+dr in range(row)) and (c+dc in range(col)) and grid[r+dr][c+dc] and (r+dr,c+dc) not in visited:
                    visited.add((r+dr, c+dc))
                    countingsum = max(countingsum, grid[r][c] + dfs(r+dr, c+dc))
                    visited.remove((r+dr, c+dc))           

            return countingsum

        value = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    visited.add((r, c))
                    value = max(value, dfs(r,c))
                    visited.remove((r, c))
        
        return value

