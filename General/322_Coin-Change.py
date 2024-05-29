'''
322. Coin Change

Difficulty: Medium
Topics: Array, Dynamic Programming, Breadth-First Search

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Classic DP Problem, also saw it on a youtube video
I believe it is a Knapsack problem, not too sure
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [inf for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            result = dp[i]
            for coin in coins:
                if i - coin < 0: continue
                result = min(result, 1+dp[i-coin])
            dp[i] = result
        return dp[amount] if dp[amount] != inf else -1



