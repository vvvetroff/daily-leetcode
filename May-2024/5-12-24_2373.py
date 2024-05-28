'''
2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid

Generate an integer matrix 'maxLocal' of size (n-2)x(n-2) such that:
- maxLocal[i][j] is equal to the largest value of the 3x3 matrix in grid centered around row i+1 and column j+1

In other words, we want to find the largest value in every contiguous 3x3 matrix in grid.

Return the generated matrix.

Submitted on 5-12-24, 114ms runtime (yay), O(n^2)

Since each i,j pair in maxLocal represents the max of a 3x3 matrix, 
iterate thru maxLocal, taking the max of 9 values. 
'''

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0 for i in range(n-2)] for j in range(n-2)]
        n = len(maxLocal)
        for i in range(n):
            for j in range(n):
                maxLocal[i][j] = max(grid[i][j],
                                     grid[i][j+1],
                                     grid[i][j+2],
                                     grid[i+1][j],
                                     grid[i+1][j+1],
                                     grid[i+1][j+2],
                                     grid[i+2][j],
                                     grid[i+2][j+1],
                                     grid[i+2][j+2])
        return maxLocal
