'''
1137. N-th Tribonacci Number

Difficulty: Easy
Topics: Math, Dynamic Programming, Memoization

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Another DP practice. Not good, but still
O(n)
'''

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        return dp[n]



