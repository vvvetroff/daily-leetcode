'''
118. Pascal's Triangle

Difficulty: Easy
Topics: Array, Dynamic Programming

Given an integer numRows,
return the first numRows of Pascal's Triangle

In Pascal's Triangle,
each number is the sum of the two numbers
directly above it.

This was the first of many Dynamic Programming problems.
This was somewhat good practice on the principles
of Dynamic Programming, but not really much help
for my Algoritms course.
Nevertheless, this was fun to code
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = []
        for i in range(numRows):
            dp.append([1]*(1+i))
        if numRows == 1 or numRows == 2:
            return dp
        
        rowsLeft = numRows - 2
        curRow = 2
        while rowsLeft > 0:
            l = 0
            r = 1
            index = 1
            while r < len(dp[curRow])-1:
                result = dp[curRow-1][l] + dp[curRow-1][r]
                dp[curRow][index] = result
                l += 1
                r += 1
                index += 1
            rowsLeft -= 1
            curRow += 1
        return dp



