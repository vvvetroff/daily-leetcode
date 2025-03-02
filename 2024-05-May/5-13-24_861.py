'''
861. Score After Flipping Matrix

Difficulty: Medium
Topics: Array, Greedy, Bit Manipulation, Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each
value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number,
and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).

Submitted on 5-13-24, 45ms runtime, O(n*m)
'''

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # flip row if MSB is 0
        for r in range(m):
            if grid[r][0] == 0:
                for c in range(n):
                    grid[r][c] = 0 if grid[r][c] else 1

        # flip column if there are more 0s than 1s
        for c in range(n):
            count = 0
            for r in range(m):
                count += grid[r][c]
            if count < m - count:
                for r in range(m):
                    grid[r][c] = 0 if grid[r][c] else 1
        
        # get decimal number from each row, add to total
        total = 0
        for r in range(m):
            for c in range(n-1,-1,-1):
                if grid[r][c] == 1:
                    shift = n - c - 1
                    total += 1 << shift

        return total
