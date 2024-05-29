'''
70. Climbing Stairs

Difficulty: Easy
Topics: Math, Dynamic Programming, Memoization

You are climbing a staircase. It takes 'n' steps to reach the top

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

O(2^n) naive solution initially.
With Memoization, O(n) time & O(n) space complexity.
VERY similar to fibonacci in implementation.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        def memo(n, dp):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if dp[n] > 0:
                return dp[n]
            result = memo(n-1, dp) + memo(n-2, dp)
            dp[n] = result
            return result
        return memo(n, dp)



